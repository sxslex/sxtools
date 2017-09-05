# -*- coding: utf-8 -*-

import sxtools


def test_empty():
    assert sxtools.join_plus([]) == ''


def test_one():
    assert sxtools.join_plus(['slex']) == 'slex'


def test_two():
    assert sxtools.join_plus(['Slex', 'Dénis']) == 'Slex e Dénis'


def test_more_than_two():
    assert (
        sxtools.join_plus(
            ['Slex', 'Dénis', 'Rafs'],
            end=' and '
        ) == 'Slex, Dénis and Rafs'
    )
