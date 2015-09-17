# -*- encoding: utf-8 -*-
# -----------------------------------------------------------------------------
# @name:                string_utils.py
# @description:         functions to work with packets strings
# @author:              SleX - slex@slex.com.br
# @created:             2015-09-14
# @version:             0.1
# @requirements:        #rome==0.0.3
# -----------------------------------------------------------------------------

from __future__ import unicode_literals

_articles = [
    'a', 'o', 'em', 'e', 'da', 'de', 'di', 'do', 'du', 'das', 'dos', 'dus'
]


def capitalize_name(full_name, articles=_articles):
    if not full_name:
        return full_name
    s = to_unicode(full_name)
    return s.capitalize()


def to_unicode(s, encodings=['utf-8', 'latin-1']):
    if isinstance(s, (list, tuple)):
        return [to_unicode(i) for i in s]
    if isinstance(s, (dict)):
        return {key: s[key] for key in s}
    elif isinstance(s, str):
        for encoding in encodings:
            try:
                return s.decode(encoding)
            except:
                pass
    return s
