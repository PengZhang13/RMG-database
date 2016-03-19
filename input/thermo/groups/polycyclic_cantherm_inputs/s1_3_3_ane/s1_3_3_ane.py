#!/usr/bin/env python
# -*- coding: utf-8 -*-

atoms = {
    'C': 5,
    'H': 8,
}

bonds = {
    'C-C': 6, 
    'C-H': 8,
}

linear = False

externalSymmetry = 1

spinMultiplicity = 1

opticalIsomers = 1

energy = {
    'M06-2X': GaussianLog('s1_3_3_ane.log'),
}

geometry = GaussianLog('s1_3_3_ane.log')

frequencies = GaussianLog('s1_3_3_ane.log')

rotors = []
