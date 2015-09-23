# -*- coding: utf-8 -*-
#
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
# Functions to work with packets strings
#    by sx.slex@gmail.com
#

from __future__ import unicode_literals
import string
import re

roman_pattern = re.compile(
    '^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$',
    re.VERBOSE
)


_articles = [
    'a', 'o', 'em', 'e', 'da', 'de', 'di', 'do', 'du', 'das', 'dos', 'dus'
]

_separator_characters = string.whitespace + '/'


def capitalize_name(
    full_name,
    articles=_articles,
    separator_characters=_separator_characters
):
    def _ajuste_word(word):
        if word not in separator_characters and word not in articles:
            word = word.upper()
            if not word or not roman_pattern.search(word):
                word = word.capitalize()
        return word
    if not full_name:
        return full_name
    new_full_name = to_unicode(full_name)
    list_full_name = []
    start_idx = 0
    for step_idx, char in enumerate(list(new_full_name)):
        if char in _separator_characters:
            list_full_name.extend(
                [
                    _ajuste_word(new_full_name[start_idx:step_idx]),
                    char
                ]
            )
            start_idx = step_idx + 1
    list_full_name.append(_ajuste_word(new_full_name[start_idx:]))
    return ''.join(list_full_name)


def to_unicode(s, encodings=['utf-8', 'latin-1']):
    if isinstance(s, (list, tuple)):
        return [to_unicode(i) for i in s]
    if isinstance(s, dict):
        in_dict = {}
        for key in s:
            in_dict[to_unicode(key)] = to_unicode(s[key])
        return in_dict
    elif isinstance(s, str):
        for encoding in encodings:
            try:
                return s.decode(encoding)
            except:
                pass
    return s


def to_encode(s, encoding='utf-8'):
    s = to_unicode(s)
    if isinstance(s, unicode):
        return s.encode(encoding)
    if isinstance(s, (list, tuple)):
        return [to_encode(i) for i in s]
    if isinstance(s, dict):
        in_dict = {}
        for key in s:
            in_dict[to_encode(key, encoding)] = to_encode(s[key], encoding)
        return in_dict
    return s
