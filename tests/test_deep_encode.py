# -*- coding: utf-8 -*-

import sxtools


def test_deep_decode_iso():
    assert sxtools.deep_decode('Ol\xe1', u'Olá')


def test_deep_encode_list():
    assert sxtools.deep_encode(
            ['BRASÍLIA/PLANO PILOTO', 1, True, u'Bolas']
    ) == ['BRASÍLIA/PLANO PILOTO', 1, True, 'Bolas']


def test_deep_encode_dict():
    assert sxtools.deep_encode(
        dict(name=u'BRASÍLIA/PLANO PILOTO', idade=1, sport='Tênis')
    ) == dict(name='BRASÍLIA/PLANO PILOTO', idade=1, sport='Tênis')


def test_deep_encode_latin():
    assert sxtools.deep_encode('Ol\xe1') == 'Olá'


def test_deep_encode_dict():
    assert sxtools.deep_encode({
            'item2': 'olá mundó!',
            'item3': 'ol\xe1 s\xe9m no\xe7\xe3o',
            'item1': u'Caçamba-trêmula'
        }) == {
            'item2': 'olá mundó!',
            'item3': 'olá sém noção',
            'item1': 'Caçamba-trêmula'
        }
