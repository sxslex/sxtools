# -*- coding: utf-8 -*-

import sxtools


def test_remove_accents_1():
    assert sxtools.remove_accents('Olá') == 'Ola'


def test_remove_accents_2():
    assert sxtools.remove_accents(u'Olá') == 'Ola'
