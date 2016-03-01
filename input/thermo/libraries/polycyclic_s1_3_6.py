#!/usr/bin/env python
# encoding: utf-8

name = "s1_3_6"
shortDesc = u"Calculation by mopac pm7 method"
longDesc = u"""

"""
entry(
    index = 1,
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
        Cpdata = ([135.752,187.564,236.803,280.543,346.172,386.401,452.264],'J/(mol*K)'),
        H298 = (-25.4166,'kJ/mol'),
        S298 = (350.061,'J/(mol*K)'),
    ),
    shortDesc = u"""QM MopacMolPM7 calculation attempt 1""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
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
        Cpdata = ([129.785,176.594,220.68,259.623,317.809,353.43,411.731],'J/(mol*K)'),
        H298 = (76.2843,'kJ/mol'),
        S298 = (354.388,'J/(mol*K)'),
    ),
    shortDesc = u"""QM MopacMolPM7 calculation attempt 1""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
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
        Cpdata = ([129.69,176.529,220.654,259.631,317.848,353.462,411.763],'J/(mol*K)'),
        H298 = (76.1668,'kJ/mol'),
        S298 = (352.996,'J/(mol*K)'),
    ),
    shortDesc = u"""QM MopacMolPM7 calculation attempt 1""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
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
        Cpdata = ([123.314,165.149,204.155,238.378,289.217,320.255,371.111],'J/(mol*K)'),
        H298 = (175.135,'kJ/mol'),
        S298 = (344.308,'J/(mol*K)'),
    ),
    shortDesc = u"""QM MopacMolPM7 calculation attempt 1""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
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
        Cpdata = ([122.949,164.863,203.976,238.3,289.247,320.28,371.142],'J/(mol*K)'),
        H298 = (174.883,'kJ/mol'),
        S298 = (349.015,'J/(mol*K)'),
    ),
    shortDesc = u"""QM MopacMolPM7 calculation attempt 1""",
    longDesc = 
u"""

""",
)

