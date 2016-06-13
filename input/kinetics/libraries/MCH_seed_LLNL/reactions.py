#!/usr/bin/env python
# encoding: utf-8

name = "MCH_seed_LLNL"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 1,
    label = "mch + oh <=> mchr1 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (512200, 'cm^3/(mol*s)'),
        n = 2.06,
        Ea = (-1834, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 2,
    label = "mch + oh <=> mchr2 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (195000, 'cm^3/(mol*s)'),
        n = 2.451,
        Ea = (-1160, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 3,
    label = "mch + oh <=> mchr3 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (195000, 'cm^3/(mol*s)'),
        n = 2.451,
        Ea = (-1160, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 4,
    label = "mch + oh <=> mchr4 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (97500, 'cm^3/(mol*s)'),
        n = 2.451,
        Ea = (-1160, 'cal/mol'),
        T0 = (1, 'K'),
    ),
)

entry(
    index = 5,
    label = "mch + oh <=> cychexch2 + h2o",
    degeneracy = 1,
    kinetics = Arrhenius(A=(2e+07, 'cm^3/(mol*s)'), n=1.763, Ea=(31.8, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 6,
    label = "mchr1 + o2 <=> mch1oo",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.41e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Argonne primary rate 2 times higher than LLNL acyclic primary rate',
    ),
    longDesc = 
u"""
Argonne primary rate 2 times higher than LLNL acyclic primary rate
""",
)

entry(
    index = 7,
    label = "mchr2 + o2 <=> mch2oo",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.75e+14, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (-506, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Tertiary site rule, Sarathy et al. rule, iso-alkanes, Comb. Flame 2011',
    ),
    longDesc = 
u"""
Tertiary site rule, Sarathy et al. rule, iso-alkanes, Comb. Flame 2011
""",
)

entry(
    index = 8,
    label = "mchr3 + o2 <=> mch3oo",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.75e+14, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (-506, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Fernandes et al. Zador, PCCP 2009 for chxrad+o2=chxo2j, 50 bar rate',
    ),
    longDesc = 
u"""
Fernandes et al. Zador, PCCP 2009 for chxrad+o2=chxo2j, 50 bar rate
""",
)

entry(
    index = 9,
    label = "mchr4 + o2 <=> mch4oo",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.75e+14, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (-506, 'cal/mol'),
        T0 = (1, 'K'),
        comment = '! Fernandes et al. Zador, PCCP 2009 for chxrad+o2=chxo2j, 50 bar rate',
    ),
    longDesc = 
u"""
! Fernandes et al. Zador, PCCP 2009 for chxrad+o2=chxo2j, 50 bar rate
""",
)

entry(
    index = 10,
    label = "cychexch2 + o2 <=> chxch2oo",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'Fernandes et al. Zador, PCCP 2009 for chxrad+o2=chxo2j, 50 bar rate',
    ),
    longDesc = 
u"""
Fernandes et al. Zador, PCCP 2009 for chxrad+o2=chxo2j, 50 bar rate
""",
)

entry(
    index = 11,
    label = "mch1q3j <=> mchyo13 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4e+12, 's^-1'),
        n = 0,
        Ea = (19500, 'cal/mol'),
        T0 = (1, 'K'),
        comment = 'CVN est.',
    ),
    longDesc = 
u"""
CVN est.
""",
)

entry(
    index = 12,
    label = "mch1q4j <=> mchyo14 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.3e+12, 's^-1'), n=0, Ea=(18300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 13,
    label = "mch2q2j <=> mchyo22 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+12, 's^-1'), n=0, Ea=(19500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 14,
    label = "mch2q4j <=> mchyo24 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+12, 's^-1'), n=0, Ea=(19500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 15,
    label = "mch3q1j <=> mchyo13 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+12, 's^-1'), n=0, Ea=(19500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 16,
    label = "mch3q3j <=> mchyo33 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+12, 's^-1'), n=0, Ea=(19500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 17,
    label = "mch4q2j <=> mchyo24 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+12, 's^-1'), n=0, Ea=(19500, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 18,
    label = "mch4q1j <=> mchyo14 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(3.3e+12, 's^-1'), n=0, Ea=(18300, 'cal/mol'), T0=(1, 'K')),
)

entry(
    index = 19,
    label = "mch0q2j <=> mchyo02 + oh",
    degeneracy = 1,
    kinetics = Arrhenius(A=(4e+12, 's^-1'), n=0, Ea=(19500, 'cal/mol'), T0=(1, 'K')),
)

