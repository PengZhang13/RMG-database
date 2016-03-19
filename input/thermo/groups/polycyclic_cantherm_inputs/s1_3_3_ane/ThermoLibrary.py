#!/usr/bin/env python
# encoding: utf-8

name = "Thermo Estimation Library"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "s1_3_3_ane",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {5,S}
3  C u0 p0 c0 {1,S} {2,S} {8,S} {9,S}
4  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
5  C u0 p0 c0 {2,S} {4,S} {12,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([88.2453,117.472,143.266,164.477,197.67,221.935,257.136],'J/(mol*K)'),
        H298 = (171.008,'kJ/mol'),
        S298 = (292.835,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

