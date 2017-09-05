# -*- coding: utf-8 -*-
#
# Functions to work with packets strings
#   sx.slex@gmail.com
# Thanks:
#   @denisfrm


from __future__ import unicode_literals

import sys
import unicodedata


def deep_decode(s, encodings=None):
    """Decode "DEEP" S using the codec registered for encoding."""
    if encodings is None:
        encodings = ['utf-8', 'latin-1']
    if isinstance(s, (list, tuple)):
        return [deep_decode(i) for i in s]
    if isinstance(s, dict):
        return dict([
            (deep_decode(key), deep_decode(s[key]))
            for key in s
        ])
        # in_dict = {}
        # for key in s:
        #     in_dict[to_unicode(key)] = to_unicode(s[key])
        # return in_dict
    elif isinstance(s, str):
        for encoding in encodings:
            try:
                return s.decode(encoding)
            except:
                pass
    return s


def deep_encode(s, encoding='utf-8', errors='strict'):
    """Encode "DEEP" S using the codec registered for encoding."""
    # encoding defaults to the default encoding. errors may be given to set
    # a different error handling scheme. Default is 'strict' meaning
    # that encoding errors raise
    # a UnicodeEncodeError. Other possible values are 'ignore', 'replace' and
    # 'xmlcharrefreplace' as well as any other name registered with
    # codecs.register_error that can handle UnicodeEncodeErrors.
    s = deep_decode(s)
    if (
                (
                            not hasattr(sys.version_info,
                                        'major') or sys.version_info.major < 3
                ) and isinstance(s, unicode)
    ):
        return s.encode(encoding, errors)
    if isinstance(s, (list, tuple)):
        return [deep_encode(i, encoding=encoding, errors=errors) for i in s]
    if isinstance(s, dict):
        return dict([
            (
                deep_encode(key, encoding=encoding, errors=errors),
                deep_encode(s[key], encoding=encoding, errors=errors)
            ) for key in s
        ])
        # new_dict = {}
        # for key in s:
        #     new_dict[
        #         to_encode(key, encoding=encoding, errors=errors)
        #     ] = to_encode(s[key], encoding=encoding, errors=errors)
        # return new_dict
    return s


def remove_accents(s):
    resp = deep_decode(s)
    return unicodedata.normalize(
        'NFKD', resp
    ).encode('ASCII', 'ignore').decode('ASCII')


def join_plus(items, sep=', ', end=' e '):
    nitems = deep_decode(items)
    if len(nitems) < 2:
        return end.join(nitems)
    return deep_encode(end.join([sep.join(nitems[:-1]), nitems[-1]]))


def pluralize(word):
    """Put a word in the plural."""
    if not word:
        return word
    nword = deep_decode(word)
    upper = (nword[:-1] == nword[:-1].upper())
    to_do = {
        'ao': 'oes',
        'ão': 'ões',
        'AO': 'OES',
        'ÃO': 'ÕES',
    }
    for to, do in to_do.items():
        if nword.endswith(to):
            return deep_encode(nword[:len(to) * -1] + do)
    if nword[-1] == 's':
        return deep_encode(nword + 'es')
    if nword[-1] == 'S':
        return deep_encode(nword + 'ES')
    if nword[-1] == 'l':
        return deep_encode(nword[:-1] + 'is')
    if nword[-1] == 'L':
        return deep_encode(nword[:-1] + 'IS')
    if upper:
        return deep_encode(nword + 'S')
    return nword + 's'
