#!/usr/bin/env python
# encoding: utf-8

name = "Overal Thermo Estimation Library"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "s1_3_3_ane",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {2,S} {8,S} {9,S}
4  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
5  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([88.2452,117.472,143.266,164.477,197.67,221.935,257.136],'J/(mol*K)'),
        H298 = (171.008,'kJ/mol'),
        S298 = (281.308,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "s1_3_3_ene",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3  C u0 p0 c0 {1,S} {2,S} {8,S} {9,S}
4  C u0 p0 c0 {1,S} {5,D} {10,S}
5  C u0 p0 c0 {1,S} {4,D} {11,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([84.5347,109.939,130.744,147.325,173.431,192.23,218.909],'J/(mol*K)'),
        H298 = (400.026,'kJ/mol'),
        S298 = (282.985,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "s1_3_4_ane",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {5,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {4,S} {15,S} {16,S}
6  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
7  H u0 p0 c0 {6,S}
8  H u0 p0 c0 {6,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([105.702,141.663,173.875,200.936,243.63,274.792,319.722],'J/(mol*K)'),
        H298 = (132.69,'kJ/mol'),
        S298 = (315.961,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "s1_3_4_ene",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {3,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {2,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
5  C u0 p0 c0 {1,S} {6,D} {14,S}
6  C u0 p0 c0 {4,S} {5,D} {13,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([98.6805,131.114,159.278,182.239,218.073,243.988,280.818],'J/(mol*K)'),
        H298 = (268.837,'kJ/mol'),
        S298 = (306.894,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "s1_3_5_ane",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {7,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {6,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {5,S} {16,S} {17,S}
5  C u0 p0 c0 {1,S} {4,S} {18,S} {19,S}
6  C u0 p0 c0 {3,S} {7,S} {8,S} {9,S}
7  C u0 p0 c0 {2,S} {6,S} {10,S} {11,S}
8  H u0 p0 c0 {6,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {7,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([121.742,164.955,203.762,236.602,288.701,326.734,381.53],'J/(mol*K)'),
        H298 = (33.9541,'kJ/mol'),
        S298 = (333.545,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "s1_3_5_ene_1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {5,S} {8,S} {9,S}
5  C u0 p0 c0 {4,S} {7,S} {14,S} {15,S}
6  C u0 p0 c0 {1,S} {7,D} {17,S}
7  C u0 p0 c0 {5,S} {6,D} {16,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([115.609,154.949,189.548,218.269,263.447,296.17,342.724],'J/(mol*K)'),
        H298 = (141.681,'kJ/mol'),
        S298 = (329.175,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "s1_3_5_ene_2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {7,S} {12,S} {13,S}
5  C u0 p0 c0 {1,S} {6,S} {14,S} {15,S}
6  C u0 p0 c0 {5,S} {7,D} {16,S}
7  C u0 p0 c0 {4,S} {6,D} {17,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([115.612,154.951,189.549,218.27,263.448,296.171,342.724],'J/(mol*K)'),
        H298 = (141.679,'kJ/mol'),
        S298 = (329.181,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "s1_3_5_diene_1_3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {7,D} {12,S}
5  C u0 p0 c0 {1,S} {6,D} {13,S}
6  C u0 p0 c0 {5,D} {7,S} {14,S}
7  C u0 p0 c0 {4,D} {6,S} {15,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([107.168,143.476,174.513,199.36,237.699,265.154,303.499],'J/(mol*K)'),
        H298 = (233.238,'kJ/mol'),
        S298 = (311.508,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "s1_3_6_ane",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {7,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {8,S} {15,S} {16,S}
4  C u0 p0 c0 {1,S} {5,S} {19,S} {20,S}
5  C u0 p0 c0 {1,S} {4,S} {21,S} {22,S}
6  C u0 p0 c0 {7,S} {8,S} {9,S} {10,S}
7  C u0 p0 c0 {2,S} {6,S} {11,S} {12,S}
8  C u0 p0 c0 {3,S} {6,S} {17,S} {18,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([139.674,190.314,235.378,273.598,334.599,379.196,443.623],'J/(mol*K)'),
        H298 = (-16.4111,'kJ/mol'),
        S298 = (347.025,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "s1_3_6_ene_1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {3,S} {15,S} {16,S}
5  C u0 p0 c0 {2,S} {6,S} {11,S} {12,S}
6  C u0 p0 c0 {5,S} {8,S} {17,S} {18,S}
7  C u0 p0 c0 {1,S} {8,D} {20,S}
8  C u0 p0 c0 {6,S} {7,D} {19,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([133.48,179.985,220.705,254.823,309.004,348.367,404.657],'J/(mol*K)'),
        H298 = (96.9745,'kJ/mol'),
        S298 = (344.422,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "s1_3_6_ene_2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {3,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {2,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
5  C u0 p0 c0 {1,S} {8,S} {15,S} {16,S}
6  C u0 p0 c0 {4,S} {7,S} {17,S} {18,S}
7  C u0 p0 c0 {6,S} {8,D} {19,S}
8  C u0 p0 c0 {5,S} {7,D} {20,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([133.478,179.985,220.707,254.825,309.007,348.369,404.659],'J/(mol*K)'),
        H298 = (96.9688,'kJ/mol'),
        S298 = (344.41,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "s1_3_6_diene_1_4",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {11,S} {12,S}
4  C u0 p0 c0 {7,S} {8,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {7,D} {16,S}
6  C u0 p0 c0 {1,S} {8,D} {17,S}
7  C u0 p0 c0 {4,S} {5,D} {15,S}
8  C u0 p0 c0 {4,S} {6,D} {18,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([126.731,169.339,205.879,235.938,283.322,317.478,365.691],'J/(mol*K)'),
        H298 = (203.173,'kJ/mol'),
        S298 = (334.324,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "s1_3_6_diene_1_3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {6,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {8,D} {15,S}
6  C u0 p0 c0 {4,S} {7,D} {16,S}
7  C u0 p0 c0 {6,D} {8,S} {17,S}
8  C u0 p0 c0 {5,D} {7,S} {18,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([127.008,169.8,206.437,236.487,283.785,317.843,365.84],'J/(mol*K)'),
        H298 = (208.862,'kJ/mol'),
        S298 = (339.565,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "s2_3_3_ane",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {6,S}
3  C u0 p0 c0 {1,S} {2,S} {7,S} {8,S}
4  C u0 p0 c0 {1,S} {2,S} {9,S} {10,S}
5  H u0 p0 c0 {1,S}
6  H u0 p0 c0 {2,S}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([64.8506,87.1395,107.638,124.602,149.955,168.374,194.965],'J/(mol*K)'),
        H298 = (208.028,'kJ/mol'),
        S298 = (258.858,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "s2_3_3_ene",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2 C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
3 C u0 p0 c0 {1,S} {2,S} {4,D}
4 C u0 p0 c0 {1,S} {3,D} {8,S}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {2,S}
8 H u0 p0 c0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([59.9733,77.5632,93.1186,105.558,124.18,137.578,156.465],'J/(mol*K)'),
        H298 = (476.31,'kJ/mol'),
        S298 = (261.664,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    label = "s2_3_4_ane",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {7,S}
3  C u0 p0 c0 {1,S} {2,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {5,S} {8,S} {9,S}
5  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([86.0788,114.241,139.983,161.801,195.995,221.059,257.427],'J/(mol*K)'),
        H298 = (471.342,'kJ/mol'),
        S298 = (287.702,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 17,
    label = "s2_3_4_ene_1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {3,S} {4,S} {7,S}
3  C u0 p0 c0 {1,S} {2,S} {8,S} {9,S}
4  C u0 p0 c0 {2,S} {5,D} {10,S}
5  C u0 p0 c0 {1,S} {4,D} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([74.8126,101.458,124.813,143.329,170.929,190.715,218.452],'J/(mol*K)'),
        H298 = (331.625,'kJ/mol'),
        S298 = (277.101,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
    label = "s2_3_5_ane",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {5,S} {8,S}
3  C u0 p0 c0 {1,S} {2,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
5  C u0 p0 c0 {2,S} {6,S} {15,S} {16,S}
6  C u0 p0 c0 {4,S} {5,S} {13,S} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([98.647,135.542,169.342,197.773,241.493,273.349,319.19],'J/(mol*K)'),
        H298 = (57.4545,'kJ/mol'),
        S298 = (305.966,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 19,
    label = "s2_3_5_ene_1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {5,S} {8,S}
3  C u0 p0 c0 {1,S} {2,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
5  C u0 p0 c0 {2,S} {6,D} {13,S}
6  C u0 p0 c0 {4,S} {5,D} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([90.8874,124.901,154.939,179.194,216.031,242.613,280.221],'J/(mol*K)'),
        H298 = (160.877,'kJ/mol'),
        S298 = (294.895,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 20,
    label = "s2_3_6_ane",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {5,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
5  C u0 p0 c0 {2,S} {7,S} {18,S} {19,S}
6  C u0 p0 c0 {4,S} {7,S} {14,S} {15,S}
7  C u0 p0 c0 {5,S} {6,S} {16,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([118.929,162.221,201.5,234.813,287.405,325.836,381.241],'J/(mol*K)'),
        H298 = (35.6763,'kJ/mol'),
        S298 = (332.512,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 21,
    label = "s2_3_6_ene_1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
5  C u0 p0 c0 {4,S} {7,S} {14,S} {15,S}
6  C u0 p0 c0 {2,S} {7,D} {16,S}
7  C u0 p0 c0 {5,S} {6,D} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([110.247,150.704,186.402,215.735,261.446,294.639,342.05],'J/(mol*K)'),
        H298 = (124.035,'kJ/mol'),
        S298 = (316.22,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 22,
    label = "s2_3_6_ene_2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {5,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
5  C u0 p0 c0 {2,S} {7,S} {14,S} {15,S}
6  C u0 p0 c0 {4,S} {7,D} {16,S}
7  C u0 p0 c0 {5,S} {6,D} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([110.326,151.125,186.891,216.17,261.915,295.111,342.469],'J/(mol*K)'),
        H298 = (241.607,'kJ/mol'),
        S298 = (309.59,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 23,
    label = "s2_3_6_diene_1_3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {5,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {6,D} {12,S}
5  C u0 p0 c0 {2,S} {7,D} {13,S}
6  C u0 p0 c0 {4,D} {7,S} {14,S}
7  C u0 p0 c0 {5,D} {6,S} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([103.06,140.044,171.723,196.996,235.966,263.935,303.117],'J/(mol*K)'),
        H298 = (213.347,'kJ/mol'),
        S298 = (309.627,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 24,
    label = "s2_4_4_ane",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {8,S}
3  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {3,S} {11,S} {12,S}
5  C u0 p0 c0 {1,S} {6,S} {13,S} {14,S}
6  C u0 p0 c0 {2,S} {5,S} {15,S} {16,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([97.7434,135.56,169.712,198.026,241.701,273.561,319.442],'J/(mol*K)'),
        H298 = (310.08,'kJ/mol'),
        S298 = (294.85,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 25,
    label = "s2_4_4_ene_1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {8,S}
3  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {3,S} {11,S} {12,S}
5  C u0 p0 c0 {1,S} {6,D} {13,S}
6  C u0 p0 c0 {2,S} {5,D} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([94.0391,125.994,154.358,177.839,214.62,241.415,279.882],'J/(mol*K)'),
        H298 = (125.521,'kJ/mol'),
        S298 = (296.964,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 26,
    label = "s2_4_5_ane",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {9,S}
3  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {3,S} {12,S} {13,S}
5  C u0 p0 c0 {1,S} {7,S} {14,S} {15,S}
6  C u0 p0 c0 {2,S} {7,S} {18,S} {19,S}
7  C u0 p0 c0 {5,S} {6,S} {16,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([115.933,159.877,200.023,233.998,287.042,325.772,381.519],'J/(mol*K)'),
        H298 = (114.955,'kJ/mol'),
        S298 = (318.718,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 27,
    label = "s2_4_5_ene_1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {9,S}
3  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
5  C u0 p0 c0 {1,S} {7,S} {14,S} {15,S}
6  C u0 p0 c0 {2,S} {7,D} {17,S}
7  C u0 p0 c0 {5,S} {6,D} {16,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([108.274,148.719,185.104,215.272,261.59,295.106,342.635],'J/(mol*K)'),
        H298 = (142.479,'kJ/mol'),
        S298 = (316.566,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 28,
    label = "s2_4_6_ane",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {10,S}
3  C u0 p0 c0 {2,S} {4,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {3,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {7,S} {15,S} {16,S}
6  C u0 p0 c0 {2,S} {8,S} {21,S} {22,S}
7  C u0 p0 c0 {5,S} {8,S} {17,S} {18,S}
8  C u0 p0 c0 {6,S} {7,S} {19,S} {20,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([134.265,185.392,231.682,270.907,332.931,378.271,443.624],'J/(mol*K)'),
        H298 = (2.33762,'kJ/mol'),
        S298 = (340.459,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 29,
    label = "s2_4_6_ene_1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {10,S}
3  C u0 p0 c0 {1,S} {4,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {3,S} {11,S} {12,S}
5  C u0 p0 c0 {1,S} {6,S} {15,S} {16,S}
6  C u0 p0 c0 {5,S} {8,S} {17,S} {18,S}
7  C u0 p0 c0 {2,S} {8,D} {20,S}
8  C u0 p0 c0 {6,S} {7,D} {19,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([127.601,174.65,216.723,251.939,307.228,347.388,404.649],'J/(mol*K)'),
        H298 = (107.088,'kJ/mol'),
        S298 = (336.565,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 30,
    label = "s2_4_6_ene_2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {10,S}
3  C u0 p0 c0 {2,S} {4,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {3,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {7,S} {15,S} {16,S}
6  C u0 p0 c0 {2,S} {8,S} {17,S} {18,S}
7  C u0 p0 c0 {5,S} {8,D} {19,S}
8  C u0 p0 c0 {6,S} {7,D} {20,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([128.049,174.692,216.535,251.745,307.187,347.438,404.75],'J/(mol*K)'),
        H298 = (121.905,'kJ/mol'),
        S298 = (343.77,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 31,
    label = "s3_5_5_ane",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {8,S}
2  C u0 p0 c0 {3,S} {4,S} {7,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {5,S} {10,S} {11,S}
5  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
6  C u0 p0 c0 {1,S} {7,S} {16,S} {17,S}
7  C u0 p0 c0 {2,S} {6,S} {18,S} {19,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([110.456,155.774,197.435,232.463,286.053,325.05,381.044],'J/(mol*K)'),
        H298 = (-27.5809,'kJ/mol'),
        S298 = (308.154,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 32,
    label = "s3_5_5_ene_1",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {3,S} {5,S} {6,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
5  C u0 p0 c0 {2,S} {4,S} {12,S} {13,S}
6  C u0 p0 c0 {2,S} {7,D} {16,S}
7  C u0 p0 c0 {1,S} {6,D} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([103.81,146.189,183.961,214.666,261.177,294.746,342.218],'J/(mol*K)'),
        H298 = (109.774,'kJ/mol'),
        S298 = (305.366,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 33,
    label = "s3_5_5_diene_1_4",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {8,S}
2  C u0 p0 c0 {3,S} {4,S} {7,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {5,D} {12,S}
5  C u0 p0 c0 {1,S} {4,D} {13,S}
6  C u0 p0 c0 {1,S} {7,D} {14,S}
7  C u0 p0 c0 {2,S} {6,D} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([98.084,137.51,171.148,197.348,236.789,264.86,303.613],'J/(mol*K)'),
        H298 = (269.873,'kJ/mol'),
        S298 = (293.067,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 34,
    label = "s3_5_6_ane",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {5,S} {9,S}
2  C u0 p0 c0 {3,S} {6,S} {7,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {21,S} {22,S}
4  C u0 p0 c0 {1,S} {8,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {6,S} {15,S} {16,S}
6  C u0 p0 c0 {2,S} {5,S} {17,S} {18,S}
7  C u0 p0 c0 {2,S} {8,S} {19,S} {20,S}
8  C u0 p0 c0 {4,S} {7,S} {11,S} {12,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {8,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([130.888,182.169,229.179,269.16,331.764,377.467,443.179],'J/(mol*K)'),
        H298 = (-45.1126,'kJ/mol'),
        S298 = (344.952,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 35,
    label = "s3_5_6_ene_1",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {6,S} {9,S}
2  C u0 p0 c0 {3,S} {5,S} {7,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {15,S} {16,S}
4  C u0 p0 c0 {1,S} {5,S} {13,S} {14,S}
5  C u0 p0 c0 {2,S} {4,S} {11,S} {12,S}
6  C u0 p0 c0 {1,S} {8,S} {17,S} {18,S}
7  C u0 p0 c0 {2,S} {8,D} {20,S}
8  C u0 p0 c0 {6,S} {7,D} {19,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([123.081,171.275,214.56,250.516,306.191,346.614,404.231],'J/(mol*K)'),
        H298 = (43.9683,'kJ/mol'),
        S298 = (328.164,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 36,
    label = "s3_5_6_ene_5",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {7,S} {9,S}
2  C u0 p0 c0 {3,S} {5,S} {8,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {17,S} {18,S}
4  C u0 p0 c0 {1,S} {6,S} {13,S} {14,S}
5  C u0 p0 c0 {2,S} {6,S} {15,S} {16,S}
6  C u0 p0 c0 {4,S} {5,S} {11,S} {12,S}
7  C u0 p0 c0 {1,S} {8,D} {19,S}
8  C u0 p0 c0 {2,S} {7,D} {20,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([122.814,171.672,215.163,250.988,306.506,346.805,404.243],'J/(mol*K)'),
        H298 = (59.5789,'kJ/mol'),
        S298 = (324.708,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 37,
    label = "s3_5_6_diene_1_5",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {5,S} {9,S}
2  C u0 p0 c0 {3,S} {6,S} {7,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {8,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {7,D} {18,S}
6  C u0 p0 c0 {2,S} {8,D} {16,S}
7  C u0 p0 c0 {2,S} {5,D} {17,S}
8  C u0 p0 c0 {4,S} {6,D} {15,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([117.765,161.74,199.471,231.643,281.888,317.205,365.146],'J/(mol*K)'),
        H298 = (178.49,'kJ/mol'),
        S298 = (319.795,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 38,
    label = "s1_4_4_ane",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {7,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {7,S} {18,S} {19,S}
6  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
7  C u0 p0 c0 {4,S} {5,S} {16,S} {17,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([121.943,165.135,203.981,236.918,289.192,327.313,382.093],'J/(mol*K)'),
        H298 = (110.826,'kJ/mol'),
        S298 = (326.963,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 39,
    label = "s1_4_4_ene_1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
5  C u0 p0 c0 {1,S} {7,S} {14,S} {15,S}
6  C u0 p0 c0 {1,S} {7,D} {17,S}
7  C u0 p0 c0 {5,S} {6,D} {16,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([115.843,155.093,189.711,218.557,263.974,296.833,343.426],'J/(mol*K)'),
        H298 = (246.766,'kJ/mol'),
        S298 = (327.921,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 40,
    label = "s1_4_4_diene_1_5",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {7,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {6,D} {13,S}
5  C u0 p0 c0 {1,S} {7,D} {15,S}
6  C u0 p0 c0 {2,S} {4,D} {12,S}
7  C u0 p0 c0 {3,S} {5,D} {14,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([109.589,144.714,174.968,199.701,238.348,266.032,304.615],'J/(mol*K)'),
        H298 = (383.729,'kJ/mol'),
        S298 = (317.164,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 41,
    label = "s1_4_5_ane",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {6,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {7,S} {15,S} {16,S}
5  C u0 p0 c0 {1,S} {8,S} {21,S} {22,S}
6  C u0 p0 c0 {2,S} {3,S} {11,S} {12,S}
7  C u0 p0 c0 {4,S} {8,S} {17,S} {18,S}
8  C u0 p0 c0 {5,S} {7,S} {19,S} {20,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([140.518,189.947,234.386,272.912,334.569,379.533,444.088],'J/(mol*K)'),
        H298 = (15.9546,'kJ/mol'),
        S298 = (357.993,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 42,
    label = "s1_4_5_ene_1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {6,S} {15,S} {16,S}
5  C u0 p0 c0 {2,S} {3,S} {11,S} {12,S}
6  C u0 p0 c0 {4,S} {8,S} {17,S} {18,S}
7  C u0 p0 c0 {1,S} {8,D} {20,S}
8  C u0 p0 c0 {6,S} {7,D} {19,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([132.663,179.076,220.116,254.652,309.375,349.011,405.302],'J/(mol*K)'),
        H298 = (126.479,'kJ/mol'),
        S298 = (346.275,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 43,
    label = "s1_4_5_ene_2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {3,S} {11,S} {12,S}
5  C u0 p0 c0 {1,S} {7,S} {15,S} {16,S}
6  C u0 p0 c0 {1,S} {8,S} {17,S} {18,S}
7  C u0 p0 c0 {5,S} {8,D} {19,S}
8  C u0 p0 c0 {6,S} {7,D} {20,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([131.898,178.625,219.973,254.62,309.361,349.017,405.348],'J/(mol*K)'),
        H298 = (127.731,'kJ/mol'),
        S298 = (344.189,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 44,
    label = "s1_4_5_ene_6",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {15,S} {16,S}
4  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
5  C u0 p0 c0 {3,S} {4,S} {13,S} {14,S}
6  C u0 p0 c0 {1,S} {8,S} {17,S} {18,S}
7  C u0 p0 c0 {1,S} {8,D} {20,S}
8  C u0 p0 c0 {6,S} {7,D} {19,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([134.226,179.413,219.499,254.089,309.12,348.896,405.205],'J/(mol*K)'),
        H298 = (154.073,'kJ/mol'),
        S298 = (353.88,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 45,
    label = "s1_4_5_diene_1_3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {3,S} {11,S} {12,S}
5  C u0 p0 c0 {1,S} {7,D} {15,S}
6  C u0 p0 c0 {1,S} {8,D} {16,S}
7  C u0 p0 c0 {5,D} {8,S} {17,S}
8  C u0 p0 c0 {6,D} {7,S} {18,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([125.397,168.432,205.742,236.319,284.073,318.352,366.312],'J/(mol*K)'),
        H298 = (232.997,'kJ/mol'),
        S298 = (338.661,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 46,
    label = "s1_4_5_diene_1_6",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {7,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {8,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {7,D} {16,S}
6  C u0 p0 c0 {1,S} {8,D} {18,S}
7  C u0 p0 c0 {3,S} {5,D} {15,S}
8  C u0 p0 c0 {4,S} {6,D} {17,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([126.441,168.673,205.348,235.794,283.741,318.192,366.44],'J/(mol*K)'),
        H298 = (263.104,'kJ/mol'),
        S298 = (342.199,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 47,
    label = "s1_4_5_diene_2_6",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {7,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {8,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {6,D} {16,S}
6  C u0 p0 c0 {2,S} {5,D} {15,S}
7  C u0 p0 c0 {3,S} {8,D} {17,S}
8  C u0 p0 c0 {4,S} {7,D} {18,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([126.029,168.666,205.629,236.12,283.997,318.398,366.584],'J/(mol*K)'),
        H298 = (265.187,'kJ/mol'),
        S298 = (339.393,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 48,
    label = "s1_4_6_ane",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {6,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {7,S} {16,S} {17,S}
5  C u0 p0 c0 {1,S} {9,S} {24,S} {25,S}
6  C u0 p0 c0 {2,S} {3,S} {12,S} {13,S}
7  C u0 p0 c0 {4,S} {8,S} {18,S} {19,S}
8  C u0 p0 c0 {7,S} {9,S} {20,S} {21,S}
9  C u0 p0 c0 {5,S} {8,S} {22,S} {23,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {5,S}
25 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([157.992,215.094,266.11,310.287,380.941,432.426,506.349],'J/(mol*K)'),
        H298 = (-31.9082,'kJ/mol'),
        S298 = (366.899,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 49,
    label = "s1_4_6_ene_1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {5,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {6,S} {16,S} {17,S}
5  C u0 p0 c0 {2,S} {3,S} {12,S} {13,S}
6  C u0 p0 c0 {4,S} {7,S} {18,S} {19,S}
7  C u0 p0 c0 {6,S} {9,S} {20,S} {21,S}
8  C u0 p0 c0 {1,S} {9,D} {23,S}
9  C u0 p0 c0 {7,S} {8,D} {22,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([151.649,204.798,251.556,291.514,355.225,401.452,467.331],'J/(mol*K)'),
        H298 = (85.3044,'kJ/mol'),
        S298 = (363.688,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 50,
    label = "s1_4_6_ene_2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {5,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {7,S} {16,S} {17,S}
5  C u0 p0 c0 {2,S} {3,S} {12,S} {13,S}
6  C u0 p0 c0 {1,S} {9,S} {20,S} {21,S}
7  C u0 p0 c0 {4,S} {8,S} {18,S} {19,S}
8  C u0 p0 c0 {7,S} {9,D} {22,S}
9  C u0 p0 c0 {6,S} {8,D} {23,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([151.57,204.721,251.494,291.461,355.184,401.419,467.308],'J/(mol*K)'),
        H298 = (85.2653,'kJ/mol'),
        S298 = (363.873,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 51,
    label = "s1_4_6_ene_7",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {6,S} {18,S} {19,S}
4  C u0 p0 c0 {2,S} {5,S} {12,S} {13,S}
5  C u0 p0 c0 {4,S} {6,S} {14,S} {15,S}
6  C u0 p0 c0 {3,S} {5,S} {16,S} {17,S}
7  C u0 p0 c0 {1,S} {9,S} {20,S} {21,S}
8  C u0 p0 c0 {1,S} {9,D} {23,S}
9  C u0 p0 c0 {7,S} {8,D} {22,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([151.014,204.311,251.227,291.206,354.958,401.251,467.302],'J/(mol*K)'),
        H298 = (106.224,'kJ/mol'),
        S298 = (361.083,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 52,
    label = "s1_4_6_diene_1_3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {4,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {3,S} {12,S} {13,S}
5  C u0 p0 c0 {1,S} {7,S} {16,S} {17,S}
6  C u0 p0 c0 {1,S} {9,D} {19,S}
7  C u0 p0 c0 {5,S} {8,D} {18,S}
8  C u0 p0 c0 {7,D} {9,S} {20,S}
9  C u0 p0 c0 {6,D} {8,S} {21,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([144.889,193.204,235.828,272.36,329.871,370.828,427.834],'J/(mol*K)'),
        H298 = (197.891,'kJ/mol'),
        S298 = (357.196,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 53,
    label = "s1_4_6_diene_1_4",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {4,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {3,S} {12,S} {13,S}
5  C u0 p0 c0 {8,S} {9,S} {16,S} {17,S}
6  C u0 p0 c0 {1,S} {8,D} {18,S}
7  C u0 p0 c0 {1,S} {9,D} {21,S}
8  C u0 p0 c0 {5,S} {6,D} {19,S}
9  C u0 p0 c0 {5,S} {7,D} {20,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([145.385,193.584,236.022,272.423,329.814,370.779,427.98],'J/(mol*K)'),
        H298 = (196.403,'kJ/mol'),
        S298 = (362.272,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 54,
    label = "s1_4_6_diene_1_7",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {8,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {9,S} {16,S} {17,S}
6  C u0 p0 c0 {1,S} {8,D} {19,S}
7  C u0 p0 c0 {1,S} {9,D} {21,S}
8  C u0 p0 c0 {4,S} {6,D} {18,S}
9  C u0 p0 c0 {5,S} {7,D} {20,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([145.177,193.373,235.842,272.279,329.745,370.78,428.089],'J/(mol*K)'),
        H298 = (221.809,'kJ/mol'),
        S298 = (358.851,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 55,
    label = "s1_4_6_diene_2_7",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {7,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {9,S} {16,S} {17,S}
5  C u0 p0 c0 {2,S} {8,S} {14,S} {15,S}
6  C u0 p0 c0 {1,S} {7,D} {19,S}
7  C u0 p0 c0 {3,S} {6,D} {18,S}
8  C u0 p0 c0 {5,S} {9,D} {20,S}
9  C u0 p0 c0 {4,S} {8,D} {21,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([144.902,193.142,235.697,272.201,329.746,370.809,428.092],'J/(mol*K)'),
        H298 = (220.926,'kJ/mol'),
        S298 = (356.995,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 56,
    label = "s1_5_5_ene_1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {6,S} {14,S} {15,S}
3  C u0 p0 c0 {1,S} {5,S} {18,S} {19,S}
4  C u0 p0 c0 {1,S} {7,S} {16,S} {17,S}
5  C u0 p0 c0 {3,S} {6,S} {10,S} {11,S}
6  C u0 p0 c0 {2,S} {5,S} {12,S} {13,S}
7  C u0 p0 c0 {4,S} {9,S} {20,S} {21,S}
8  C u0 p0 c0 {1,S} {9,D} {23,S}
9  C u0 p0 c0 {7,S} {8,D} {22,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([149.885,203.098,250.242,290.524,354.681,401.166,467.195],'J/(mol*K)'),
        H298 = (35.7228,'kJ/mol'),
        S298 = (376.462,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 57,
    label = "s1_5_5_ene_2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {14,S} {15,S}
3  C u0 p0 c0 {1,S} {4,S} {16,S} {17,S}
4  C u0 p0 c0 {3,S} {5,S} {10,S} {11,S}
5  C u0 p0 c0 {2,S} {4,S} {12,S} {13,S}
6  C u0 p0 c0 {1,S} {8,S} {18,S} {19,S}
7  C u0 p0 c0 {1,S} {9,S} {20,S} {21,S}
8  C u0 p0 c0 {6,S} {9,D} {22,S}
9  C u0 p0 c0 {7,S} {8,D} {23,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([150.116,203.2,250.233,290.539,354.752,401.269,467.321],'J/(mol*K)'),
        H298 = (33.8776,'kJ/mol'),
        S298 = (365.57,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 58,
    label = "s1_5_5_diene_1_3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {14,S} {15,S}
3  C u0 p0 c0 {1,S} {4,S} {16,S} {17,S}
4  C u0 p0 c0 {3,S} {5,S} {10,S} {11,S}
5  C u0 p0 c0 {2,S} {4,S} {12,S} {13,S}
6  C u0 p0 c0 {1,S} {8,D} {18,S}
7  C u0 p0 c0 {1,S} {9,D} {19,S}
8  C u0 p0 c0 {6,D} {9,S} {20,S}
9  C u0 p0 c0 {7,D} {8,S} {21,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([143.136,192.54,235.674,271.868,329.106,370.288,428.092],'J/(mol*K)'),
        H298 = (140.028,'kJ/mol'),
        S298 = (360.184,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 59,
    label = "s1_5_5_diene_1_6",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {9,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {8,S} {16,S} {17,S}
6  C u0 p0 c0 {1,S} {8,D} {19,S}
7  C u0 p0 c0 {1,S} {9,D} {21,S}
8  C u0 p0 c0 {5,S} {6,D} {18,S}
9  C u0 p0 c0 {4,S} {7,D} {20,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([143.629,192.952,235.951,272.104,329.337,370.528,428.372],'J/(mol*K)'),
        H298 = (147.348,'kJ/mol'),
        S298 = (361.916,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 60,
    label = "s1_5_5_diene_1_7",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {6,S}
2  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {8,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {7,S} {16,S} {17,S}
5  C u0 p0 c0 {2,S} {9,S} {14,S} {15,S}
6  C u0 p0 c0 {1,S} {9,D} {21,S}
7  C u0 p0 c0 {4,S} {8,D} {18,S}
8  C u0 p0 c0 {3,S} {7,D} {19,S}
9  C u0 p0 c0 {5,S} {6,D} {20,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([142.784,192.508,235.878,272.103,329.325,370.529,428.436],'J/(mol*K)'),
        H298 = (147.135,'kJ/mol'),
        S298 = (357.946,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 61,
    label = "s1_5_5_diene_2_7",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {7,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {8,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {9,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {6,S} {16,S} {17,S}
6  C u0 p0 c0 {5,S} {7,D} {18,S}
7  C u0 p0 c0 {2,S} {6,D} {19,S}
8  C u0 p0 c0 {3,S} {9,D} {20,S}
9  C u0 p0 c0 {4,S} {8,D} {21,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([155.329,202.847,242.537,276.111,329.363,367.746,422.362],'J/(mol*K)'),
        H298 = (863.556,'kJ/mol'),
        S298 = (370.12,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 62,
    label = "s1_5_6_ene_1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {9,S}
2  C u0 p0 c0 {1,S} {6,S} {15,S} {16,S}
3  C u0 p0 c0 {1,S} {7,S} {17,S} {18,S}
4  C u0 p0 c0 {1,S} {5,S} {21,S} {22,S}
5  C u0 p0 c0 {4,S} {6,S} {11,S} {12,S}
6  C u0 p0 c0 {2,S} {5,S} {13,S} {14,S}
7  C u0 p0 c0 {3,S} {8,S} {19,S} {20,S}
8  C u0 p0 c0 {7,S} {10,S} {23,S} {24,S}
9  C u0 p0 c0 {1,S} {10,D} {26,S}
10 C u0 p0 c0 {8,S} {9,D} {25,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {6,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {10,S}
26 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([168.917,228.569,281.749,327.656,400.705,453.572,528.926],'J/(mol*K)'),
        H298 = (-2.56223,'kJ/mol'),
        S298 = (389.174,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 63,
    label = "s1_5_6_ene_7",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {7,S} {19,S} {20,S}
4  C u0 p0 c0 {1,S} {8,S} {21,S} {22,S}
5  C u0 p0 c0 {2,S} {6,S} {13,S} {14,S}
6  C u0 p0 c0 {5,S} {7,S} {15,S} {16,S}
7  C u0 p0 c0 {3,S} {6,S} {17,S} {18,S}
8  C u0 p0 c0 {4,S} {10,S} {23,S} {24,S}
9  C u0 p0 c0 {1,S} {10,D} {26,S}
10 C u0 p0 c0 {8,S} {9,D} {25,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {10,S}
26 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([168.452,228.476,281.596,327.478,400.618,453.651,529.17],'J/(mol*K)'),
        H298 = (-8.42059,'kJ/mol'),
        S298 = (379.262,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 64,
    label = "s1_5_6_ene_8",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {6,S} {19,S} {20,S}
4  C u0 p0 c0 {2,S} {5,S} {13,S} {14,S}
5  C u0 p0 c0 {4,S} {6,S} {15,S} {16,S}
6  C u0 p0 c0 {3,S} {5,S} {17,S} {18,S}
7  C u0 p0 c0 {1,S} {10,S} {21,S} {22,S}
8  C u0 p0 c0 {1,S} {9,S} {23,S} {24,S}
9  C u0 p0 c0 {8,S} {10,D} {25,S}
10 C u0 p0 c0 {7,S} {9,D} {26,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {9,S}
26 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([168.446,228.472,281.593,327.477,400.618,453.651,529.17],'J/(mol*K)'),
        H298 = (-8.42087,'kJ/mol'),
        S298 = (379.242,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 65,
    label = "s1_5_6_diene_1_4",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {15,S} {16,S}
3  C u0 p0 c0 {1,S} {4,S} {17,S} {18,S}
4  C u0 p0 c0 {3,S} {5,S} {11,S} {12,S}
5  C u0 p0 c0 {2,S} {4,S} {13,S} {14,S}
6  C u0 p0 c0 {9,S} {10,S} {19,S} {20,S}
7  C u0 p0 c0 {1,S} {9,D} {21,S}
8  C u0 p0 c0 {1,S} {10,D} {24,S}
9  C u0 p0 c0 {6,S} {7,D} {22,S}
10 C u0 p0 c0 {6,S} {8,D} {23,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {10,S}
24 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([162.363,217.73,266.522,308.48,374.905,422.61,489.81],'J/(mol*K)'),
        H298 = (109.661,'kJ/mol'),
        S298 = (388.467,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 66,
    label = "s1_5_6_diene_1_7",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {6,S} {15,S} {16,S}
4  C u0 p0 c0 {2,S} {5,S} {13,S} {14,S}
5  C u0 p0 c0 {4,S} {10,S} {17,S} {18,S}
6  C u0 p0 c0 {3,S} {9,S} {19,S} {20,S}
7  C u0 p0 c0 {1,S} {9,D} {22,S}
8  C u0 p0 c0 {1,S} {10,D} {24,S}
9  C u0 p0 c0 {6,S} {7,D} {21,S}
10 C u0 p0 c0 {5,S} {8,D} {23,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {10,S}
24 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([162.208,217.672,266.584,308.624,375.124,422.823,489.886],'J/(mol*K)'),
        H298 = (107.764,'kJ/mol'),
        S298 = (376.841,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 67,
    label = "s1_5_6_diene_1_8",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {6,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {9,S} {15,S} {16,S}
5  C u0 p0 c0 {1,S} {8,S} {19,S} {20,S}
6  C u0 p0 c0 {3,S} {10,S} {17,S} {18,S}
7  C u0 p0 c0 {1,S} {10,D} {24,S}
8  C u0 p0 c0 {5,S} {9,D} {21,S}
9  C u0 p0 c0 {4,S} {8,D} {22,S}
10 C u0 p0 c0 {6,S} {7,D} {23,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {10,S}
24 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([161.972,217.559,266.632,308.787,375.401,423.107,490.021],'J/(mol*K)'),
        H298 = (107.455,'kJ/mol'),
        S298 = (375.034,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 68,
    label = "s1_5_6_diene_2_7",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {6,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {10,S} {17,S} {18,S}
5  C u0 p0 c0 {2,S} {9,S} {15,S} {16,S}
6  C u0 p0 c0 {3,S} {8,S} {19,S} {20,S}
7  C u0 p0 c0 {1,S} {8,D} {22,S}
8  C u0 p0 c0 {6,S} {7,D} {21,S}
9  C u0 p0 c0 {5,S} {10,D} {23,S}
10 C u0 p0 c0 {4,S} {9,D} {24,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([161.895,217.448,266.497,308.639,375.253,422.98,489.965],'J/(mol*K)'),
        H298 = (103.668,'kJ/mol'),
        S298 = (374.293,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 69,
    label = "s1_5_6_diene_2_8",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {8,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {10,S} {17,S} {18,S}
5  C u0 p0 c0 {1,S} {7,S} {19,S} {20,S}
6  C u0 p0 c0 {2,S} {9,S} {15,S} {16,S}
7  C u0 p0 c0 {5,S} {8,D} {21,S}
8  C u0 p0 c0 {3,S} {7,D} {22,S}
9  C u0 p0 c0 {6,S} {10,D} {23,S}
10 C u0 p0 c0 {4,S} {9,D} {24,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([161.335,216.94,266.125,308.382,375.152,422.961,489.984],'J/(mol*K)'),
        H298 = (106.316,'kJ/mol'),
        S298 = (373.78,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 70,
    label = "s1_5_6_diene_7_9",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {6,S} {19,S} {20,S}
4  C u0 p0 c0 {2,S} {5,S} {13,S} {14,S}
5  C u0 p0 c0 {4,S} {6,S} {15,S} {16,S}
6  C u0 p0 c0 {3,S} {5,S} {17,S} {18,S}
7  C u0 p0 c0 {1,S} {9,D} {21,S}
8  C u0 p0 c0 {1,S} {10,D} {22,S}
9  C u0 p0 c0 {7,D} {10,S} {23,S}
10 C u0 p0 c0 {8,D} {9,S} {24,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([160.186,217.293,266.992,308.687,374.798,422.545,490.044],'J/(mol*K)'),
        H298 = (98.4814,'kJ/mol'),
        S298 = (370.934,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 71,
    label = "s1_6_6_ene_1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {10,S}
2  C u0 p0 c0 {1,S} {6,S} {16,S} {17,S}
3  C u0 p0 c0 {1,S} {8,S} {18,S} {19,S}
4  C u0 p0 c0 {1,S} {7,S} {22,S} {23,S}
5  C u0 p0 c0 {6,S} {7,S} {12,S} {13,S}
6  C u0 p0 c0 {2,S} {5,S} {14,S} {15,S}
7  C u0 p0 c0 {4,S} {5,S} {24,S} {25,S}
8  C u0 p0 c0 {3,S} {9,S} {20,S} {21,S}
9  C u0 p0 c0 {8,S} {11,S} {26,S} {27,S}
10 C u0 p0 c0 {1,S} {11,D} {29,S}
11 C u0 p0 c0 {9,S} {10,D} {28,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {4,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
26 H u0 p0 c0 {9,S}
27 H u0 p0 c0 {9,S}
28 H u0 p0 c0 {11,S}
29 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([186.658,253.578,313.077,364.471,446.378,505.794,590.807],'J/(mol*K)'),
        H298 = (-41.7851,'kJ/mol'),
        S298 = (396.235,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 72,
    label = "s1_6_6_ene_2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {6,S} {16,S} {17,S}
3  C u0 p0 c0 {1,S} {7,S} {20,S} {21,S}
4  C u0 p0 c0 {1,S} {9,S} {18,S} {19,S}
5  C u0 p0 c0 {6,S} {7,S} {12,S} {13,S}
6  C u0 p0 c0 {2,S} {5,S} {14,S} {15,S}
7  C u0 p0 c0 {3,S} {5,S} {22,S} {23,S}
8  C u0 p0 c0 {1,S} {11,S} {26,S} {27,S}
9  C u0 p0 c0 {4,S} {10,S} {24,S} {25,S}
10 C u0 p0 c0 {9,S} {11,D} {28,S}
11 C u0 p0 c0 {8,S} {10,D} {29,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {9,S}
25 H u0 p0 c0 {9,S}
26 H u0 p0 c0 {8,S}
27 H u0 p0 c0 {8,S}
28 H u0 p0 c0 {10,S}
29 H u0 p0 c0 {11,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([186.173,253.138,312.767,364.274,446.347,505.865,590.955],'J/(mol*K)'),
        H298 = (-45.4939,'kJ/mol'),
        S298 = (392.839,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 73,
    label = "s1_6_6_diene_1_3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {16,S} {17,S}
3  C u0 p0 c0 {1,S} {6,S} {18,S} {19,S}
4  C u0 p0 c0 {5,S} {6,S} {12,S} {13,S}
5  C u0 p0 c0 {2,S} {4,S} {14,S} {15,S}
6  C u0 p0 c0 {3,S} {4,S} {20,S} {21,S}
7  C u0 p0 c0 {1,S} {9,S} {22,S} {23,S}
8  C u0 p0 c0 {1,S} {11,D} {25,S}
9  C u0 p0 c0 {7,S} {10,D} {24,S}
10 C u0 p0 c0 {9,D} {11,S} {26,S}
11 C u0 p0 c0 {8,D} {10,S} {27,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {9,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {10,S}
27 H u0 p0 c0 {11,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([181.037,243.836,299.027,346.498,421.705,475.777,552.115],'J/(mol*K)'),
        H298 = (65.62,'kJ/mol'),
        S298 = (391.515,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 74,
    label = "s1_6_6_diene_1_4",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {16,S} {17,S}
3  C u0 p0 c0 {1,S} {6,S} {18,S} {19,S}
4  C u0 p0 c0 {5,S} {6,S} {12,S} {13,S}
5  C u0 p0 c0 {2,S} {4,S} {14,S} {15,S}
6  C u0 p0 c0 {3,S} {4,S} {20,S} {21,S}
7  C u0 p0 c0 {10,S} {11,S} {22,S} {23,S}
8  C u0 p0 c0 {1,S} {10,D} {24,S}
9  C u0 p0 c0 {1,S} {11,D} {27,S}
10 C u0 p0 c0 {7,S} {8,D} {25,S}
11 C u0 p0 c0 {7,S} {9,D} {26,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {10,S}
26 H u0 p0 c0 {11,S}
27 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([180.536,243.108,298.138,345.526,420.735,474.953,551.788],'J/(mol*K)'),
        H298 = (68.842,'kJ/mol'),
        S298 = (397.306,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 75,
    label = "s1_6_6_diene_1_7",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {8,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {14,S} {15,S}
3  C u0 p0 c0 {1,S} {5,S} {16,S} {17,S}
4  C u0 p0 c0 {2,S} {6,S} {12,S} {13,S}
5  C u0 p0 c0 {3,S} {7,S} {18,S} {19,S}
6  C u0 p0 c0 {4,S} {11,S} {20,S} {21,S}
7  C u0 p0 c0 {5,S} {10,S} {22,S} {23,S}
8  C u0 p0 c0 {1,S} {10,D} {25,S}
9  C u0 p0 c0 {1,S} {11,D} {26,S}
10 C u0 p0 c0 {7,S} {8,D} {24,S}
11 C u0 p0 c0 {6,S} {9,D} {27,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {10,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {9,S}
27 H u0 p0 c0 {11,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([180.801,243.373,298.375,345.738,420.908,475.098,551.883],'J/(mol*K)'),
        H298 = (72.8519,'kJ/mol'),
        S298 = (389.472,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 76,
    label = "s1_6_6_diene_2_8",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {5,S}
2  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {7,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {9,S} {16,S} {17,S}
5  C u0 p0 c0 {1,S} {11,S} {20,S} {21,S}
6  C u0 p0 c0 {2,S} {10,S} {18,S} {19,S}
7  C u0 p0 c0 {3,S} {8,S} {22,S} {23,S}
8  C u0 p0 c0 {7,S} {9,D} {24,S}
9  C u0 p0 c0 {4,S} {8,D} {25,S}
10 C u0 p0 c0 {6,S} {11,D} {26,S}
11 C u0 p0 c0 {5,S} {10,D} {27,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {9,S}
26 H u0 p0 c0 {10,S}
27 H u0 p0 c0 {11,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([180.416,243.184,298.426,345.96,421.306,475.518,552.113],'J/(mol*K)'),
        H298 = (64.4888,'kJ/mol'),
        S298 = (383.312,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 77,
    label = "s2_5_5_ane",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {5,S} {10,S}
3  C u0 p0 c0 {1,S} {7,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {7,S} {15,S} {16,S}
5  C u0 p0 c0 {2,S} {8,S} {17,S} {18,S}
6  C u0 p0 c0 {1,S} {8,S} {21,S} {22,S}
7  C u0 p0 c0 {3,S} {4,S} {13,S} {14,S}
8  C u0 p0 c0 {5,S} {6,S} {19,S} {20,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {7,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([131.971,183.294,230.161,269.936,332.32,377.857,443.327],'J/(mol*K)'),
        H298 = (-60.5633,'kJ/mol'),
        S298 = (334.309,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 78,
    label = "s2_5_5_ene_0",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {6,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {5,S} {12,S} {13,S}
5  C u0 p0 c0 {4,S} {7,S} {16,S} {17,S}
6  C u0 p0 c0 {3,S} {8,S} {18,S} {19,S}
7  C u0 p0 c0 {1,S} {5,S} {8,D}
8  C u0 p0 c0 {6,S} {7,D} {20,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([128.241,174.574,216.187,251.341,306.886,347.229,404.699],'J/(mol*K)'),
        H298 = (59.5825,'kJ/mol'),
        S298 = (341.477,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 79,
    label = "s2_5_5_ene_1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {10,S}
3  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {5,S} {15,S} {16,S}
5  C u0 p0 c0 {3,S} {4,S} {13,S} {14,S}
6  C u0 p0 c0 {1,S} {8,S} {17,S} {18,S}
7  C u0 p0 c0 {2,S} {8,D} {19,S}
8  C u0 p0 c0 {6,S} {7,D} {20,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([126.412,173.471,215.808,251.327,306.907,347.255,404.692],'J/(mol*K)'),
        H298 = (97.6221,'kJ/mol'),
        S298 = (337.456,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 80,
    label = "s2_5_5_ene_m",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
2  C u0 p0 c0 {5,S} {6,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {7,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {8,S} {15,S} {16,S}
5  C u0 p0 c0 {2,S} {8,S} {17,S} {18,S}
6  C u0 p0 c0 {2,S} {7,S} {19,S} {20,S}
7  C u0 p0 c0 {3,S} {6,S} {8,D}
8  C u0 p0 c0 {4,S} {5,S} {7,D}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([130.002,174.747,215.027,249.941,305.763,346.4,404.463],'J/(mol*K)'),
        H298 = (51.8163,'kJ/mol'),
        S298 = (340.969,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 81,
    label = "s2_5_5_diene_0_2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {4,S} {12,S} {13,S}
4  C u0 p0 c0 {3,S} {5,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {4,S} {7,D}
6  C u0 p0 c0 {1,S} {8,D} {16,S}
7  C u0 p0 c0 {5,D} {8,S} {17,S}
8  C u0 p0 c0 {6,D} {7,S} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([120.56,163.712,201.795,233.162,281.805,316.809,365.896],'J/(mol*K)'),
        H298 = (168.446,'kJ/mol'),
        S298 = (333.359,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 82,
    label = "s2_5_5_diene_0_3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {5,S} {13,S} {14,S}
4  C u0 p0 c0 {7,S} {8,S} {15,S} {16,S}
5  C u0 p0 c0 {3,S} {6,S} {7,D}
6  C u0 p0 c0 {2,S} {5,S} {8,D}
7  C u0 p0 c0 {4,S} {5,D} {17,S}
8  C u0 p0 c0 {4,S} {6,D} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([122.255,165.367,202.957,233.824,282.097,316.898,365.91],'J/(mol*K)'),
        H298 = (152.083,'kJ/mol'),
        S298 = (332.701,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 83,
    label = "s2_5_5_diene_m_2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {6,S} {13,S} {14,S}
4  C u0 p0 c0 {5,S} {7,S} {15,S} {16,S}
5  C u0 p0 c0 {2,S} {4,S} {6,D}
6  C u0 p0 c0 {3,S} {5,D} {8,S}
7  C u0 p0 c0 {4,S} {8,D} {17,S}
8  C u0 p0 c0 {6,S} {7,D} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([122.291,164.44,201.573,232.504,281.162,316.272,365.736],'J/(mol*K)'),
        H298 = (157.584,'kJ/mol'),
        S298 = (335.975,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 84,
    label = "s2_5_5_diene_0_4",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {6,S} {11,S} {12,S}
2  C u0 p0 c0 {4,S} {5,S} {15,S} {16,S}
3  C u0 p0 c0 {1,S} {7,S} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {8,S} {13,S} {14,S}
5  C u0 p0 c0 {2,S} {6,S} {7,D}
6  C u0 p0 c0 {1,S} {5,S} {8,D}
7  C u0 p0 c0 {3,S} {5,D} {17,S}
8  C u0 p0 c0 {4,S} {6,D} {18,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([123.294,164.511,200.951,231.827,280.766,316.031,365.575],'J/(mol*K)'),
        H298 = (156.012,'kJ/mol'),
        S298 = (342.451,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 85,
    label = "s2_5_5_diene_0_5",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {7,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {10,S} {11,S}
3  C u0 p0 c0 {2,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {5,S} {8,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {4,S} {6,D}
6  C u0 p0 c0 {3,S} {5,D} {16,S}
7  C u0 p0 c0 {1,S} {8,D} {17,S}
8  C u0 p0 c0 {4,S} {7,D} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([120.159,163.404,201.457,232.749,281.403,316.475,365.808],'J/(mol*K)'),
        H298 = (178.147,'kJ/mol'),
        S298 = (330.713,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 86,
    label = "s2_5_5_diene_0_6",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {4,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {7,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {6,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {6,D} {8,S}
6  C u0 p0 c0 {4,S} {5,D} {17,S}
7  C u0 p0 c0 {3,S} {8,D} {16,S}
8  C u0 p0 c0 {5,S} {7,D} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([119.766,163.082,201.233,232.595,281.297,316.402,365.777],'J/(mol*K)'),
        H298 = (164.781,'kJ/mol'),
        S298 = (330.159,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 87,
    label = "s2_5_5_diene_1_5",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {9,S}
2  C u0 p0 c0 {1,S} {3,S} {6,S} {10,S}
3  C u0 p0 c0 {2,S} {7,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {8,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {7,D} {15,S}
6  C u0 p0 c0 {2,S} {8,D} {17,S}
7  C u0 p0 c0 {3,S} {5,D} {16,S}
8  C u0 p0 c0 {4,S} {6,D} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([118.589,163.005,201.743,233.189,281.823,316.829,365.971],'J/(mol*K)'),
        H298 = (230.177,'kJ/mol'),
        S298 = (325.159,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 88,
    label = "s2_5_5_diene_1_6",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {9,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {10,S}
3  C u0 p0 c0 {1,S} {7,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {8,S} {13,S} {14,S}
5  C u0 p0 c0 {2,S} {7,D} {16,S}
6  C u0 p0 c0 {2,S} {8,D} {17,S}
7  C u0 p0 c0 {3,S} {5,D} {15,S}
8  C u0 p0 c0 {4,S} {6,D} {18,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([119.2,162.633,201.131,232.813,281.63,316.729,365.872],'J/(mol*K)'),
        H298 = (162.274,'kJ/mol'),
        S298 = (332.771,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 89,
    label = "s2_5_6_ane",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {5,S} {11,S}
3  C u0 p0 c0 {1,S} {7,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {7,S} {16,S} {17,S}
5  C u0 p0 c0 {2,S} {8,S} {18,S} {19,S}
6  C u0 p0 c0 {1,S} {9,S} {24,S} {25,S}
7  C u0 p0 c0 {3,S} {4,S} {14,S} {15,S}
8  C u0 p0 c0 {5,S} {9,S} {20,S} {21,S}
9  C u0 p0 c0 {6,S} {8,S} {22,S} {23,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {7,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {6,S}
25 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([153.649,210.593,262.111,306.834,378.45,430.72,505.818],'J/(mol*K)'),
        H298 = (-98.1354,'kJ/mol'),
        S298 = (366.674,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 90,
    label = "s2_5_6_ene_0",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {8,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {5,S} {17,S} {18,S}
4  C u0 p0 c0 {2,S} {6,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {7,S} {15,S} {16,S}
6  C u0 p0 c0 {4,S} {8,S} {19,S} {20,S}
7  C u0 p0 c0 {5,S} {9,S} {21,S} {22,S}
8  C u0 p0 c0 {1,S} {6,S} {9,D}
9  C u0 p0 c0 {7,S} {8,D} {23,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([147.636,200.52,247.668,288.148,352.774,399.75,466.801],'J/(mol*K)'),
        H298 = (7.32767,'kJ/mol'),
        S298 = (361.131,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 91,
    label = "s2_5_6_ene_1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {11,S}
3  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {6,S} {16,S} {17,S}
5  C u0 p0 c0 {1,S} {7,S} {18,S} {19,S}
6  C u0 p0 c0 {3,S} {4,S} {14,S} {15,S}
7  C u0 p0 c0 {5,S} {9,S} {20,S} {21,S}
8  C u0 p0 c0 {2,S} {9,D} {22,S}
9  C u0 p0 c0 {7,S} {8,D} {23,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([147.18,200.101,247.391,287.992,352.766,399.802,466.801],'J/(mol*K)'),
        H298 = (26.6061,'kJ/mol'),
        S298 = (362.406,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 92,
    label = "s2_5_6_ene_2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {11,S}
3  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {5,S} {16,S} {17,S}
5  C u0 p0 c0 {3,S} {4,S} {14,S} {15,S}
6  C u0 p0 c0 {2,S} {8,S} {18,S} {19,S}
7  C u0 p0 c0 {1,S} {9,S} {20,S} {21,S}
8  C u0 p0 c0 {6,S} {9,D} {22,S}
9  C u0 p0 c0 {7,S} {8,D} {23,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([145.336,199.326,247.582,288.325,352.863,399.758,466.648],'J/(mol*K)'),
        H298 = (26.0409,'kJ/mol'),
        S298 = (356.073,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 93,
    label = "s2_5_6_ene_5",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {8,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {7,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {5,S} {15,S} {16,S}
5  C u0 p0 c0 {4,S} {6,S} {17,S} {18,S}
6  C u0 p0 c0 {5,S} {8,S} {21,S} {22,S}
7  C u0 p0 c0 {3,S} {9,S} {19,S} {20,S}
8  C u0 p0 c0 {1,S} {6,S} {9,D}
9  C u0 p0 c0 {7,S} {8,D} {23,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([148.34,200.776,247.601,288.108,352.771,399.744,466.733],'J/(mol*K)'),
        H298 = (25.1635,'kJ/mol'),
        S298 = (362.654,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 94,
    label = "s2_5_6_ene_6",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {11,S}
3  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {6,S} {18,S} {19,S}
5  C u0 p0 c0 {3,S} {6,S} {14,S} {15,S}
6  C u0 p0 c0 {4,S} {5,S} {16,S} {17,S}
7  C u0 p0 c0 {1,S} {9,S} {20,S} {21,S}
8  C u0 p0 c0 {2,S} {9,D} {22,S}
9  C u0 p0 c0 {7,S} {8,D} {23,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([146.716,200.253,248.005,288.568,353.112,400.015,466.916],'J/(mol*K)'),
        H298 = (43.9256,'kJ/mol'),
        S298 = (357.514,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 95,
    label = "s2_5_6_diene_m_1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {6,S} {18,S} {19,S}
3  C u0 p0 c0 {5,S} {6,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {7,S} {16,S} {17,S}
5  C u0 p0 c0 {3,S} {8,S} {14,S} {15,S}
6  C u0 p0 c0 {2,S} {3,S} {7,D}
7  C u0 p0 c0 {4,S} {6,D} {9,S}
8  C u0 p0 c0 {5,S} {9,D} {20,S}
9  C u0 p0 c0 {7,S} {8,D} {21,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([142.503,190.245,232.653,269.181,327.11,368.808,427.631],'J/(mol*K)'),
        H298 = (109.333,'kJ/mol'),
        S298 = (359.545,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 96,
    label = "s2_5_6_diene_m_2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {7,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {6,S} {14,S} {15,S}
4  C u0 p0 c0 {6,S} {8,S} {16,S} {17,S}
5  C u0 p0 c0 {7,S} {9,S} {18,S} {19,S}
6  C u0 p0 c0 {3,S} {4,S} {7,D}
7  C u0 p0 c0 {2,S} {5,S} {6,D}
8  C u0 p0 c0 {4,S} {9,D} {20,S}
9  C u0 p0 c0 {5,S} {8,D} {21,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([142.004,189.618,231.971,268.488,326.488,368.328,427.52],'J/(mol*K)'),
        H298 = (104.843,'kJ/mol'),
        S298 = (360.684,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 97,
    label = "s2_5_6_diene_0_2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {4,S} {13,S} {14,S}
4  C u0 p0 c0 {3,S} {6,S} {15,S} {16,S}
5  C u0 p0 c0 {1,S} {7,S} {17,S} {18,S}
6  C u0 p0 c0 {1,S} {4,S} {8,D}
7  C u0 p0 c0 {5,S} {9,D} {19,S}
8  C u0 p0 c0 {6,D} {9,S} {20,S}
9  C u0 p0 c0 {7,D} {8,S} {21,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([140.048,189.786,233.402,269.834,327.419,369.041,427.885],'J/(mol*K)'),
        H298 = (113.676,'kJ/mol'),
        S298 = (352.027,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 98,
    label = "s2_5_6_diene_0_3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {8,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {4,S} {13,S} {14,S}
4  C u0 p0 c0 {3,S} {6,S} {15,S} {16,S}
5  C u0 p0 c0 {7,S} {9,S} {17,S} {18,S}
6  C u0 p0 c0 {1,S} {4,S} {7,D}
7  C u0 p0 c0 {5,S} {6,D} {19,S}
8  C u0 p0 c0 {1,S} {9,D} {21,S}
9  C u0 p0 c0 {5,S} {8,D} {20,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([140.877,189.819,232.865,269.279,327.091,368.853,427.82],'J/(mol*K)'),
        H298 = (123.043,'kJ/mol'),
        S298 = (359.524,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 99,
    label = "s2_5_6_diene_0_4",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {7,S} {16,S} {17,S}
3  C u0 p0 c0 {1,S} {6,S} {18,S} {19,S}
4  C u0 p0 c0 {5,S} {8,S} {12,S} {13,S}
5  C u0 p0 c0 {4,S} {9,S} {14,S} {15,S}
6  C u0 p0 c0 {3,S} {7,S} {8,D}
7  C u0 p0 c0 {2,S} {6,S} {9,D}
8  C u0 p0 c0 {4,S} {6,D} {20,S}
9  C u0 p0 c0 {5,S} {7,D} {21,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([142.027,190.862,233.586,269.768,327.297,368.906,427.822],'J/(mol*K)'),
        H298 = (112.398,'kJ/mol'),
        S298 = (355.516,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 100,
    label = "s2_5_6_diene_0_5",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {6,S} {18,S} {19,S}
3  C u0 p0 c0 {5,S} {7,S} {14,S} {15,S}
4  C u0 p0 c0 {1,S} {9,S} {16,S} {17,S}
5  C u0 p0 c0 {3,S} {8,S} {12,S} {13,S}
6  C u0 p0 c0 {2,S} {7,S} {8,D}
7  C u0 p0 c0 {3,S} {6,S} {9,D}
8  C u0 p0 c0 {5,S} {6,D} {20,S}
9  C u0 p0 c0 {4,S} {7,D} {21,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {2,S}
19 H u0 p0 c0 {2,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([141.54,189.96,232.518,268.86,326.683,368.489,427.62],'J/(mol*K)'),
        H298 = (99.1009,'kJ/mol'),
        S298 = (359.055,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 101,
    label = "s2_5_6_diene_0_6",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {8,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {13,S} {14,S}
3  C u0 p0 c0 {2,S} {4,S} {11,S} {12,S}
4  C u0 p0 c0 {3,S} {7,S} {15,S} {16,S}
5  C u0 p0 c0 {6,S} {9,S} {17,S} {18,S}
6  C u0 p0 c0 {1,S} {5,S} {7,D}
7  C u0 p0 c0 {4,S} {6,D} {21,S}
8  C u0 p0 c0 {1,S} {9,D} {19,S}
9  C u0 p0 c0 {5,S} {8,D} {20,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([139.706,189.406,233.046,269.529,327.208,368.91,427.886],'J/(mol*K)'),
        H298 = (124.829,'kJ/mol'),
        S298 = (351.576,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 102,
    label = "s2_5_6_diene_0_7",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {6,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {13,S} {14,S}
3  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {8,S} {15,S} {16,S}
5  C u0 p0 c0 {3,S} {7,S} {17,S} {18,S}
6  C u0 p0 c0 {1,S} {7,D} {9,S}
7  C u0 p0 c0 {5,S} {6,D} {20,S}
8  C u0 p0 c0 {4,S} {9,D} {19,S}
9  C u0 p0 c0 {6,S} {8,D} {21,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([139.457,189.14,232.813,269.334,327.062,368.8,427.824],'J/(mol*K)'),
        H298 = (109.137,'kJ/mol'),
        S298 = (351.464,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 103,
    label = "s2_5_6_diene_1_3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {6,S} {11,S}
3  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {5,S} {16,S} {17,S}
5  C u0 p0 c0 {3,S} {4,S} {14,S} {15,S}
6  C u0 p0 c0 {2,S} {8,D} {18,S}
7  C u0 p0 c0 {1,S} {9,D} {19,S}
8  C u0 p0 c0 {6,D} {9,S} {20,S}
9  C u0 p0 c0 {7,D} {8,S} {21,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([139.21,188.825,232.594,269.245,327.104,368.879,427.798],'J/(mol*K)'),
        H298 = (139.396,'kJ/mol'),
        S298 = (348.437,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 104,
    label = "s2_5_6_diene_1_5",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {8,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {5,S} {6,S} {17,S} {18,S}
4  C u0 p0 c0 {2,S} {7,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {9,S} {15,S} {16,S}
6  C u0 p0 c0 {1,S} {3,S} {7,D}
7  C u0 p0 c0 {4,S} {6,D} {19,S}
8  C u0 p0 c0 {1,S} {9,D} {20,S}
9  C u0 p0 c0 {5,S} {8,D} {21,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([141.306,190.459,233.588,269.948,327.615,369.257,428.023],'J/(mol*K)'),
        H298 = (135.454,'kJ/mol'),
        S298 = (356.77,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 105,
    label = "s2_5_6_diene_1_6",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {11,S}
3  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {8,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {9,S} {16,S} {17,S}
6  C u0 p0 c0 {1,S} {8,D} {18,S}
7  C u0 p0 c0 {2,S} {9,D} {20,S}
8  C u0 p0 c0 {4,S} {6,D} {19,S}
9  C u0 p0 c0 {5,S} {7,D} {21,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([138.783,188.85,232.934,269.629,327.369,369.059,427.878],'J/(mol*K)'),
        H298 = (126.678,'kJ/mol'),
        S298 = (350.813,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 106,
    label = "s2_5_6_diene_1_7",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {10,S}
2  C u0 p0 c0 {1,S} {6,S} {7,S} {11,S}
3  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {8,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {9,S} {16,S} {17,S}
6  C u0 p0 c0 {2,S} {8,D} {19,S}
7  C u0 p0 c0 {2,S} {9,D} {20,S}
8  C u0 p0 c0 {4,S} {6,D} {18,S}
9  C u0 p0 c0 {5,S} {7,D} {21,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([138.541,188.675,232.836,269.572,327.327,369.029,427.859],'J/(mol*K)'),
        H298 = (130.105,'kJ/mol'),
        S298 = (350.852,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 107,
    label = "s2_5_6_diene_2_5",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {8,S} {15,S} {16,S}
4  C u0 p0 c0 {2,S} {7,S} {13,S} {14,S}
5  C u0 p0 c0 {6,S} {9,S} {17,S} {18,S}
6  C u0 p0 c0 {1,S} {5,S} {7,D}
7  C u0 p0 c0 {4,S} {6,D} {19,S}
8  C u0 p0 c0 {3,S} {9,D} {20,S}
9  C u0 p0 c0 {5,S} {8,D} {21,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([141.242,189.906,232.742,269.201,327.138,368.965,427.948],'J/(mol*K)'),
        H298 = (122.85,'kJ/mol'),
        S298 = (360.659,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 108,
    label = "s2_5_6_diene_2_6",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {10,S}
2  C u0 p0 c0 {1,S} {5,S} {6,S} {11,S}
3  C u0 p0 c0 {1,S} {7,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {8,S} {14,S} {15,S}
5  C u0 p0 c0 {2,S} {9,S} {16,S} {17,S}
6  C u0 p0 c0 {2,S} {7,D} {18,S}
7  C u0 p0 c0 {3,S} {6,D} {19,S}
8  C u0 p0 c0 {4,S} {9,D} {20,S}
9  C u0 p0 c0 {5,S} {8,D} {21,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([138.471,188.845,233.08,269.78,327.493,369.189,428.076],'J/(mol*K)'),
        H298 = (134.882,'kJ/mol'),
        S298 = (348.073,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 109,
    label = "s2_5_6_diene_5_7",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {4,S} {13,S} {14,S}
4  C u0 p0 c0 {3,S} {5,S} {15,S} {16,S}
5  C u0 p0 c0 {4,S} {6,S} {17,S} {18,S}
6  C u0 p0 c0 {1,S} {5,S} {8,D}
7  C u0 p0 c0 {1,S} {9,D} {19,S}
8  C u0 p0 c0 {6,D} {9,S} {20,S}
9  C u0 p0 c0 {7,D} {8,S} {21,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([138.882,189.134,233.253,269.879,327.493,369.107,427.871],'J/(mol*K)'),
        H298 = (105.85,'kJ/mol'),
        S298 = (349.305,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 110,
    label = "s2_5_6_diene_5_8",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {7,S} {14,S} {15,S}
4  C u0 p0 c0 {2,S} {6,S} {16,S} {17,S}
5  C u0 p0 c0 {8,S} {9,S} {18,S} {19,S}
6  C u0 p0 c0 {4,S} {7,S} {8,D}
7  C u0 p0 c0 {3,S} {6,S} {9,D}
8  C u0 p0 c0 {5,S} {6,D} {20,S}
9  C u0 p0 c0 {5,S} {7,D} {21,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([141.569,191.019,234.218,270.441,327.859,369.361,428.055],'J/(mol*K)'),
        H298 = (103.216,'kJ/mol'),
        S298 = (349.138,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 111,
    label = "s2_6_6_ane",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {5,S} {12,S}
3  C u0 p0 c0 {1,S} {7,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {8,S} {19,S} {20,S}
5  C u0 p0 c0 {2,S} {9,S} {21,S} {22,S}
6  C u0 p0 c0 {1,S} {10,S} {27,S} {28,S}
7  C u0 p0 c0 {3,S} {8,S} {15,S} {16,S}
8  C u0 p0 c0 {4,S} {7,S} {17,S} {18,S}
9  C u0 p0 c0 {5,S} {10,S} {23,S} {24,S}
10 C u0 p0 c0 {6,S} {9,S} {25,S} {26,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {7,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {8,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {9,S}
25 H u0 p0 c0 {10,S}
26 H u0 p0 c0 {10,S}
27 H u0 p0 c0 {6,S}
28 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([172.31,236.623,294.419,344.561,424.926,483.66,568.259],'J/(mol*K)'),
        H298 = (-148.58,'kJ/mol'),
        S298 = (373.269,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 112,
    label = "s2_6_6_ene_0",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {9,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {6,S} {20,S} {21,S}
4  C u0 p0 c0 {2,S} {5,S} {14,S} {15,S}
5  C u0 p0 c0 {4,S} {7,S} {16,S} {17,S}
6  C u0 p0 c0 {3,S} {8,S} {18,S} {19,S}
7  C u0 p0 c0 {5,S} {9,S} {22,S} {23,S}
8  C u0 p0 c0 {6,S} {10,S} {24,S} {25,S}
9  C u0 p0 c0 {1,S} {7,S} {10,D}
10 C u0 p0 c0 {8,S} {9,D} {26,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([165.61,225.362,278.614,324.707,398.388,452.025,528.793],'J/(mol*K)'),
        H298 = (-33.8172,'kJ/mol'),
        S298 = (376.704,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 113,
    label = "s2_6_6_ene_1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {12,S}
3  C u0 p0 c0 {1,S} {6,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {7,S} {19,S} {20,S}
5  C u0 p0 c0 {1,S} {8,S} {21,S} {22,S}
6  C u0 p0 c0 {3,S} {7,S} {15,S} {16,S}
7  C u0 p0 c0 {4,S} {6,S} {17,S} {18,S}
8  C u0 p0 c0 {5,S} {10,S} {23,S} {24,S}
9  C u0 p0 c0 {2,S} {10,D} {25,S}
10 C u0 p0 c0 {8,S} {9,D} {26,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {7,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {5,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {9,S}
26 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([166.383,228.112,282.398,328.196,401.092,454.072,529.75],'J/(mol*K)'),
        H298 = (195.28,'kJ/mol'),
        S298 = (371.392,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 114,
    label = "s2_6_6_ene_2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {8,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {12,S}
3  C u0 p0 c0 {1,S} {5,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {6,S} {19,S} {20,S}
5  C u0 p0 c0 {3,S} {6,S} {15,S} {16,S}
6  C u0 p0 c0 {4,S} {5,S} {17,S} {18,S}
7  C u0 p0 c0 {2,S} {9,S} {21,S} {22,S}
8  C u0 p0 c0 {1,S} {10,S} {23,S} {24,S}
9  C u0 p0 c0 {7,S} {10,D} {25,S}
10 C u0 p0 c0 {8,S} {9,D} {26,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {8,S}
25 H u0 p0 c0 {9,S}
26 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([166.165,226.031,279.338,325.457,399.125,452.691,529.201],'J/(mol*K)'),
        H298 = (-31.6029,'kJ/mol'),
        S298 = (371.4,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 115,
    label = "s2_6_6_ene_m",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {6,S} {13,S} {14,S}
3  C u0 p0 c0 {4,S} {7,S} {15,S} {16,S}
4  C u0 p0 c0 {3,S} {8,S} {17,S} {18,S}
5  C u0 p0 c0 {1,S} {9,S} {19,S} {20,S}
6  C u0 p0 c0 {2,S} {10,S} {21,S} {22,S}
7  C u0 p0 c0 {3,S} {10,S} {23,S} {24,S}
8  C u0 p0 c0 {4,S} {9,S} {25,S} {26,S}
9  C u0 p0 c0 {5,S} {8,S} {10,D}
10 C u0 p0 c0 {6,S} {7,S} {9,D}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {8,S}
26 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([166.819,225.886,278.793,324.635,397.984,451.486,528.519],'J/(mol*K)'),
        H298 = (-41.0873,'kJ/mol'),
        S298 = (369.536,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 116,
    label = "s2_6_6_diene_m_1",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {3,S} {13,S} {14,S}
3  C u0 p0 c0 {2,S} {7,S} {21,S} {22,S}
4  C u0 p0 c0 {6,S} {7,S} {15,S} {16,S}
5  C u0 p0 c0 {1,S} {8,S} {19,S} {20,S}
6  C u0 p0 c0 {4,S} {9,S} {17,S} {18,S}
7  C u0 p0 c0 {3,S} {4,S} {8,D}
8  C u0 p0 c0 {5,S} {7,D} {10,S}
9  C u0 p0 c0 {6,S} {10,D} {23,S}
10 C u0 p0 c0 {8,S} {9,D} {24,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {3,S}
22 H u0 p0 c0 {3,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([160.86,215.789,264.362,306.263,372.921,421.131,489.651],'J/(mol*K)'),
        H298 = (70.8471,'kJ/mol'),
        S298 = (377.289,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 117,
    label = "s2_6_6_diene_m_2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {4,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {8,S} {15,S} {16,S}
4  C u0 p0 c0 {2,S} {7,S} {17,S} {18,S}
5  C u0 p0 c0 {7,S} {9,S} {19,S} {20,S}
6  C u0 p0 c0 {8,S} {10,S} {21,S} {22,S}
7  C u0 p0 c0 {4,S} {5,S} {8,D}
8  C u0 p0 c0 {3,S} {6,S} {7,D}
9  C u0 p0 c0 {5,S} {10,D} {23,S}
10 C u0 p0 c0 {6,S} {9,D} {24,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {6,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([160.847,215.627,264.064,305.889,372.538,420.854,489.725],'J/(mol*K)'),
        H298 = (68.9928,'kJ/mol'),
        S298 = (374.507,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 118,
    label = "s2_6_6_diene_0_2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {6,S} {7,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {4,S} {14,S} {15,S}
4  C u0 p0 c0 {3,S} {5,S} {16,S} {17,S}
5  C u0 p0 c0 {4,S} {7,S} {18,S} {19,S}
6  C u0 p0 c0 {1,S} {8,S} {20,S} {21,S}
7  C u0 p0 c0 {1,S} {5,S} {9,D}
8  C u0 p0 c0 {6,S} {10,D} {22,S}
9  C u0 p0 c0 {7,D} {10,S} {23,S}
10 C u0 p0 c0 {8,D} {9,S} {24,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([159.996,215.201,264.174,306.356,373.267,421.454,489.535],'J/(mol*K)'),
        H298 = (91.4821,'kJ/mol'),
        S298 = (374.47,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 119,
    label = "s2_6_6_diene_0_3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {9,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {12,S} {13,S}
3  C u0 p0 c0 {2,S} {4,S} {14,S} {15,S}
4  C u0 p0 c0 {3,S} {5,S} {16,S} {17,S}
5  C u0 p0 c0 {4,S} {7,S} {18,S} {19,S}
6  C u0 p0 c0 {8,S} {10,S} {20,S} {21,S}
7  C u0 p0 c0 {1,S} {5,S} {8,D}
8  C u0 p0 c0 {6,S} {7,D} {22,S}
9  C u0 p0 c0 {1,S} {10,D} {24,S}
10 C u0 p0 c0 {6,S} {9,D} {23,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {10,S}
24 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([158.853,214.836,263.983,305.994,372.89,421.309,489.935],'J/(mol*K)'),
        H298 = (74.7709,'kJ/mol'),
        S298 = (373.137,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 120,
    label = "s2_6_6_diene_0_4",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {11,S} {12,S}
2  C u0 p0 c0 {1,S} {4,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {8,S} {19,S} {20,S}
4  C u0 p0 c0 {2,S} {7,S} {21,S} {22,S}
5  C u0 p0 c0 {6,S} {9,S} {15,S} {16,S}
6  C u0 p0 c0 {5,S} {10,S} {17,S} {18,S}
7  C u0 p0 c0 {4,S} {8,S} {9,D}
8  C u0 p0 c0 {3,S} {7,S} {10,D}
9  C u0 p0 c0 {5,S} {7,D} {23,S}
10 C u0 p0 c0 {6,S} {8,D} {24,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {3,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([160.579,215.678,264.456,306.491,373.248,421.406,489.627],'J/(mol*K)'),
        H298 = (79.097,'kJ/mol'),
        S298 = (368.765,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 121,
    label = "s2_6_6_diene_0_5",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {11,S} {12,S}
2  C u0 p0 c0 {4,S} {6,S} {13,S} {14,S}
3  C u0 p0 c0 {1,S} {8,S} {17,S} {18,S}
4  C u0 p0 c0 {2,S} {7,S} {21,S} {22,S}
5  C u0 p0 c0 {1,S} {9,S} {15,S} {16,S}
6  C u0 p0 c0 {2,S} {10,S} {19,S} {20,S}
7  C u0 p0 c0 {4,S} {8,S} {9,D}
8  C u0 p0 c0 {3,S} {7,S} {10,D}
9  C u0 p0 c0 {5,S} {7,D} {23,S}
10 C u0 p0 c0 {6,S} {8,D} {24,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {4,S}
22 H u0 p0 c0 {4,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([159.587,214.666,263.569,305.725,372.678,420.984,489.414],'J/(mol*K)'),
        H298 = (59.6772,'kJ/mol'),
        S298 = (367.605,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 122,
    label = "s2_6_6_diene_0_6",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {9,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {14,S} {15,S}
3  C u0 p0 c0 {2,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {6,S} {7,S} {18,S} {19,S}
5  C u0 p0 c0 {3,S} {8,S} {20,S} {21,S}
6  C u0 p0 c0 {4,S} {10,S} {16,S} {17,S}
7  C u0 p0 c0 {1,S} {4,S} {8,D}
8  C u0 p0 c0 {5,S} {7,D} {24,S}
9  C u0 p0 c0 {1,S} {10,D} {22,S}
10 C u0 p0 c0 {6,S} {9,D} {23,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {5,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {10,S}
24 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([161.305,217.022,266.34,308.7,375.593,423.446,490.408],'J/(mol*K)'),
        H298 = (305.008,'kJ/mol'),
        S298 = (370.663,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 123,
    label = "s2_6_6_diene_0_7",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {7,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {14,S} {15,S}
3  C u0 p0 c0 {2,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {9,S} {16,S} {17,S}
5  C u0 p0 c0 {3,S} {8,S} {18,S} {19,S}
6  C u0 p0 c0 {7,S} {10,S} {20,S} {21,S}
7  C u0 p0 c0 {1,S} {6,S} {8,D}
8  C u0 p0 c0 {5,S} {7,D} {24,S}
9  C u0 p0 c0 {4,S} {10,D} {22,S}
10 C u0 p0 c0 {6,S} {9,D} {23,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {2,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {10,S}
24 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([159.659,214.82,263.805,306.016,373.014,421.305,489.598],'J/(mol*K)'),
        H298 = (86.0802,'kJ/mol'),
        S298 = (375.074,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 124,
    label = "s2_6_6_diene_0_8",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {16,S} {17,S}
3  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {6,S} {14,S} {15,S}
5  C u0 p0 c0 {3,S} {9,S} {18,S} {19,S}
6  C u0 p0 c0 {4,S} {8,S} {20,S} {21,S}
7  C u0 p0 c0 {1,S} {8,D} {10,S}
8  C u0 p0 c0 {6,S} {7,D} {23,S}
9  C u0 p0 c0 {5,S} {10,D} {22,S}
10 C u0 p0 c0 {7,S} {9,D} {24,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([158.774,214.782,263.941,305.929,372.79,421.191,489.813],'J/(mol*K)'),
        H298 = (74.7787,'kJ/mol'),
        S298 = (371.796,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 125,
    label = "s2_6_6_diene_1_3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {8,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {12,S}
3  C u0 p0 c0 {1,S} {5,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {6,S} {19,S} {20,S}
5  C u0 p0 c0 {3,S} {6,S} {15,S} {16,S}
6  C u0 p0 c0 {4,S} {5,S} {17,S} {18,S}
7  C u0 p0 c0 {2,S} {9,D} {21,S}
8  C u0 p0 c0 {1,S} {10,D} {22,S}
9  C u0 p0 c0 {7,D} {10,S} {23,S}
10 C u0 p0 c0 {8,D} {9,S} {24,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {4,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([158.028,215.083,265.015,306.999,373.637,421.859,490.184],'J/(mol*K)'),
        H298 = (83.2527,'kJ/mol'),
        S298 = (361.944,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 126,
    label = "s2_6_6_diene_1_6",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {7,S} {11,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {12,S}
3  C u0 p0 c0 {2,S} {5,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {6,S} {15,S} {16,S}
5  C u0 p0 c0 {3,S} {9,S} {17,S} {18,S}
6  C u0 p0 c0 {4,S} {10,S} {19,S} {20,S}
7  C u0 p0 c0 {1,S} {9,D} {21,S}
8  C u0 p0 c0 {2,S} {10,D} {23,S}
9  C u0 p0 c0 {5,S} {7,D} {22,S}
10 C u0 p0 c0 {6,S} {8,D} {24,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([158.155,214.677,264.281,306.3,373.109,421.449,489.917],'J/(mol*K)'),
        H298 = (87.529,'kJ/mol'),
        S298 = (364.082,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 127,
    label = "s2_6_6_diene_1_7",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {11,S}
2  C u0 p0 c0 {1,S} {5,S} {7,S} {12,S}
3  C u0 p0 c0 {1,S} {6,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {8,S} {15,S} {16,S}
5  C u0 p0 c0 {2,S} {9,S} {17,S} {18,S}
6  C u0 p0 c0 {3,S} {10,S} {19,S} {20,S}
7  C u0 p0 c0 {2,S} {10,D} {23,S}
8  C u0 p0 c0 {4,S} {9,D} {21,S}
9  C u0 p0 c0 {5,S} {8,D} {22,S}
10 C u0 p0 c0 {6,S} {7,D} {24,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {8,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {7,S}
24 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([160.84,219.855,270.293,311.796,377.345,424.629,491.383],'J/(mol*K)'),
        H298 = (540.304,'kJ/mol'),
        S298 = (363.762,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 128,
    label = "s2_6_6_diene_1_8",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {11,S}
2  C u0 p0 c0 {1,S} {7,S} {8,S} {12,S}
3  C u0 p0 c0 {1,S} {5,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {6,S} {15,S} {16,S}
5  C u0 p0 c0 {3,S} {9,S} {17,S} {18,S}
6  C u0 p0 c0 {4,S} {10,S} {19,S} {20,S}
7  C u0 p0 c0 {2,S} {9,D} {22,S}
8  C u0 p0 c0 {2,S} {10,D} {23,S}
9  C u0 p0 c0 {5,S} {7,D} {21,S}
10 C u0 p0 c0 {6,S} {8,D} {24,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {9,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {8,S}
24 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([157.891,214.648,264.443,306.479,373.252,421.563,489.983],'J/(mol*K)'),
        H298 = (90.5492,'kJ/mol'),
        S298 = (368.603,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 129,
    label = "s2_6_6_diene_2_7",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {11,S}
2  C u0 p0 c0 {1,S} {4,S} {5,S} {12,S}
3  C u0 p0 c0 {1,S} {7,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {8,S} {15,S} {16,S}
5  C u0 p0 c0 {2,S} {9,S} {17,S} {18,S}
6  C u0 p0 c0 {1,S} {10,S} {19,S} {20,S}
7  C u0 p0 c0 {3,S} {8,D} {21,S}
8  C u0 p0 c0 {4,S} {7,D} {22,S}
9  C u0 p0 c0 {5,S} {10,D} {23,S}
10 C u0 p0 c0 {6,S} {9,D} {24,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([165.305,219.914,267.707,308.95,374.637,422.225,490.073],'J/(mol*K)'),
        H298 = (104.797,'kJ/mol'),
        S298 = (385.827,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 130,
    label = "s3_4_4_ane",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
2  C u0 p0 c0 {3,S} {4,S} {5,S} {7,S}
3  C u0 p0 c0 {1,S} {2,S} {8,S} {9,S}
4  C u0 p0 c0 {1,S} {2,S} {10,S} {11,S}
5  C u0 p0 c0 {1,S} {2,S} {12,S} {13,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {5,S}
13 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([75.1309,106.126,135.018,159.145,194.818,220.521,257.222],'J/(mol*K)'),
        H298 = (208.948,'kJ/mol'),
        S298 = (260.826,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 131,
    label = "s3_4_4_ene_0",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
2  C u0 p0 c0 {1,S} {4,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
4  C u0 p0 c0 {2,S} {3,S} {5,D}
5  C u0 p0 c0 {1,S} {4,D} {11,S}
6  H u0 p0 c0 {1,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([76.0106,102.152,125.037,143.301,170.919,190.782,218.73],'J/(mol*K)'),
        H298 = (469.021,'kJ/mol'),
        S298 = (278.682,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 132,
    label = "s3_4_4_diene_0_2",
    molecule = 
"""
1 C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2 C u0 p0 c0 {1,S} {4,D} {5,S}
3 C u0 p0 c0 {1,S} {4,S} {5,D}
4 C u0 p0 c0 {2,D} {3,S} {8,S}
5 C u0 p0 c0 {2,S} {3,D} {9,S}
6 H u0 p0 c0 {1,S}
7 H u0 p0 c0 {1,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([67.2098,89.2816,108.373,123.154,144.502,159.492,179.702],'J/(mol*K)'),
        H298 = (636.349,'kJ/mol'),
        S298 = (265.133,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 133,
    label = "s3_4_5_ane",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {4,S} {5,S} {8,S}
3  C u0 p0 c0 {1,S} {2,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {2,S} {11,S} {12,S}
5  C u0 p0 c0 {2,S} {6,S} {13,S} {14,S}
6  C u0 p0 c0 {1,S} {5,S} {15,S} {16,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([92.9938,131.607,167.024,196.465,240.879,273.1,319.236],'J/(mol*K)'),
        H298 = (78.7028,'kJ/mol'),
        S298 = (288.094,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 134,
    label = "s3_4_5_ene_0",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {7,S}
2  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
3  C u0 p0 c0 {1,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
5  C u0 p0 c0 {2,S} {3,S} {6,D}
6  C u0 p0 c0 {4,S} {5,D} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([93.3955,126.881,155.58,180.028,218.152,244.893,281.122],'J/(mol*K)'),
        H298 = (544.561,'kJ/mol'),
        S298 = (293.859,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 135,
    label = "s3_4_5_ene_1",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {6,S} {7,S}
2  C u0 p0 c0 {3,S} {4,S} {5,S} {8,S}
3  C u0 p0 c0 {1,S} {2,S} {9,S} {10,S}
4  C u0 p0 c0 {1,S} {2,S} {11,S} {12,S}
5  C u0 p0 c0 {2,S} {6,D} {13,S}
6  C u0 p0 c0 {1,S} {5,D} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {3,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([87.0733,122.503,153.866,178.928,216.245,243.012,280.528],'J/(mol*K)'),
        H298 = (252.882,'kJ/mol'),
        S298 = (282.101,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 136,
    label = "s3_4_5_ene_3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {6,S} {7,S}
2  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
3  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {5,S} {12,S} {13,S}
5  C u0 p0 c0 {3,S} {4,S} {6,D}
6  C u0 p0 c0 {1,S} {5,D} {14,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([96.7138,129.204,158.062,181.798,218.254,244.51,281.46],'J/(mol*K)'),
        H298 = (415.428,'kJ/mol'),
        S298 = (307.376,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 137,
    label = "s3_4_5_diene_0_2",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {2,S} {5,D}
4  C u0 p0 c0 {1,S} {2,S} {6,D}
5  C u0 p0 c0 {3,D} {6,S} {11,S}
6  C u0 p0 c0 {4,D} {5,S} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([83.9458,114.022,139.793,159.972,190.344,211.952,241.718],'J/(mol*K)'),
        H298 = (495.078,'kJ/mol'),
        S298 = (282.337,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 138,
    label = "s3_4_5_diene_0_3",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {9,S} {10,S}
2  C u0 p0 c0 {3,S} {5,S} {7,S} {8,S}
3  C u0 p0 c0 {1,S} {2,S} {6,D}
4  C u0 p0 c0 {1,S} {5,D} {6,S}
5  C u0 p0 c0 {2,S} {4,D} {11,S}
6  C u0 p0 c0 {3,D} {4,S} {12,S}
7  H u0 p0 c0 {2,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([94.8636,120.823,143.414,162.639,192.577,213.551,242.057],'J/(mol*K)'),
        H298 = (534.629,'kJ/mol'),
        S298 = (306.9,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 139,
    label = "s3_4_5_diene_1_3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {5,S} {7,S}
2  C u0 p0 c0 {1,S} {3,S} {8,S} {9,S}
3  C u0 p0 c0 {2,S} {4,D} {6,S}
4  C u0 p0 c0 {1,S} {3,D} {10,S}
5  C u0 p0 c0 {1,S} {6,D} {11,S}
6  C u0 p0 c0 {3,S} {5,D} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([86.2857,116.148,141.757,161.828,191.854,213.145,242.309],'J/(mol*K)'),
        H298 = (525.059,'kJ/mol'),
        S298 = (292.328,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 140,
    label = "s3_4_5_diene_3_4",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {5,D} {6,S}
4  C u0 p0 c0 {2,S} {5,S} {6,D}
5  C u0 p0 c0 {3,D} {4,S} {11,S}
6  C u0 p0 c0 {3,S} {4,D} {12,S}
7  H u0 p0 c0 {1,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {5,S}
12 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([88.2955,117.447,142.342,161.981,191.779,212.98,242.198],'J/(mol*K)'),
        H298 = (609.658,'kJ/mol'),
        S298 = (289.452,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 141,
    label = "s3_4_6_ane",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {6,S} {8,S}
2  C u0 p0 c0 {3,S} {4,S} {5,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {2,S} {12,S} {13,S}
5  C u0 p0 c0 {2,S} {7,S} {14,S} {15,S}
6  C u0 p0 c0 {1,S} {7,S} {18,S} {19,S}
7  C u0 p0 c0 {5,S} {6,S} {16,S} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {7,S}
17 H u0 p0 c0 {7,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([112.937,157.806,198.769,233.187,286.449,325.323,381.298],'J/(mol*K)'),
        H298 = (39.2147,'kJ/mol'),
        S298 = (316.266,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 142,
    label = "s3_4_6_ene_0",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
2  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {6,S} {13,S} {14,S}
5  C u0 p0 c0 {2,S} {7,S} {15,S} {16,S}
6  C u0 p0 c0 {3,S} {4,S} {7,D}
7  C u0 p0 c0 {5,S} {6,D} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([108.423,149.733,185.228,215.544,263.026,296.559,342.517],'J/(mol*K)'),
        H298 = (336.095,'kJ/mol'),
        S298 = (307.767,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 143,
    label = "s3_4_6_ene_1",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {5,S} {8,S}
2  C u0 p0 c0 {3,S} {4,S} {6,S} {9,S}
3  C u0 p0 c0 {1,S} {2,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {2,S} {12,S} {13,S}
5  C u0 p0 c0 {1,S} {7,S} {14,S} {15,S}
6  C u0 p0 c0 {2,S} {7,D} {16,S}
7  C u0 p0 c0 {5,S} {6,D} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {5,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {6,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([105.487,147.26,184.372,214.655,261.086,294.694,342.394],'J/(mol*K)'),
        H298 = (149.029,'kJ/mol'),
        S298 = (307.914,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 144,
    label = "s3_4_6_ene_4",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {7,S} {8,S}
2  C u0 p0 c0 {1,S} {3,S} {9,S} {10,S}
3  C u0 p0 c0 {2,S} {5,S} {11,S} {12,S}
4  C u0 p0 c0 {1,S} {6,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {6,S} {15,S} {16,S}
6  C u0 p0 c0 {4,S} {5,S} {7,D}
7  C u0 p0 c0 {1,S} {6,D} {17,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([108.883,150.224,186.685,216.438,262.409,295.681,342.903],'J/(mol*K)'),
        H298 = (337.077,'kJ/mol'),
        S298 = (312.383,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 145,
    label = "s3_4_6_diene_0_2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {3,S} {6,D}
5  C u0 p0 c0 {1,S} {7,D} {13,S}
6  C u0 p0 c0 {4,D} {7,S} {14,S}
7  C u0 p0 c0 {5,D} {6,S} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([102.117,140.489,172.93,198.438,237.62,265.581,304.335],'J/(mol*K)'),
        H298 = (485.231,'kJ/mol'),
        S298 = (304.279,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 146,
    label = "s3_4_6_diene_0_3",
    molecule = 
"""
1  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
2  C u0 p0 c0 {4,S} {5,S} {12,S} {13,S}
3  C u0 p0 c0 {6,S} {7,S} {10,S} {11,S}
4  C u0 p0 c0 {1,S} {2,S} {6,D}
5  C u0 p0 c0 {1,S} {2,S} {7,D}
6  C u0 p0 c0 {3,S} {4,D} {14,S}
7  C u0 p0 c0 {3,S} {5,D} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {1,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([101.745,137.827,168.735,195.042,236.005,264.66,303.233],'J/(mol*K)'),
        H298 = (343.735,'kJ/mol'),
        S298 = (306.28,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 147,
    label = "s3_4_6_diene_0_4",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {6,S} {8,S} {9,S}
3  C u0 p0 c0 {4,S} {5,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {3,S} {7,D}
5  C u0 p0 c0 {3,S} {6,D} {7,S}
6  C u0 p0 c0 {2,S} {5,D} {14,S}
7  C u0 p0 c0 {4,D} {5,S} {15,S}
8  H u0 p0 c0 {2,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([112.439,145.774,174.828,199.625,238.43,265.833,303.626],'J/(mol*K)'),
        H298 = (389.182,'kJ/mol'),
        S298 = (323.797,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 148,
    label = "s3_4_6_diene_1_4",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {6,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {4,S} {7,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {3,S} {5,D}
5  C u0 p0 c0 {1,S} {4,D} {13,S}
6  C u0 p0 c0 {1,S} {7,D} {14,S}
7  C u0 p0 c0 {3,S} {6,D} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([101.379,139.713,172.293,197.953,237.269,265.339,304.257],'J/(mol*K)'),
        H298 = (461.232,'kJ/mol'),
        S298 = (303.8,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 149,
    label = "s3_4_6_diene_1_5",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {8,S}
2  C u0 p0 c0 {1,S} {4,S} {9,S} {10,S}
3  C u0 p0 c0 {1,S} {6,S} {11,S} {12,S}
4  C u0 p0 c0 {2,S} {5,D} {7,S}
5  C u0 p0 c0 {1,S} {4,D} {13,S}
6  C u0 p0 c0 {3,S} {7,D} {14,S}
7  C u0 p0 c0 {4,S} {6,D} {15,S}
8  H u0 p0 c0 {1,S}
9  H u0 p0 c0 {2,S}
10 H u0 p0 c0 {2,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {5,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([102.174,140.007,172.296,197.887,237.198,265.302,304.344],'J/(mol*K)'),
        H298 = (487.574,'kJ/mol'),
        S298 = (305.668,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 150,
    label = "s3_6_6_ane",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {7,S} {10,S}
2  C u0 p0 c0 {3,S} {5,S} {6,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {18,S} {19,S}
4  C u0 p0 c0 {1,S} {8,S} {12,S} {13,S}
5  C u0 p0 c0 {2,S} {8,S} {16,S} {17,S}
6  C u0 p0 c0 {2,S} {9,S} {20,S} {21,S}
7  C u0 p0 c0 {1,S} {9,S} {24,S} {25,S}
8  C u0 p0 c0 {4,S} {5,S} {14,S} {15,S}
9  C u0 p0 c0 {6,S} {7,S} {22,S} {23,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {8,S}
15 H u0 p0 c0 {8,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {6,S}
22 H u0 p0 c0 {9,S}
23 H u0 p0 c0 {9,S}
24 H u0 p0 c0 {7,S}
25 H u0 p0 c0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([147.85,206.354,259.527,304.744,376.399,428.886,504.77],'J/(mol*K)'),
        H298 = (-94.4323,'kJ/mol'),
        S298 = (345.41,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 151,
    label = "s3_6_6_ene_0",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {5,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {7,S} {15,S} {16,S}
4  C u0 p0 c0 {2,S} {6,S} {13,S} {14,S}
5  C u0 p0 c0 {1,S} {8,S} {19,S} {20,S}
6  C u0 p0 c0 {4,S} {8,S} {17,S} {18,S}
7  C u0 p0 c0 {3,S} {9,S} {21,S} {22,S}
8  C u0 p0 c0 {5,S} {6,S} {9,D}
9  C u0 p0 c0 {7,S} {8,D} {23,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {6,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {5,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([144.058,199.959,249.155,289.866,353.924,400.469,466.944],'J/(mol*K)'),
        H298 = (227.417,'kJ/mol'),
        S298 = (344.823,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 152,
    label = "s3_6_6_ene_1",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {7,S} {10,S}
2  C u0 p0 c0 {3,S} {5,S} {8,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {18,S} {19,S}
4  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
5  C u0 p0 c0 {2,S} {6,S} {16,S} {17,S}
6  C u0 p0 c0 {4,S} {5,S} {14,S} {15,S}
7  C u0 p0 c0 {1,S} {9,S} {20,S} {21,S}
8  C u0 p0 c0 {2,S} {9,D} {22,S}
9  C u0 p0 c0 {7,S} {8,D} {23,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {4,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {6,S}
15 H u0 p0 c0 {6,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {3,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {8,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([142.456,197.394,246.431,287.45,352.028,399.035,466.307],'J/(mol*K)'),
        H298 = (22.3156,'kJ/mol'),
        S298 = (346.809,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 153,
    label = "s3_6_6_ene_4",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {9,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {5,S} {17,S} {18,S}
4  C u0 p0 c0 {2,S} {6,S} {13,S} {14,S}
5  C u0 p0 c0 {3,S} {7,S} {15,S} {16,S}
6  C u0 p0 c0 {4,S} {8,S} {19,S} {20,S}
7  C u0 p0 c0 {5,S} {8,S} {21,S} {22,S}
8  C u0 p0 c0 {6,S} {7,S} {9,D}
9  C u0 p0 c0 {1,S} {8,D} {23,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {3,S}
18 H u0 p0 c0 {3,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {6,S}
21 H u0 p0 c0 {7,S}
22 H u0 p0 c0 {7,S}
23 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([155.304,207.986,254.525,294.561,357.981,403.581,468.023],'J/(mol*K)'),
        H298 = (399.764,'kJ/mol'),
        S298 = (362.887,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 154,
    label = "s3_6_6_diene_0_m",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {7,S} {14,S} {15,S}
4  C u0 p0 c0 {5,S} {6,S} {18,S} {19,S}
5  C u0 p0 c0 {4,S} {8,S} {16,S} {17,S}
6  C u0 p0 c0 {2,S} {4,S} {9,D}
7  C u0 p0 c0 {3,S} {8,D} {9,S}
8  C u0 p0 c0 {5,S} {7,D} {20,S}
9  C u0 p0 c0 {6,D} {7,S} {21,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([140.424,192.88,237.523,273.728,330.546,371.438,428.944],'J/(mol*K)'),
        H298 = (524.48,'kJ/mol'),
        S298 = (341.251,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 155,
    label = "s3_6_6_diene_0_2",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {4,S} {7,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {5,S} {13,S} {14,S}
4  C u0 p0 c0 {1,S} {6,S} {17,S} {18,S}
5  C u0 p0 c0 {3,S} {6,S} {15,S} {16,S}
6  C u0 p0 c0 {4,S} {5,S} {8,D}
7  C u0 p0 c0 {1,S} {9,D} {19,S}
8  C u0 p0 c0 {6,D} {9,S} {20,S}
9  C u0 p0 c0 {7,D} {8,S} {21,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {5,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {4,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([136.404,188.02,232.942,269.722,327.3,368.897,427.703],'J/(mol*K)'),
        H298 = (208.295,'kJ/mol'),
        S298 = (340.227,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 156,
    label = "s3_6_6_diene_0_3",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {10,S} {11,S}
2  C u0 p0 c0 {1,S} {6,S} {12,S} {13,S}
3  C u0 p0 c0 {1,S} {7,S} {14,S} {15,S}
4  C u0 p0 c0 {6,S} {7,S} {18,S} {19,S}
5  C u0 p0 c0 {8,S} {9,S} {16,S} {17,S}
6  C u0 p0 c0 {2,S} {4,S} {8,D}
7  C u0 p0 c0 {3,S} {4,S} {9,D}
8  C u0 p0 c0 {5,S} {6,D} {20,S}
9  C u0 p0 c0 {5,S} {7,D} {21,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {1,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {4,S}
19 H u0 p0 c0 {4,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([137.815,190.235,235.049,271.432,328.55,369.744,427.9],'J/(mol*K)'),
        H298 = (274.213,'kJ/mol'),
        S298 = (338.854,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 157,
    label = "s3_6_6_diene_0_4",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {7,S} {12,S} {13,S}
2  C u0 p0 c0 {4,S} {6,S} {16,S} {17,S}
3  C u0 p0 c0 {1,S} {8,S} {10,S} {11,S}
4  C u0 p0 c0 {2,S} {9,S} {14,S} {15,S}
5  C u0 p0 c0 {6,S} {7,S} {18,S} {19,S}
6  C u0 p0 c0 {2,S} {5,S} {8,D}
7  C u0 p0 c0 {1,S} {5,S} {9,D}
8  C u0 p0 c0 {3,S} {6,D} {20,S}
9  C u0 p0 c0 {4,S} {7,D} {21,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {1,S}
13 H u0 p0 c0 {1,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {2,S}
17 H u0 p0 c0 {2,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {5,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([138.606,190.592,235.136,271.428,328.474,369.647,427.845],'J/(mol*K)'),
        H298 = (254.306,'kJ/mol'),
        S298 = (335.01,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 158,
    label = "s3_6_6_diene_0_5",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {7,S} {10,S}
2  C u0 p0 c0 {1,S} {4,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {6,S} {13,S} {14,S}
4  C u0 p0 c0 {2,S} {8,S} {15,S} {16,S}
5  C u0 p0 c0 {6,S} {9,S} {17,S} {18,S}
6  C u0 p0 c0 {3,S} {5,S} {8,D}
7  C u0 p0 c0 {1,S} {9,D} {19,S}
8  C u0 p0 c0 {4,S} {6,D} {21,S}
9  C u0 p0 c0 {5,S} {7,D} {20,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {9,S}
21 H u0 p0 c0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([136.2,188.041,233.095,269.898,327.438,368.989,427.696],'J/(mol*K)'),
        H298 = (183.463,'kJ/mol'),
        S298 = (340.013,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 159,
    label = "s3_6_6_diene_0_6",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {3,S} {4,S} {10,S}
2  C u0 p0 c0 {1,S} {5,S} {11,S} {12,S}
3  C u0 p0 c0 {1,S} {6,S} {15,S} {16,S}
4  C u0 p0 c0 {1,S} {8,S} {13,S} {14,S}
5  C u0 p0 c0 {2,S} {7,S} {17,S} {18,S}
6  C u0 p0 c0 {3,S} {7,D} {9,S}
7  C u0 p0 c0 {5,S} {6,D} {20,S}
8  C u0 p0 c0 {4,S} {9,D} {19,S}
9  C u0 p0 c0 {6,S} {8,D} {21,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {4,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {3,S}
16 H u0 p0 c0 {3,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([137.327,190.207,235.037,271.323,328.38,369.513,427.586],'J/(mol*K)'),
        H298 = (463.449,'kJ/mol'),
        S298 = (336.864,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 160,
    label = "s3_6_6_diene_1_m",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {7,S} {8,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {13,S} {14,S}
3  C u0 p0 c0 {2,S} {4,S} {11,S} {12,S}
4  C u0 p0 c0 {3,S} {6,S} {15,S} {16,S}
5  C u0 p0 c0 {6,S} {9,S} {17,S} {18,S}
6  C u0 p0 c0 {4,S} {5,S} {7,D}
7  C u0 p0 c0 {1,S} {6,D} {19,S}
8  C u0 p0 c0 {1,S} {9,D} {20,S}
9  C u0 p0 c0 {5,S} {8,D} {21,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {3,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {2,S}
14 H u0 p0 c0 {2,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([141.243,191.787,235.693,271.961,329.055,370.245,428.351],'J/(mol*K)'),
        H298 = (360.047,'kJ/mol'),
        S298 = (350.464,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 161,
    label = "s3_6_6_diene_1_5",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {5,S} {6,S} {10,S}
2  C u0 p0 c0 {3,S} {4,S} {7,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {12,S} {13,S}
4  C u0 p0 c0 {2,S} {8,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {9,S} {16,S} {17,S}
6  C u0 p0 c0 {1,S} {8,D} {18,S}
7  C u0 p0 c0 {2,S} {9,D} {20,S}
8  C u0 p0 c0 {4,S} {6,D} {19,S}
9  C u0 p0 c0 {5,S} {7,D} {21,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {6,S}
19 H u0 p0 c0 {8,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([135.25,186.449,231.405,268.413,326.287,368.145,427.39],'J/(mol*K)'),
        H298 = (112.133,'kJ/mol'),
        S298 = (334.768,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 162,
    label = "s3_6_6_diene_1_6",
    molecule = 
"""
1  C u0 p0 c0 {3,S} {4,S} {5,S} {10,S}
2  C u0 p0 c0 {3,S} {6,S} {7,S} {11,S}
3  C u0 p0 c0 {1,S} {2,S} {12,S} {13,S}
4  C u0 p0 c0 {1,S} {8,S} {14,S} {15,S}
5  C u0 p0 c0 {1,S} {9,S} {16,S} {17,S}
6  C u0 p0 c0 {2,S} {8,D} {19,S}
7  C u0 p0 c0 {2,S} {9,D} {20,S}
8  C u0 p0 c0 {4,S} {6,D} {18,S}
9  C u0 p0 c0 {5,S} {7,D} {21,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {3,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {4,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {5,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {8,S}
19 H u0 p0 c0 {6,S}
20 H u0 p0 c0 {7,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([136.392,186.883,231.448,268.388,326.264,368.114,427.316],'J/(mol*K)'),
        H298 = (127.372,'kJ/mol'),
        S298 = (348.443,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 163,
    label = "s3_6_6_diene_1_8",
    molecule = 
"""
1  C u0 p0 c0 {2,S} {5,S} {7,S} {10,S}
2  C u0 p0 c0 {1,S} {3,S} {11,S} {12,S}
3  C u0 p0 c0 {2,S} {4,S} {13,S} {14,S}
4  C u0 p0 c0 {3,S} {6,S} {15,S} {16,S}
5  C u0 p0 c0 {1,S} {8,S} {17,S} {18,S}
6  C u0 p0 c0 {4,S} {7,D} {9,S}
7  C u0 p0 c0 {1,S} {6,D} {19,S}
8  C u0 p0 c0 {5,S} {9,D} {20,S}
9  C u0 p0 c0 {6,S} {8,D} {21,S}
10 H u0 p0 c0 {1,S}
11 H u0 p0 c0 {2,S}
12 H u0 p0 c0 {2,S}
13 H u0 p0 c0 {3,S}
14 H u0 p0 c0 {3,S}
15 H u0 p0 c0 {4,S}
16 H u0 p0 c0 {4,S}
17 H u0 p0 c0 {5,S}
18 H u0 p0 c0 {5,S}
19 H u0 p0 c0 {7,S}
20 H u0 p0 c0 {8,S}
21 H u0 p0 c0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([138.34,189.873,234.509,271.047,328.349,369.713,428.127],'J/(mol*K)'),
        H298 = (323.956,'kJ/mol'),
        S298 = (342.812,'J/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

