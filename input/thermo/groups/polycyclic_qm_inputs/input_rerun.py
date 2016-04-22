database(
    thermoLibraries = ['primaryThermoLibrary', 'GRI-Mech3.0']   
)
# share 1 atoms with left side of 3-member ring
species(
    label='s2_6_6_diene_2_7',
    structure=SMILES("C12CC=CCC1CC=CC2"),
)

species(
    label='s2_4_6_diene_1_3',
    structure=SMILES(""),
)

species(
    label='s2_4_6_diene_1_6',
    structure=SMILES(""),
)

species(
    label='s2_4_6_diene_2_6',
    structure=SMILES(""),
)

quantumMechanics(
    software='mopac',
    method='pm7',
    onlyCyclics = True,
    maxRadicalNumber = 0,
)
