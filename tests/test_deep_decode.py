# -*- coding: utf-8 -*-

import sxtools


def test_deep_decode_str():
    assert (
        sxtools.deep_decode(u'BRASILIA/PLANO PILOTO')
        ==
        'BRASILIA/PLANO PILOTO'
    )


def test_deep_decode_list():
    assert (
        sxtools.deep_decode([u'BRASILIA/PLANO PILOTO', 1, True, u'Bolas'])
        ==
        ['BRASILIA/PLANO PILOTO', 1, True, 'Bolas']
    )


def test_deep_decode_dict():
    assert (
        sxtools.deep_decode(
            dict(name=u'BRASILIA/PLANO PILOTO', idade=1, sport=u'Foo')
        ) == dict(name='BRASILIA/PLANO PILOTO', idade=1, sport='Foo')
    )
