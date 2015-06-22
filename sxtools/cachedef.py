# -*- encoding: utf-8 -*-
# -----------------------------------------------------------------------------
# @name:        cachedef.py
# @description: Allow decorate a method with a cache to increase
#               performance of costly methods
# @author:      SleX - slex@slex.com.br
# @created:     09:37 30/01/2013
# @version:     0.2.5
# -----------------------------------------------------------------------------
import os
import pprint
import hashlib
import datetime
from functools import wraps


def _loads(s, ftype='pickle'):
    if ftype == 'pickle':
        import cPickle
        return cPickle.loads(s)
    if ftype == 'literal':
        import ast
        return ast.literal_eval(s)
    raise Exception('ftype "%s" not supported' % ftype)


def _dumps(s, ftype='pickle'):
    if ftype == 'literal':
        return s.__repr__()
    if ftype == 'pickle':
        import cPickle
        return cPickle.dumps(s)
    raise Exception('ftype "%s" not supported' % ftype)


def getpathfiledir(path, filename, nivel=3, numc=2):
    patha = path.replace('\\', '/')
    directory = ''
    for d in patha.split('/'):
        directory += d
        if d and not os.path.exists(directory):
            os.mkdir(directory, 0775)
            os.chmod(directory, 0775)
        directory += '/'
    for i in xrange(0, nivel):
        sub = filename[i * numc:(i * numc) + numc]
        directory += '%s/' % sub
        if not os.path.exists(directory):
            os.mkdir(directory, 0775)
            os.chmod(directory, 0775)
    return directory + filename


def getcontextfile(pathfile, minuteexpire=5, debug=False, ftype='pickle'):
    if not os.path.exists(pathfile):
        return None
    timestamp = datetime.datetime.fromtimestamp(os.path.getmtime(pathfile))
    r = (datetime.datetime.now() - timestamp)
    horas = ((r.days * 24 * 60) + r.seconds / 60)
    if debug:
        print('expires in %s minutes' % str(minuteexpire - horas))
    if horas < minuteexpire:
        f = open(pathfile, 'r')
        try:
            try:
                return _loads(f.read(), ftype=ftype)
            except:
                return None
        finally:
            f.close()
    else:
        if os.path.isdir(pathfile):
            os.rmdir(pathfile)
        else:
            os.remove(pathfile)
    return None


def setcontextfile(pathfile, context, ftype='pickle'):
    if os.path.exists(pathfile):
        os.remove(pathfile)
    f = open(pathfile, 'w')
    try:
        f.write(_dumps(context, ftype=ftype))
        return True
    finally:
        f.close()
        os.chmod(pathfile, 0664)
    return False


def getcache(config, *args, **kwargs):
    if os.path.isdir(config.get('path', '')):
        newkwargs = kwargs.copy()
        if 'ignore_cache' in newkwargs:
            newkwargs.pop('ignore_cache')
        seed = pprint.pformat([args, newkwargs])
        pathfile = getpathfiledir(
            config['path'],
            hashlib.md5(
                config.get('seed', '') +
                config['path'] +
                seed
            ).hexdigest(),
        )
        if config.get('debug'):
            print([pathfile, seed])
        return getcontextfile(
            pathfile=pathfile,
            minuteexpire=config.get(
                'minuteexpire',
                60 * 24 * 7
            ),
            debug=config.get('debug'),
            ftype=config.get('ftype', 'literal')
        )
    return None


def setcache(config, context, *args, **kwargs):
    if config.get('path', ''):
        newkwargs = kwargs.copy()
        if 'ignore_cache' in newkwargs:
            newkwargs.pop('ignore_cache')
        seed = pprint.pformat([args, newkwargs])
        pathfile = getpathfiledir(
            config['path'],
            hashlib.md5(
                config.get('seed', '') + config['path'] + seed
            ).hexdigest(),
        )
        if config.get('debug'):
            print([pathfile, seed])
        return setcontextfile(
            pathfile=pathfile,
            context=context,
            ftype=config.get('ftype', 'literal')
        )
    return False


class CacheDef(object):

    """
        Decorator responsible for making a cache of the results
        of calling a method in accordance with the reported.

        Arguments:
            seed -- string to differentiate the caches
            path -- path to store the cache
            minuteexpire -- time in minutes for validity of cache
            debug -- bool active debug mode
            ftype -- so that to store the cache ('pickle', 'literal')

    """

    def __init__(self, seed, path=None, minuteexpire=60, debug=False,
                 ftype='pickle'):
        if not path:
            path = '/tmp/cachedef'
            if os.path.exists('c:/'):
                path = 'c:/tmp/cachedef'
        self.__config = {
            'seed': seed,
            'path': path + '/' + seed,
            'debug': debug,
            'minuteexpire': minuteexpire,
            'ftype': ftype
        }

    def __call__(self, call, *args, **kwargs):
        self.config = self.__config.copy()
        self.config['path'] = self.config['path'] + '/' + call.func_name

        @wraps(call)
        def newdef(*args, **kwargs):
            resp = None
            if not kwargs.get('ignore_cache'):
                resp = getcache(
                    self.config,
                    *args,
                    **kwargs
                )
            if resp is None:
                if self.config.get('debug'):
                    print('not cache')
                if (
                    'ignore_cache' not in call.func_code.co_varnames
                ) and (
                    'ignore_cache' in kwargs
                ):
                    kwargs.pop('ignore_cache')
                resp = call(*args, **kwargs)
                setcache(
                    self.config,
                    resp,
                    *args,
                    **kwargs
                )
                if self.config.get('debug'):
                    print('save cache')
            else:
                if self.config.get('debug'):
                    print('get cache')
            return resp
        return newdef


def cachedef(seed, path=None, minuteexpire=60, debug=False, ftype='pickle'):
    """
        Decorator responsible for making a cache of the results
        of calling a method in accordance with the reported.

        Arguments:
            seed -- string to differentiate the caches
            path -- path to store the cache
            minuteexpire -- time in minutes for validity of cache
            debug -- bool active debug mode
            ftype -- so that to store the cache ('pickle', 'literal')

    """
    return CacheDef(seed=seed, path=path, minuteexpire=minuteexpire,
                    debug=debug, ftype=ftype)


def test():
    import datetime
    alreadycached = False

    @cachedef(seed='CacheDef')
    def calculation_slow(a, b):
        import time
        time.sleep(3)
        return a + b

    def exec_calc(a, b):
        # get now time
        start = datetime.datetime.now()
        # call function slow
        if not alreadycached:
            calculation_slow(
                a,
                b,
                ignore_cache=True
            )
        else:
            calculation_slow(
                a,
                b
            )
        # takes the time to answer
        cost = datetime.datetime.now() - start
        # brow caught cache
        if alreadycached and cost > datetime.timedelta(seconds=2):
            raise Exception('not already cached')
        return 'cost: %s ' % str(cost)

    alreadycached = False
    print('\n*** test')
    print(exec_calc(4, 44))
    alreadycached = True
    print(exec_calc(4, 44))
    print(exec_calc(4, 44))
    return True


if __name__ == '__main__':
    test()
