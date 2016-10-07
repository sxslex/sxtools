# -*- coding: utf-8 -*-
"""Decorator to cache methods."""
# Copyright 2015 Alexandre Villela (SleX) <https://github.com/sxslex/sxtools/>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Allow decorate a method with a cache to increase
# performance of costly methods
#    by sx.slex@gmail.com
#    cache_def - version 0.0.5
# Thanks:
#   @denisfrm
#
# from __ future__ import unicode_literals
import os
# import copy
# import types
# import codecs
import pprint
import hashlib
import datetime
import platform
from functools import wraps
try:
    import cPickle
except:
    import pickle as cPickle


def _loads(s, ftype='pickle'):
    if ftype == 'pickle':
        return cPickle.loads(s)
    if ftype == 'literal':
        import ast
        return ast.literal_eval(s)
    raise Exception('ftype "%s" not supported' % ftype)


def _dumps(s, ftype='pickle'):
    if ftype == 'pickle':
        return cPickle.dumps(s)
    if ftype == 'literal':
        r = pprint.pformat(s).encode('utf-8')
        return r
    raise Exception('ftype "%s" not supported' % ftype)


def _getpathfiledir(path, filename, nivel=3, numc=2):
    newpath = os.path.join(
        path.replace('\\', '/'),
        '/'.join([
            filename[i * numc:(i * numc) + numc] for i in range(nivel)
        ]),
        filename
    )
    if not os.path.exists(newpath):
        os.makedirs(newpath, 0o775)
    return os.path.join(newpath, filename)


def _getcontextfile(pathfile, minuteexpire=5, debug=False, ftype='pickle'):
    if not os.path.exists(pathfile):
        return None
    timestamp = datetime.datetime.fromtimestamp(os.path.getmtime(pathfile))
    r = (datetime.datetime.now() - timestamp)
    horas = ((r.days * 24 * 60) + r.seconds / 60.0)
    if debug:
        print('expires in %s minutes' % str(minuteexpire - horas))
    if os.path.isdir(pathfile):
        os.rmdir(pathfile)
        return None
    if horas < minuteexpire:
        f = open(pathfile, 'rb')
        content = f.read()
        try:
            try:
                return _loads(content, ftype=ftype)
            except:
                return None
        finally:
            f.close()
    os.unlink(pathfile)
    return None


def _setcontextfile(pathfile, context, ftype='pickle'):
    if os.path.exists(pathfile):
        os.unlink(pathfile)
    f = open(pathfile, 'wb')
    try:
        content = _dumps(context, ftype=ftype)
        f.write(content)
        return True
    finally:
        f.close()
        os.chmod(pathfile, 0o664)


def _gera_hash(config, args, kwargs):
    # Monta o cache da consulta de acordo com os parametros passados
    new_args = args
    newkwargs = kwargs.copy()
    if 'renew_cache' in newkwargs:
        newkwargs.pop('renew_cache')
    s = (
        config.get('seed', '') +
        config.get('path', '') +
        config.get('redishost', '') +
        pprint.pformat([new_args, newkwargs])
    )
    if hasattr(s, 'encode'):
        s = s.encode('utf-8')
    return hashlib.md5(s).hexdigest()


def _getcache(config, *args, **kwargs):
    value_md5 = _gera_hash(config=config, args=args, kwargs=kwargs)
    if config.get('redishost'):
        import redis
        r = redis.Redis(config.get('redishost'))
        resp = r.get('cache:' + config.get('seed', '') + ':' + value_md5)
        if resp:
            try:
                return _loads(resp, ftype=config.get('ftype', 'pickle'))
            except:
                return None
        return None
    if config.get('path'):
        if os.path.isdir(config.get('path', '')):
            pathfile = _getpathfiledir(
                config['path'],
                value_md5,
            )
            if config.get('debug'):
                print([pathfile, value_md5])
            return _getcontextfile(
                pathfile=pathfile,
                minuteexpire=config.get(
                    'minuteexpire',
                    60 * 24 * 7
                ),
                debug=config.get('debug'),
                ftype=config.get('ftype', 'pickle')
            )
    return None


def _setcache(config, context, *args, **kwargs):
    value_md5 = _gera_hash(config=config, args=args, kwargs=kwargs)
    # cache in redis
    if config.get('redishost'):
        import redis
        r = redis.Redis(config.get('redishost'))
        r.set(
            'cache_' + config.get('seed', '') + '_' + value_md5,
            _dumps(context, ftype=config.get('ftype', 'pickle')),
            ex=int(config.get(
                'minuteexpire',
                60 * 24 * 7
            ) * 60)
        )
        return True

    # cache in file
    pathfile = _getpathfiledir(
        config['path'],
        value_md5,
    )
    if config.get('debug'):
        print([pathfile, value_md5])
    return _setcontextfile(
        pathfile=pathfile,
        context=context,
        ftype=config.get('ftype', 'literal')
    )


class CacheDef(object):
    """
    Decorator responsible for making a cache.

    Decorator responsible for making a cache of the results of calling a
    method in accordance with the reported.
        Arguments:
            seed -- string to differentiate the caches
            redishost -- host redis server
            path -- path to store the cache
            minuteexpire -- time in minutes for validity of cache
            debug -- bool active debug mode
            ftype -- so that to store the cache ('pickle', 'literal')
    """

    def __init__(
        self,
        seed,
        path=None,
        redishost=None,
        minuteexpire=60,
        debug=False,
        ftype='pickle'
    ):
        """."""
        if not path and not redishost:
            path = '/tmp/cachedef'
            if platform.system() == 'Windows':
                path = 'c:/tmp/cachedef'
        self.__config = {
            'seed': seed,
            'debug': debug,
            'minuteexpire': minuteexpire,
            'ftype': ftype,
        }
        if redishost:
            self.__config['redishost'] = redishost
        elif path:
            self.__config['path'] = path + '/' + seed

    def __call__(self, call, *args, **kwargs):
        """."""
        self.config = self.__config.copy()
        # self.config['path'] = self.config['path']  # + '/' + call.func_name

        @wraps(call)
        def newdef(*args, **kwargs):
            resp = None
            is_im_class = (
                hasattr(args[0], call.__name__)
            )
            xargs = args
            if is_im_class:
                xargs = args[1:]
            # if self.config.get('debug'):
            #     pprint.pprint(
            #         dict(
            #             is_im_class=is_im_class,
            #             xargs=xargs,
            #             kwargs=kwargs,
            #             icall=getattr(args[0], call.__name__),
            #             call=call,
            #         )
            #     )
            if not kwargs.get('renew_cache'):
                resp = _getcache(
                    self.config,
                    *xargs,
                    **kwargs
                )
            if resp is None:
                # pprint.pprint(call)
                co_varnames = []
                if hasattr(call, 'func_code'):
                    co_varnames = call.func_code.co_varnames
                elif hasattr(call, '__code__'):
                    co_varnames = call.__code__.co_varnames
                if self.config.get('debug'):
                    print('not cache')
                if (
                    'renew_cache' not in co_varnames
                ) and (
                    'renew_cache' in kwargs
                ):
                    kwargs.pop('renew_cache')
                resp = call(*args, **kwargs)
                _setcache(
                    self.config,
                    resp,
                    *xargs,
                    **kwargs
                )
                if self.config.get('debug'):
                    print('save cache')
            else:
                if self.config.get('debug'):
                    print('get cache')
            return resp
        return newdef


def cache_def_clear_expired(
    seed,
    path,
    minuteexpire,
    osmode=True
):
    """Exclue os arquivos de cache."""
    import os
    pathseed = os.path.join(path, seed).replace('\\', '/')
    if os.path.exists(pathseed):
        if osmode:
            command = 'find %s -type f -mmin +%s -exec rm -rf {} \\;' % (
                pathseed,
                str(int(minuteexpire))
            )
            os.system(command)
    return True


def cache_def(
    seed,
    redishost=None,
    path=None,
    minuteexpire=60,
    debug=False,
    ftype='pickle',
):
    """
    Decorator responsible for making a cache.

    Decorator responsible for making a cache of the results
    of calling a method in accordance with the reported.

        Arguments:
            seed -- string to differentiate the caches
            redishost -- host redis server
            path -- path to store the cache
            minuteexpire -- time in minutes for validity of cache
            debug -- bool active debug mode
            ftype -- so that to store the cache ('pickle', 'literal')
    """
    return CacheDef(
        seed=seed,
        redishost=redishost,
        path=path,
        minuteexpire=minuteexpire,
        debug=debug,
        ftype=ftype,
    )
