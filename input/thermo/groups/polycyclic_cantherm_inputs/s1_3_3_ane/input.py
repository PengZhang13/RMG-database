#!/usr/bin/env python
# encoding: utf-8

modelChemistry = "M06-2X"
frequencyScaleFactor = 0.99
useHinderedRotors = False
useBondCorrections = False

species('s1_3_3_ane', 'C1C2(C1)CC2', 's1_3_3_ane.py')

statmech('s1_3_3_ane')
thermo('s1_3_3_ane', 'NASA')
