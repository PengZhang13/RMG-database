#!/usr/bin/env python
# encoding: utf-8

name = "Other Corrections"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 0,
    label = "R",
    group = 
"""
1 * R u0
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""dummy root""",
    longDesc = 
u"""

""",
)

entry(
    index = 1,
    label = "ortho",
    group = 
"""
1 *1 Cb u0 {2,B}
2 *2 Cb u0 {1,B}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""Root for Aromatics NNI correction.""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "o_OH_CHO",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {5,S}
3    O u0 {1,S} {4,S}
4    H u0 {3,S}
5    C u0 {2,S} {6,S} {7,D}
6    H u0 {5,S}
7    O u0 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.49, -2.15, -1.77, -1.43, -0.81, -0.33, 0.43],'cal/(mol*K)'),
        H298 = (-6.55,'kcal/mol'),
        S298 = (-5.09,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "o_CHO_CHO",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {5,S}
3    C u0 {1,S} {4,S} {8,D}
4    H u0 {3,S}
5    C u0 {2,S} {6,S} {7,D}
6    H u0 {5,S}
7    O u0 {5,D}
8    O u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.20, 0.20, 0.19, 0.17, 0.05, -0.10, -0.30],'cal/(mol*K)'),
        H298 = (2.52,'kcal/mol'),
        S298 = (0.76,'cal/(mol*K)'),
    ),
    shortDesc = u"""Half value. This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "o_MeO_MeO",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {8,S}
3    O u0 {1,S} {4,S}
4    C u0 {3,S} {5,S} {6,S} {7,S}
5    H u0 {4,S}
6    H u0 {4,S}
7    H u0 {4,S}
8    O u0 {2,S} {9,S}
9    C u0 {8,S} {10,S} {11,S} {12,S}
10   H u0 {9,S}
11   H u0 {9,S}
12   H u0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.00, -0.41, -0.56, -0.60, -0.53, -0.44, -0.26],'cal/(mol*K)'),
        H298 = (1.76,'kcal/mol'),
        S298 = (0.93,'cal/(mol*K)'),
    ),
    shortDesc = u"""Half value. This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "o_CHO_vinyl",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {6,S}
3    C u0 {1,S} {4,S} {5,D}
4    H u0 {3,S}
5    O u0 {3,D}
6    C u0 {2,S} {7,D} {8,S}
7    C u0 {6,D} {9,S} {10,S}
8    H u0 {6,S}
9    H u0 {7,S}
10   H u0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.31, 0.38, 0.50, 0.60, 0.57, 0.43, 0.07],'cal/(mol*K)'),
        H298 = (2.84,'kcal/mol'),
        S298 = (-0.62,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "o_vinyl_vinyl",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {6,S}
3    C u0 {1,S} {4,S} {5,D}
4    H u0 {3,S}
5    C u0 {3,D} {11,S} {12,S}
6    C u0 {2,S} {7,D} {8,S}
7    C u0 {6,D} {9,S} {10,S}
8    H u0 {6,S}
9    H u0 {7,S}
10   H u0 {7,S}
11   H u0 {5,S}
12   H u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.55, 0.38, 0.25, 0.16, 0.02, -0.02, -0.06],'cal/(mol*K)'),
        H298 = (0.97,'kcal/mol'),
        S298 = (-0.27,'cal/(mol*K)'),
    ),
    shortDesc = u"""Half value. This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "o_CHO_CH3",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {6,S}
3    C u0 {1,S} {4,S} {5,D}
4    H u0 {3,S}
5    O u0 {3,D}
6    C u0 {2,S} {7,S} {8,S} {9,S}
7    H u0 {6,S}
8    H u0 {6,S}
9    H u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.96, 0.72, 0.48, 0.26, 0.00, -0.14, -0.22],'cal/(mol*K)'),
        H298 = (1.94,'kcal/mol'),
        S298 = (-0.57,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "o_CHO_C2H5",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {6,S}
3    C u0 {1,S} {4,S} {5,D}
4    H u0 {3,S}
5    O u0 {3,D}
6    C u0 {2,S} {7,S} {8,S} {9,S}
7    H u0 {6,S}
8    H u0 {6,S}
9    C u0 {6,S} {10,S} {11,S} {12,S}
10    H u0 {9,S}
11    H u0 {9,S}
12    H u0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.96, 0.72, 0.48, 0.26, 0.00, -0.14, -0.22],'cal/(mol*K)'),
        H298 = (1.94,'kcal/mol'),
        S298 = (-0.57,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "o_vinyl_CH3",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {8,S}
3    C u0 {1,S} {4,S} {5,D}
4    H u0 {3,S}
5    C u0 {3,D} {6,S} {7,S}
6    H u0 {5,S}
7    H u0 {5,S}
8    C u0 {2,S} {9,S} {10,S} {11,S}
9    H u0 {8,S}
10   H u0 {8,S}
11   H u0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.36, 1.34, 1.17, 1.00, 0.69, 0.50, 0.24],'cal/(mol*K)'),
        H298 = (1.10,'kcal/mol'),
        S298 = (-1.36,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "o_vinyl_C2H5",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {8,S}
3    C u0 {1,S} {4,S} {5,D}
4    H u0 {3,S}
5    C u0 {3,D} {6,S} {7,S}
6    H u0 {5,S}
7    H u0 {5,S}
8    C u0 {2,S} {9,S} {10,S} {11,S}
9    H u0 {8,S}
10   H u0 {8,S}
11   C u0 {8,S} {12,S} {13,S} {14,S}
12   H u0 {11,S}
13   H u0 {11,S}
14   H u0 {11,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.36, 1.34, 1.17, 1.00, 0.69, 0.50, 0.24],'cal/(mol*K)'),
        H298 = (1.10,'kcal/mol'),
        S298 = (-1.36,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "o_CHO_MeO",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {6,S}
3    C u0 {1,S} {4,S} {5,D}
4    H u0 {3,S}
5    O u0 {3,D}
6    O u0 {2,S} {7,S}
7    C u0 {6,S} {8,S} {9,S} {10,S}
8    H u0 {7,S}
9    H u0 {7,S}
10   H u0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.62, 0.07, 0.62, 0.93, 0.98, 0.79, 0.31],'cal/(mol*K)'),
        H298 = (1.89,'kcal/mol'),
        S298 = (-0.41,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "o_CH3_CH3",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {7,S}
3    C u0 {1,S} {4,S} {5,S} {6,S}
4    H u0 {3,S}
5    H u0 {3,S}
6    H u0 {3,S}
7    C u0 {2,S} {8,S} {9,S} {10,S}
8    H u0 {7,S}
9    H u0 {7,S}
10    H u0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.39, 0.35, 0.31, 0.30, 0.27, 0.24, 0.18],'cal/(mol*K)'),
        H298 = (0.50,'kcal/mol'),
        S298 = (-0.79,'cal/(mol*K)'),
    ),
    shortDesc = u"""Half value. This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "o_CH3_C2H5",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {7,S}
3    C u0 {1,S} {4,S} {5,S} {6,S}
4    H u0 {3,S}
5    H u0 {3,S}
6    H u0 {3,S}
7    C u0 {2,S} {8,S} {9,S} {10,S}
8    H u0 {7,S}
9    H u0 {7,S}
10   C u0 {7,S} {11,S} {12,S} {13,S}
11   H u0 {10,S}
12   H u0 {10,S}
13   H u0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.79, 0.69, 0.62, 0.60, 0.55, 0.48, 0.36],'cal/(mol*K)'),
        H298 = (1.00,'kcal/mol'),
        S298 = (-1.58,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "o_C2H5_C2H5",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {7,S}
3    C u0 {1,S} {4,S} {5,S} {6,S}
4    H u0 {3,S}
5    H u0 {3,S}
6    C u0 {3,S} {14,S} {15,S} {16,S}
7    C u0 {2,S} {8,S} {9,S} {10,S}
8    H u0 {7,S}
9    H u0 {7,S}
10   C u0 {7,S} {11,S} {12,S} {13,S}
11   H u0 {10,S}
12   H u0 {10,S}
13   H u0 {10,S}
14   H u0 {6,S}
15   H u0 {6,S}
16   H u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.39, 0.35, 0.31, 0.30, 0.27, 0.24, 0.18],'cal/(mol*K)'),
        H298 = (0.50,'kcal/mol'),
        S298 = (-0.79,'cal/(mol*K)'),
    ),
    shortDesc = u"""Half value. This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "o_OH_OH",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {5,S}
3    O u0 {1,S} {4,S}
4    H u0 {3,S}
5    O u0 {2,S} {6,S}
6    H u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.32, -0.18, 0.02, 0.24, 0.50, 0.57, 0.44],'cal/(mol*K)'),
        H298 = (-0.36,'kcal/mol'),
        S298 = (-0.67,'cal/(mol*K)'),
    ),
    shortDesc = u"""Half value. This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    label = "o_OH_MeO",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {5,S}
3    O u0 {1,S} {4,S}
4    H u0 {3,S}
5    O u0 {2,S} {6,S}
6    C u0 {5,S} {7,S} {8,S} {9,S}
7    H u0 {6,S}
8    H u0 {6,S}
9    H u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.65, -0.36, 0.05, 0.48, 1.00, 1.15, 0.88],'cal/(mol*K)'),
        H298 = (-0.72,'kcal/mol'),
        S298 = (-1.34,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 17,
    label = "o_OH_vinyl",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {5,S}
3    O u0 {1,S} {4,S}
4    H u0 {3,S}
5    C u0 {2,S} {6,D} {7,S}
6    C u0 {5,D} {8,S} {9,S}
7    H u0 {5,S}
8    H u0 {6,S}
9    H u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.60, 0.65, 0.62, 0.60, 0.50, 0.43, 0.29],'cal/(mol*K)'),
        H298 = (0.62,'kcal/mol'),
        S298 = (-0.79,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
    label = "o_MeO_vinyl",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {5,S}
3    O u0 {1,S} {4,S}
4    C u0 {3,S} {10,S} {11,S} {12,S}
5    C u0 {2,S} {6,D} {7,S}
6    C u0 {5,D} {8,S} {9,S}
7    H u0 {5,S}
8    H u0 {6,S}
9    H u0 {6,S}
10    H u0 {4,S}
11    H u0 {4,S}
12    H u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.60, 0.65, 0.62, 0.60, 0.50, 0.43, 0.29],'cal/(mol*K)'),
        H298 = (0.62,'kcal/mol'),
        S298 = (-0.79,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 19,
    label = "meta",
    group = 
"""
1 *1 Cb u0 {2,B}
2    Cb u0 {1,B} {3,B}
3 *2 Cb u0 {2,B}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""Root for Aromatics NNI correction.""",
    longDesc = 
u"""

""",
)

entry(
    index = 20,
    label = "m_CHO_CHO",
    group = 
"""
1 *1 Cb u0 {2,B} {4,S}
2    Cb u0 {1,B} {3,B}
3 *2 Cb u0 {2,B} {7,S}
4    C  u0 {1,S} {5,D} {6,S}
5    O  u0 {4,D}
6    H  u0 {4,S}
7    C  u0 {3,S} {8,D} {9,S}
8    O  u0 {7,D}
9    H  u0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.20, 0.12, 0.06, 0.01, -0.05, -0.08, -0.10],'cal/(mol*K)'),
        H298 = (0.57,'kcal/mol'),
        S298 = (0.01,'cal/(mol*K)'),
    ),
    shortDesc = u"""Half value. Root for Aromatics NNI correction.""",
    longDesc = 
u"""

""",
)

entry(
    index = 21,
    label = "para",
    group = 
"""
1 *1 Cb u0 {2,B}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""Root for Aromatics NNI correction.""",
    longDesc = 
u"""

""",
)

entry(
    index = 22,
    label = "p_OH_OH",
    group = 
"""
1 *1 Cb u0 {2,B} {5,S}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B} {7,S}
5    O u0 {1,S} {6,S}
6    H u0 {5,S}
7    O u0 {4,S} {8,S}
8    H u0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.20, 0.05, -0.10, -0.20, -0.27, -0.27, -0.20],'cal/(mol*K)'),
        H298 = (0.87,'kcal/mol'),
        S298 = (0.48,'cal/(mol*K)'),
    ),
    shortDesc = u"""Half value. This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 23,
    label = "p_OH_MeO",
    group = 
"""
1 *1 Cb u0 {2,B} {5,S}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B} {7,S}
5    O u0 {1,S} {6,S}
6    H u0 {5,S}
7    O u0 {4,S} {8,S}
8    C u0 {7,S} {9,S} {10,S} {11,S}
9    H u0 {8,S}
10   H u0 {8,S}
11   H u0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.41, 0.10, -0.19, -0.41, -0.55, -0.55, -0.41],'cal/(mol*K)'),
        H298 = (1.74,'kcal/mol'),
        S298 = (0.96,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 24,
    label = "p_MeO_MeO",
    group = 
"""
1 *1 Cb u0 {2,B} {5,S}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B} {7,S}
5    O u0 {1,S} {6,S}
6    C u0 {5,S} {12,S} {13,S} {14,S}
7    O u0 {4,S} {8,S}
8    C u0 {7,S} {9,S} {10,S} {11,S}
9    H u0 {8,S}
10   H u0 {8,S}
11   H u0 {8,S}
12   H u0 {6,S}
13   H u0 {6,S}
14   H u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.20, 0.05, -0.10, -0.20, -0.27, -0.27, -0.20],'cal/(mol*K)'),
        H298 = (0.87,'kcal/mol'),
        S298 = (0.48,'cal/(mol*K)'),
    ),
    shortDesc = u"""Half value. This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 25,
    label = "p_CHO_CHO",
    group = 
"""
1 *1 Cb u0 {2,B} {5,S}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B} {7,S}
5    C u0 {1,S} {6,S} {10,D}
6    H u0 {5,S}
7    C u0 {4,S} {8,D} {9,S}
8    O u0 {7,D}
9    H u0 {7,S}
10   O u0 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.22, 0.17, 0.12, 0.08, 0.01, -0.04, -0.11],'cal/(mol*K)'),
        H298 = (1.18,'kcal/mol'),
        S298 = (-0.10,'cal/(mol*K)'),
    ),
    shortDesc = u"""Half value. This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 26,
    label = "p_OH_CHO",
    group = 
"""
1 *1 Cb u0 {2,B} {5,S}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B} {7,S}
5    O u0 {1,S} {6,S}
6    H u0 {5,S}
7    C u0 {4,S} {8,D} {9,S}
8    O u0 {7,D}
9    H u0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.38, -0.24, -0.07, 0.05, 0.22, 0.29, 0.36],'cal/(mol*K)'),
        H298 = (-1.10,'kcal/mol'),
        S298 = (-0.19,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

entry(
    index = 27,
    label = "p_MeO_CHO",
    group = 
"""
1 *1 Cb u0 {2,B} {5,S}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B} {7,S}
5    O u0 {1,S} {6,S}
6    C u0 {5,S} {10,S} {11,S} {12,S}
7    C u0 {4,S} {8,D} {9,S}
8    O u0 {7,D}
9    H u0 {7,S}
10   H u0 {6,S}
11   H u0 {6,S}
12   H u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.38, -0.24, -0.07, 0.05, 0.22, 0.29, 0.36],'cal/(mol*K)'),
        H298 = (-1.10,'kcal/mol'),
        S298 = (-0.19,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""

""",
)

tree(
"""
L1: R
    L2: ortho
        L3: o_OH_CHO
        L3: o_CHO_CHO
        L3: o_MeO_MeO
        L3: o_CHO_vinyl
        L3: o_vinyl_vinyl
        L3: o_CHO_CH3
        L3: o_CHO_C2H5
        L3: o_vinyl_CH3
        L3: o_vinyl_C2H5
        L3: o_CHO_MeO
        L3: o_CH3_CH3
        L3: o_CH3_C2H5
        L3: o_C2H5_C2H5
        L3: o_OH_OH
        L3: o_OH_MeO
        L3: o_OH_vinyl
        L3: o_MeO_vinyl
    L2: meta
        L3: m_CHO_CHO
    L2: para
        L3: p_OH_OH
        L3: p_OH_MeO
        L3: p_MeO_MeO
        L3: p_CHO_CHO
        L3: p_OH_CHO
        L3: p_MeO_CHO
"""
)

