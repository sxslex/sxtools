# -*- coding: utf-8 -*-

import sxtools


TO_DO = {
    'carro': 'carros',
    'moto': 'motos',
    'caminhao': 'caminhoes',
    'caminhão': 'caminhões',
    'nautico': 'nauticos',
    'CAMINHÃO': 'CAMINHÕES',
    'Legal': 'Legais',
    'LEGAL': 'LEGAIS'
}


def test_pluralize_items():
    for to in TO_DO:
        assert sxtools.pluralize(to) == TO_DO[to]
