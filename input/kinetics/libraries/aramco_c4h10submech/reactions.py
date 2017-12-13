#!/usr/bin/env python
# encoding: utf-8

name = "Aramco2"
shortDesc = u"Aramco 2.0"
longDesc = u"""
Developed by NUI Galway. 
Released date: February 2016
http://www.nuigalway.ie/c3/aramco2/frontmatter.html

Reference paper:
Y. Li, C-W. Zhou, K.P. Somers, K. Zhang, H.J. Curran 
The Oxidation of 2-Butene: A High Pressure Ignition Delay, Kinetic Modeling Study and Reactivity Comparison with Isobutene and 1-Butene
Proc. Combust. Inst. (2017) submitted
C-W. Zhou, Y. Li, E. O'Connor, K.P. Somers, S. Thion et al.
A Comprehensive experimental and modeling study of isobutene oxidation
Combust. Flame (2016) accepted
U. Burke, W.K. Metcalfe, S.M. Burke, K.A. Heufer, P. Dagaut, H.J. Curran
A Detailed Chemical Kinetic Modeling, Ignition Delay time and Jet-Stirred Reactor Study of Methanol Oxidation
Combust. Flame (2016) 165 125–136
S.M. Burke, U. Burke, O. Mathieu, I. Osorio et al.
An experimental and modeling study of propene oxidation. Part 2: Ignition delay time and flame speed measurements
Combust. Flame (2015) 162(2) 296–314
S.M. Burke, W.K. Metcalfe, O. Herbinet et al.
An experimental and modeling study of propene oxidation. Part 1: Speciation measurements in jet-stirred and flow reactors
Combust. Flame (2014) 161(11) 2765–2784
W.K. Metcalfe, S.M. Burke, S.S. Ahmed, H.J. Curran
A hierarchical and comparative kinetic modeling study of C1–C2 hydrocarbon and oxygenated fuels
Int. J. Chem. Kinet. (2013) 45(10) 638–675
A. Kéromnès, W.K. Metcalfe, K.A. Heufer et al.
An Experimental and Detailed Chemical Kinetic Modelling Study of Hydrogen and Syngas Mixtures at Elevated Pressures
Combustion and Flame (2013) 160 995–1011

The species in excited state, together with corresponding reactions have been deleted.
The reactions with 4 or more products have also been deleted.
Peng Zhang
Date: Mar. 20, 2016
"""

entry(
    index = 872,
    label = "C4H10 <=> C2H5 + C2H5",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(1.355e+37, 's^-1'), n=-6.036, Ea=(92929, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(4.72e+18, 'cm^3/(mol*s)'), n=0, Ea=(49578, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.07998,
        T3 = (1e-20, 'K'),
        T1 = (32430, 'K'),
        T2 = (4858, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 873,
    label = "C4H10 <=> NC3H7 + CH3",
    degeneracy = 1,
    kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(6.6e+52, 's^-1'), n=-10.626, Ea=(100330, 'cal/mol'), T0=(1, 'K')),
        arrheniusLow = Arrhenius(A=(5.34e+17, 'cm^3/(mol*s)'), n=0, Ea=(42959, 'cal/mol'), T0=(1, 'K')),
        alpha = 0.09502,
        T3 = (1e-20, 'K'),
        T1 = (5348, 'K'),
        T2 = (4326, 'K'),
        efficiencies = {},
    ),
)

entry(
    index = 874,
    label = "C4H10 <=> PC4H9 + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(4.45e+90, 's^-1'), n=-21.91, Ea=(140564, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.63e+76, 's^-1'), n=-17.64, Ea=(134669, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.94e+58, 's^-1'), n=-12.32, Ea=(125435, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.8e+40, 's^-1'), n=-7.06, Ea=(115302, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.49e+27, 's^-1'), n=-3.15, Ea=(107323, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 875,
    label = "C4H10 <=> SC4H9 + H",
    degeneracy = 1,
    kinetics = PDepArrhenius(
        pressures = ([0.01, 0.1, 1, 10, 100], 'atm'),
        arrhenius = [
            Arrhenius(A=(3.1e+88, 's^-1'), n=-21.24, Ea=(136355, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.34e+73, 's^-1'), n=-16.76, Ea=(129590, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(7.39e+55, 's^-1'), n=-11.52, Ea=(120199, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(8.52e+38, 's^-1'), n=-6.58, Ea=(110556, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(5.4e+26, 's^-1'), n=-3.05, Ea=(103313, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 876,
    label = "C4H10 + H <=> PC4H9 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(349000, 'cm^3/(mol*s)'), n=2.69, Ea=(6450, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 877,
    label = "C4H10 + O2 <=> PC4H9 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+13, 'cm^3/(mol*s)'), n=0, Ea=(52340, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 878,
    label = "C4H10 + O <=> PC4H9 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.13e+14, 'cm^3/(mol*s)'), n=0, Ea=(7850, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 879,
    label = "C4H10 + OH <=> PC4H9 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.054e+10, 'cm^3/(mol*s)'),
        n = 0.97,
        Ea = (1586, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 880,
    label = "C4H10 + HO2 <=> PC4H9 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(40.8, 'cm^3/(mol*s)'), n=3.59, Ea=(17160, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 881,
    label = "C4H10 + CH3 <=> PC4H9 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.904, 'cm^3/(mol*s)'), n=3.65, Ea=(7154, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 882,
    label = "C4H10 + CH3O <=> PC4H9 + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0, Ea=(7000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 883,
    label = "C4H10 + CH3O2 <=> PC4H9 + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.386, 'cm^3/(mol*s)'), n=3.97, Ea=(18280, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 884,
    label = "C4H10 + O2CHO <=> PC4H9 + HO2CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.68e+13, 'cm^3/(mol*s)'), n=0, Ea=(20440, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 885,
    label = "C4H10 + C2H5 <=> PC4H9 + C2H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.58e+11, 'cm^3/(mol*s)'), n=0, Ea=(12300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 886,
    label = "C4H10 + C2H3 <=> PC4H9 + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+12, 'cm^3/(mol*s)'), n=0, Ea=(18000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 887,
    label = "C4H10 + C2H5O <=> PC4H9 + C2H5OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3e+11, 'cm^3/(mol*s)'), n=0, Ea=(7000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 888,
    label = "C4H10 + C2H5O2 <=> PC4H9 + C2H5O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(40.8, 'cm^3/(mol*s)'), n=3.59, Ea=(17160, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 889,
    label = "C4H10 + CH3CO3 <=> PC4H9 + CH3CO3H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 890,
    label = "C4H10 + C3H5-A <=> PC4H9 + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7.94e+11, 'cm^3/(mol*s)'), n=0, Ea=(20500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 891,
    label = "C4H10 + NC3H7O2 <=> PC4H9 + NC3H7O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 892,
    label = "C4H10 + IC3H7O2 <=> PC4H9 + IC3H7O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 893,
    label = "C4H10 + PC4H9 <=> SC4H9 + C4H10",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(10400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 894,
    label = "C4H10 + PC4H9O2 <=> PC4H9 + PC4H9O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 895,
    label = "C4H10 + SC4H9O2 <=> PC4H9 + SC4H9O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 896,
    label = "C4H10 + IC4H9O2 <=> PC4H9 + IC4H9O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 897,
    label = "C4H10 + TC4H9O2 <=> PC4H9 + TC4H9O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 898,
    label = "C4H10 + H <=> SC4H9 + H2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.6e+06, 'cm^3/(mol*s)'), n=2.4, Ea=(4471, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 899,
    label = "C4H10 + O2 <=> SC4H9 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+13, 'cm^3/(mol*s)'), n=0, Ea=(49800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 900,
    label = "C4H10 + O <=> SC4H9 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.62e+13, 'cm^3/(mol*s)'), n=0, Ea=(5200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 901,
    label = "C4H10 + OH <=> SC4H9 + H2O",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.34e+07, 'cm^3/(mol*s)'),
        n = 1.61,
        Ea = (-35, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 902,
    label = "C4H10 + HO2 <=> SC4H9 + H2O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(126.4, 'cm^3/(mol*s)'), n=3.37, Ea=(13720, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 903,
    label = "C4H10 + CH3 <=> SC4H9 + CH4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.02, 'cm^3/(mol*s)'), n=3.46, Ea=(5481, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 904,
    label = "C4H10 + CH3O <=> SC4H9 + CH3OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+11, 'cm^3/(mol*s)'), n=0, Ea=(7000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 905,
    label = "C4H10 + CH3O2 <=> SC4H9 + CH3O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(20.37, 'cm^3/(mol*s)'), n=3.58, Ea=(14810, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 906,
    label = "C4H10 + O2CHO <=> SC4H9 + HO2CHO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.12e+13, 'cm^3/(mol*s)'), n=0, Ea=(17690, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 907,
    label = "C4H10 + C2H5 <=> SC4H9 + C2H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+11, 'cm^3/(mol*s)'), n=0, Ea=(10400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 908,
    label = "C4H10 + C2H3 <=> SC4H9 + C2H4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(8e+11, 'cm^3/(mol*s)'), n=0, Ea=(16800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 909,
    label = "C4H10 + C2H5O <=> SC4H9 + C2H5OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6e+11, 'cm^3/(mol*s)'), n=0, Ea=(7000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 910,
    label = "C4H10 + C2H5O2 <=> SC4H9 + C2H5O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(126.4, 'cm^3/(mol*s)'), n=3.37, Ea=(13720, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 911,
    label = "C4H10 + CH3CO3 <=> SC4H9 + CH3CO3H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.12e+13, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 912,
    label = "C4H10 + C3H5-A <=> SC4H9 + C3H6",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.16e+11, 'cm^3/(mol*s)'), n=0, Ea=(16400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 913,
    label = "C4H10 + NC3H7O2 <=> SC4H9 + NC3H7O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.12e+13, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 914,
    label = "C4H10 + IC3H7O2 <=> SC4H9 + IC3H7O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.12e+13, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 915,
    label = "C4H10 + PC4H9O2 <=> SC4H9 + PC4H9O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.12e+13, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 916,
    label = "C4H10 + SC4H9O2 <=> SC4H9 + SC4H9O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.12e+13, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 917,
    label = "C4H10 + IC4H9O2 <=> SC4H9 + IC4H9O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.12e+13, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 918,
    label = "C4H10 + TC4H9O2 <=> SC4H9 + TC4H9O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.12e+13, 'cm^3/(mol*s)'), n=0, Ea=(17700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 919,
    label = "PC4H9 + HO2 <=> PC4H9O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 920,
    label = "CH3O2 + PC4H9 <=> CH3O + PC4H9O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 921,
    label = "SC4H9 + HO2 <=> SC4H9O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 922,
    label = "SC4H9 + CH3O2 <=> CH3O + SC4H9O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 923,
    label = "C2H5 + CH3CHO <=> SC4H9O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.33e+10, 'cm^3/(mol*s)'), n=0, Ea=(6397, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 924,
    label = "PC4H9 + O2 <=> C4H8-1 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.837, 'cm^3/(mol*s)'), n=3.59, Ea=(11960, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 925,
    label = "PC4H9 + O2 <=> PC4H9O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.865e+16, 'cm^3/(mol*s)'),
        n = -1.627,
        Ea = (198.7, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 926,
    label = "SC4H9 + O2 <=> C4H8-1 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(0.535, 'cm^3/(mol*s)'), n=3.71, Ea=(9322, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 927,
    label = "SC4H9 + O2 <=> C4H8-2 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.07, 'cm^3/(mol*s)'), n=3.71, Ea=(9322, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 928,
    label = "SC4H9 + O2 <=> SC4H9O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.487e+14, 'cm^3/(mol*s)'),
        n = -0.816,
        Ea = (-536.5, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 929,
    label = "PC4H9O2 + H2 <=> PC4H9O2H + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+13, 'cm^3/(mol*s)'), n=0, Ea=(26030, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 930,
    label = "PC4H9O2 + HO2 <=> PC4H9O2H + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 931,
    label = "PC4H9O2 + H2O2 <=> PC4H9O2H + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 932,
    label = "PC4H9O2 + CH4 <=> PC4H9O2H + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.12e+13, 'cm^3/(mol*s)'), n=0, Ea=(24640, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 933,
    label = "PC4H9O2 + CH3OH <=> PC4H9O2H + CH2OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.3e+12, 'cm^3/(mol*s)'), n=0, Ea=(19360, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 934,
    label = "PC4H9O2 + CH2O <=> PC4H9O2H + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 935,
    label = "PC4H9O2 + C2H6 <=> PC4H9O2H + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 936,
    label = "PC4H9O2 + CH3CHO <=> PC4H9O2H + CH3CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 937,
    label = "PC4H9O2 + C2H4 <=> PC4H9O2H + C2H3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.13e+13, 'cm^3/(mol*s)'), n=0, Ea=(30430, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 938,
    label = "PC4H9O2 + C3H6 <=> PC4H9O2H + C3H5-A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0535, 'cm^3/(mol*s)'),
        n = 4.207,
        Ea = (13288.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 939,
    label = "PC4H9O2 + C2H5CHO <=> PC4H9O2H + C2H5CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(9500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 940,
    label = "PC4H9O2 + C2H3CHO <=> PC4H9O2H + C2H3CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 941,
    label = "PC4H9O2 + C3H8 <=> PC4H9O2H + NC3H7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 942,
    label = "PC4H9O2 + C3H8 <=> PC4H9O2H + IC3H7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(17000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 943,
    label = "PC4H9O2 + CH3 <=> PC4H9O + CH3O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 944,
    label = "PC4H9O2 + C2H5 <=> PC4H9O + C2H5O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 945,
    label = "PC4H9O2 + IC3H7 <=> PC4H9O + IC3H7O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 946,
    label = "PC4H9O2 + NC3H7 <=> PC4H9O + NC3H7O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 947,
    label = "PC4H9O2 + C3H5-A <=> PC4H9O + C3H5O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 948,
    label = "PC4H9O2 + PC4H9 <=> PC4H9O + PC4H9O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 949,
    label = "PC4H9O2 + SC4H9 <=> PC4H9O + SC4H9O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 950,
    label = "PC4H9O2 + C4H71-3 <=> PC4H9O + C4H71-O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 951,
    label = "PC4H9O2H <=> PC4H9O + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.5e+16, 's^-1'), n=0, Ea=(42500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 952,
    label = "PC4H9O2 + CH3O2 => PC4H9O + CH3O + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 953,
    label = "PC4H9O2 + CH3CO3 => PC4H9O + CH3CO2 + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 954,
    label = "PC4H9O2 + C2H5O2 => PC4H9O + C2H5O + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 955,
    label = "PC4H9O2 + NC3H7O2 => PC4H9O + NC3H7O + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 956,
    label = "PC4H9O2 + IC3H7O2 => PC4H9O + IC3H7O + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 957,
    label = "PC4H9O2 + PC4H9O2 => PC4H9O + PC4H9O + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 958,
    label = "PC4H9O2 + SC4H9O2 => PC4H9O + SC4H9O + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 959,
    label = "PC4H9O2 <=> C4H8OOH1-2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.009e+08, 's^-1'), n=1.1, Ea=(30100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 960,
    label = "PC4H9O2 <=> C4H8OOH1-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.36e+07, 's^-1'), n=1.3, Ea=(18200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 961,
    label = "PC4H9O2 <=> C4H8OOH1-4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.233e+06, 's^-1'), n=1.5, Ea=(20000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 962,
    label = "PC4H9O2 <=> C4H8-1 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.258e+08, 's^-1'), n=1.38, Ea=(28900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 963,
    label = "IC3H7O2 + PC4H9 <=> IC3H7O + PC4H9O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 964,
    label = "NC3H7O2 + PC4H9 <=> NC3H7O + PC4H9O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 965,
    label = "SC4H9O2 + PC4H9 <=> SC4H9O + PC4H9O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 966,
    label = "IC3H7O2 + SC4H9 <=> IC3H7O + SC4H9O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 967,
    label = "NC3H7O2 + SC4H9 <=> NC3H7O + SC4H9O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 968,
    label = "SC4H9O2 + H2 <=> SC4H9O2H + H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.01e+13, 'cm^3/(mol*s)'), n=0, Ea=(26030, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 969,
    label = "SC4H9O2 + HO2 <=> SC4H9O2H + O2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.75e+10, 'cm^3/(mol*s)'), n=0, Ea=(-3275, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 970,
    label = "SC4H9O2 + CH2O <=> SC4H9O2H + HCO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.6e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 971,
    label = "SC4H9O2 + CH3CHO <=> SC4H9O2H + CH3CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 972,
    label = "SC4H9O2 + C2H6 <=> SC4H9O2H + C2H5",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 973,
    label = "SC4H9O2 + C2H5CHO <=> SC4H9O2H + C2H5CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(9500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 974,
    label = "SC4H9O2 + C3H6 <=> SC4H9O2H + C3H5-A",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0535, 'cm^3/(mol*s)'),
        n = 4.207,
        Ea = (13288.1, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 975,
    label = "SC4H9O2 + C2H4 <=> SC4H9O2H + C2H3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.13e+13, 'cm^3/(mol*s)'), n=0, Ea=(30430, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 976,
    label = "SC4H9O2 + CH3OH <=> SC4H9O2H + CH2OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.3e+12, 'cm^3/(mol*s)'), n=0, Ea=(19360, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 977,
    label = "SC4H9O2 + C2H3CHO <=> SC4H9O2H + C2H3CO",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.8e+12, 'cm^3/(mol*s)'), n=0, Ea=(13600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 978,
    label = "SC4H9O2 + CH4 <=> SC4H9O2H + CH3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.12e+13, 'cm^3/(mol*s)'), n=0, Ea=(24640, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 979,
    label = "SC4H9O2 + H2O2 <=> SC4H9O2H + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.4e+12, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 980,
    label = "SC4H9O2 + C3H8 <=> SC4H9O2H + NC3H7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.7e+13, 'cm^3/(mol*s)'), n=0, Ea=(20460, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 981,
    label = "SC4H9O2 + C3H8 <=> SC4H9O2H + IC3H7",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+12, 'cm^3/(mol*s)'), n=0, Ea=(17000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 982,
    label = "SC4H9O2 + CH3O2 => SC4H9O + CH3O + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 983,
    label = "SC4H9O2 + CH3CO3 => SC4H9O + CH3CO2 + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 984,
    label = "SC4H9O2 + NC3H7O2 => SC4H9O + NC3H7O + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 985,
    label = "SC4H9O2 + IC3H7O2 => SC4H9O + IC3H7O + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 986,
    label = "SC4H9O2 + SC4H9O2 => SC4H9O + SC4H9O + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 987,
    label = "SC4H9O2 + C2H5O2 => SC4H9O + C2H5O + O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(
        A = (1.4e+16, 'cm^3/(mol*s)'),
        n = -1.61,
        Ea = (1860, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 988,
    label = "SC4H9O2 + CH3 <=> SC4H9O + CH3O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 989,
    label = "SC4H9O2 + C2H5 <=> SC4H9O + C2H5O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 990,
    label = "SC4H9O2 + IC3H7 <=> SC4H9O + IC3H7O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 991,
    label = "SC4H9O2 + NC3H7 <=> SC4H9O + NC3H7O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 992,
    label = "SC4H9O2 + SC4H9 <=> SC4H9O + SC4H9O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 993,
    label = "SC4H9O2 + C3H5-A <=> SC4H9O + C3H5O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 994,
    label = "SC4H9O2 + C4H71-3 <=> SC4H9O + C4H71-O",
    degeneracy = 1,
    kinetics = Arrhenius(A=(7e+12, 'cm^3/(mol*s)'), n=0, Ea=(-1000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 995,
    label = "SC4H9O + OH <=> SC4H9O2H",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1e+15, 'cm^3/(mol*s)'), n=-0.8, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 996,
    label = "SC4H9O2 <=> C4H8OOH2-1",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.458e+09, 's^-1'), n=1.1, Ea=(33500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 997,
    label = "SC4H9O2 <=> C4H8OOH2-3",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.716e+09, 's^-1'), n=0.9, Ea=(29500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 998,
    label = "SC4H9O2 <=> C4H8OOH2-4",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.439e+07, 's^-1'), n=1.4, Ea=(20800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 999,
    label = "SC4H9O2 <=> C4H8-1 + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.13e+09, 's^-1'), n=1, Ea=(30400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1000,
    label = "C4H8OOH1-2 <=> C4H8O1-2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.71e+09, 's^-1'), n=1.06, Ea=(10900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1001,
    label = "C4H8OOH1-3 <=> C4H8O1-3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.59e+09, 's^-1'), n=0.69, Ea=(16000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1002,
    label = "C4H8OOH1-4 <=> C4H8O1-4 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.72e+08, 's^-1'), n=0.76, Ea=(11100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1003,
    label = "C4H8OOH2-4 <=> C4H8O1-3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.44e+09, 's^-1'), n=0.78, Ea=(18000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1004,
    label = "C4H8O1-2 + H => CH2O + C3H5-A + H2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1005,
    label = "C4H8O1-2 + O => CH2O + C3H5-A + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1006,
    label = "C4H8O1-2 + OH => CH2O + C3H5-A + H2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1007,
    label = "C4H8O1-2 + HO2 => CH2O + C3H5-A + H2O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(15000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1008,
    label = "C4H8O1-2 + CH3 => CH2O + C3H5-A + CH4",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1009,
    label = "C4H8O1-2 + CH3O2 => CH2O + C3H5-A + CH3O2H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(19000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1010,
    label = "C4H8O1-3 + H => CH2O + C3H5-A + H2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1011,
    label = "C4H8O1-3 + O => CH2O + C3H5-A + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1012,
    label = "C4H8O1-3 + OH => CH2O + C3H5-A + H2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1013,
    label = "C4H8O1-3 + HO2 => CH2O + C3H5-A + H2O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(15000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1014,
    label = "C4H8O1-3 + CH3 => CH2O + C3H5-A + CH4",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1015,
    label = "C4H8O1-3 + CH3O2 => CH2O + C3H5-A + CH3O2H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(19000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1016,
    label = "C4H8O1-4 + H => CH2O + C3H5-A + H2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1017,
    label = "C4H8O1-4 + O => CH2O + C3H5-A + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1018,
    label = "C4H8O1-4 + OH => CH2O + C3H5-A + H2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1019,
    label = "C4H8O1-4 + HO2 => CH2O + C3H5-A + H2O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(15000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1020,
    label = "C4H8O1-4 + CH3 => CH2O + C3H5-A + CH4",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1021,
    label = "C4H8O1-4 + CH3O2 => CH2O + C3H5-A + CH3O2H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(19000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1022,
    label = "C4H8O2-3 + H => CH2O + C3H5-A + H2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1023,
    label = "C4H8O2-3 + OH => CH2O + C3H5-A + H2O",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1024,
    label = "C4H8O2-3 + O => CH2O + C3H5-A + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(5e+12, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1025,
    label = "C4H8O2-3 + HO2 => CH2O + C3H5-A + H2O2",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(15000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1026,
    label = "C4H8O2-3 + CH3O2 => CH2O + C3H5-A + CH3O2H",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(19000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1027,
    label = "C4H8O2-3 + CH3 => CH2O + C3H5-A + CH4",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(2e+11, 'cm^3/(mol*s)'), n=0, Ea=(10000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1028,
    label = "C4H8OOH1-3 => OH + CH2O + C3H6",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.23e+09, 's^-1'), n=1.3, Ea=(24900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1029,
    label = "C4H8OOH2-4 => OH + CH3CHO + C2H4",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(3.08e+08, 's^-1'), n=1.5, Ea=(23500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1030,
    label = "C4H8OOH1-2 + O2 <=> C4H8OOH1-2O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.744e+14, 'cm^3/(mol*s)'),
        n = -0.816,
        Ea = (-536.5, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1031,
    label = "C4H8OOH1-3 + O2 <=> C4H8OOH1-3O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.744e+14, 'cm^3/(mol*s)'),
        n = -0.816,
        Ea = (-536.5, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1032,
    label = "C4H8OOH1-4 + O2 <=> C4H8OOH1-4O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.433e+16, 'cm^3/(mol*s)'),
        n = -1.627,
        Ea = (198.7, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1033,
    label = "C4H8OOH2-1 + O2 <=> C4H8OOH2-1O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.433e+16, 'cm^3/(mol*s)'),
        n = -1.627,
        Ea = (198.7, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1034,
    label = "C4H8OOH2-3 + O2 <=> C4H8OOH2-3O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.744e+14, 'cm^3/(mol*s)'),
        n = -0.816,
        Ea = (-536.5, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1035,
    label = "C4H8OOH2-4 + O2 <=> C4H8OOH2-4O2",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.433e+16, 'cm^3/(mol*s)'),
        n = -1.627,
        Ea = (198.7, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 1036,
    label = "C4H8OOH1-2O2 <=> C4H72-1OOH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.54e+10, 's^-1'), n=0.804, Ea=(30098.5, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1037,
    label = "C4H8OOH1-3O2 <=> C4H71-4OOH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.13e+09, 's^-1'), n=1, Ea=(30400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1038,
    label = "C4H8OOH1-3O2 <=> C4H72-1OOH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.54e+10, 's^-1'), n=0.804, Ea=(30098.5, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1039,
    label = "C4H8OOH1-4O2 <=> C4H71-4OOH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.44e+07, 's^-1'), n=1.38, Ea=(28900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1040,
    label = "C4H8OOH2-3O2 <=> C4H71-3OOH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(5.13e+09, 's^-1'), n=1, Ea=(30400, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1041,
    label = "C4H8OOH2-4O2 <=> C4H71-3OOH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.44e+07, 's^-1'), n=1.38, Ea=(28900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1042,
    label = "C4H8OOH1-2O2 <=> C4H71-3,4OOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.44e+07, 's^-1'), n=1.4, Ea=(20800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1043,
    label = "C4H8OOH1-2O2 <=> C4H72-3,4OOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.72e+09, 's^-1'), n=0.9, Ea=(29500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1044,
    label = "C4H8OOH1-2O2 <=> NC4KET12 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.44e+07, 's^-1'), n=1.6, Ea=(27900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1045,
    label = "C4H8OOH1-3O2 <=> C4H71-2,4OOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.46e+09, 's^-1'), n=1.1, Ea=(33500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1046,
    label = "C4H8OOH1-3O2 <=> C4H72-1,3OOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.72e+09, 's^-1'), n=0.9, Ea=(29500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1047,
    label = "C4H8OOH1-3O2 <=> NC4KET13 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(10900, 's^-1'), n=2.4, Ea=(19900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1048,
    label = "C4H8OOH1-4O2 <=> C4H72-1,4OOH",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(1.36e+07, 's^-1'), n=1.3, Ea=(18200, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(4.01e+08, 's^-1'), n=1.1, Ea=(30100, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 1049,
    label = "C4H8OOH1-4O2 <=> NC4KET14 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4800, 's^-1'), n=1.7, Ea=(16600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1050,
    label = "C4H8OOH2-1O2 <=> C4H72-3,4OOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.72e+09, 's^-1'), n=0.9, Ea=(29500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1051,
    label = "C4H8OOH2-1O2 <=> C4H71-3,4OOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.23e+06, 's^-1'), n=1.5, Ea=(20000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1052,
    label = "C4H8OOH2-1O2 <=> NC4KET21 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.76e+08, 's^-1'), n=1.2, Ea=(25700, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1053,
    label = "C4H8OOH2-3O2 <=> C4H71-2,3OOH",
    degeneracy = 1,
    kinetics = MultiArrhenius(
        arrhenius = [
            Arrhenius(A=(1.46e+09, 's^-1'), n=1.1, Ea=(33500, 'cal/mol'), T0=(1, 'K')),
            Arrhenius(A=(1.44e+07, 's^-1'), n=1.4, Ea=(20800, 'cal/mol'), T0=(1, 'K')),
        ],
    ),
)

entry(
    index = 1054,
    label = "C4H8OOH2-3O2 <=> NC4KET23 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.75e+06, 's^-1'), n=1.7, Ea=(26000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1055,
    label = "C4H8OOH2-4O2 <=> C4H71-2,4OOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.23e+06, 's^-1'), n=1.5, Ea=(20000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1056,
    label = "C4H8OOH2-4O2 <=> C4H72-1,3OOH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4.01e+08, 's^-1'), n=1.1, Ea=(30100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1057,
    label = "C4H8OOH2-4O2 <=> NC4KET24 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(57.9, 's^-1'), n=2.9, Ea=(17000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1058,
    label = "C4H71-3,4OOH <=> C4H7O1-3OOH-4 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.44e+09, 's^-1'), n=0.78, Ea=(18000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1059,
    label = "C4H71-3,4OOH <=> C4H7O1-4OOH-2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.72e+09, 's^-1'), n=0.76, Ea=(11100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1060,
    label = "C4H72-3,4OOH <=> C4H7O2-3OOH-1 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.99e+09, 's^-1'), n=0.815, Ea=(9788.3, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1061,
    label = "C4H72-3,4OOH <=> C4H7O1-3OOH-2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.59e+09, 's^-1'), n=0.69, Ea=(16000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1062,
    label = "C4H71-2,4OOH <=> C4H7O1-2OOH-4 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.35e+10, 's^-1'), n=0.68, Ea=(10800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1063,
    label = "C4H71-2,4OOH <=> C4H7O1-4OOH-2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.72e+09, 's^-1'), n=0.76, Ea=(11100, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1064,
    label = "C4H72-1,3OOH <=> C4H7O1-2OOH-3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.71e+09, 's^-1'), n=1.06, Ea=(10900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1065,
    label = "C4H72-1,3OOH <=> C4H7O2-3OOH-1 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.99e+09, 's^-1'), n=0.815, Ea=(9788.3, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1066,
    label = "C4H72-1,4OOH <=> C4H7O1-2OOH-4 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(1.71e+09, 's^-1'), n=1.06, Ea=(10900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1067,
    label = "C4H72-1,4OOH <=> C4H7O1-3OOH-4 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.59e+09, 's^-1'), n=0.69, Ea=(16000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1068,
    label = "C4H71-2,3OOH <=> C4H7O1-2OOH-3 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.35e+10, 's^-1'), n=0.68, Ea=(10800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1069,
    label = "C4H71-2,3OOH <=> C4H7O1-3OOH-2 + OH",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.44e+09, 's^-1'), n=0.78, Ea=(18000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1070,
    label = "C4H71-3,4OOH => C2H4 + OH + HO2CH2CHO",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.23e+09, 's^-1'), n=1.3, Ea=(24900, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1071,
    label = "C4H72-3,4OOH <=> C4H72-1OOH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.568e+11, 's^-1'), n=0.538, Ea=(15324.7, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1072,
    label = "C4H71-2,4OOH <=> C4H71-4OOH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.67e+11, 's^-1'), n=0.5, Ea=(15800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1073,
    label = "C4H72-1,3OOH <=> C4H72-1OOH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.568e+11, 's^-1'), n=0.538, Ea=(15324.7, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1074,
    label = "C4H72-1,3OOH <=> C4H71-3OOH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.03e+09, 's^-1'), n=0.95, Ea=(15200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1075,
    label = "C4H72-1,4OOH <=> C4H71-4OOH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.568e+11, 's^-1'), n=0.538, Ea=(15324.7, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1076,
    label = "C4H71-2,3OOH <=> C4H71-3OOH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(6.03e+09, 's^-1'), n=0.95, Ea=(15200, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1077,
    label = "C4H72-1,4OOH <=> C4H72-1OOH + HO2",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2.67e+11, 's^-1'), n=0.5, Ea=(15800, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1078,
    label = "C4H72-1OOH => CH2O + C3H5-S + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.5e+16, 's^-1'), n=0, Ea=(42000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1079,
    label = "C4H71-3OOH => C2H3CHO + CH3 + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.05e+16, 's^-1'), n=0, Ea=(41600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1080,
    label = "C4H71-3OOH => CH3CHO + C2H3 + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.05e+16, 's^-1'), n=0, Ea=(41600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1081,
    label = "NC4KET12 => C2H5CHO + HCO + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.05e+16, 's^-1'), n=0, Ea=(41600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1082,
    label = "NC4KET13 => CH3CHO + CH2CHO + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.05e+16, 's^-1'), n=0, Ea=(43000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1083,
    label = "NC4KET14 => CH2CH2CHO + CH2O + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.5e+16, 's^-1'), n=0, Ea=(42000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1084,
    label = "NC4KET21 => CH2O + C2H5CO + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.5e+16, 's^-1'), n=0, Ea=(42000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1085,
    label = "NC4KET23 => CH3CHO + CH3CO + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.05e+16, 's^-1'), n=0, Ea=(41600, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1086,
    label = "NC4KET24 => CH2O + CH3COCH2 + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.5e+16, 's^-1'), n=0, Ea=(43000, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 1087,
    label = "HO2CH2CHO => CH2O + HCO + OH",
    degeneracy = 1,
    reversible = False,
    kinetics = Arrhenius(A=(1.5e+16, 's^-1'), n=0, Ea=(42000, 'cal/mol'), T0=(1, 'K')),
)

