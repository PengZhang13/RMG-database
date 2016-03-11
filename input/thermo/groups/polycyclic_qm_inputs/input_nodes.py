database(
    thermoLibraries = ['primaryThermoLibrary', 'GRI-Mech3.0']   
)
# share 1 atoms with left side of 3-member ring
species(
    label='s3_6_6_ene_yne_1_8',
    structure=SMILES("C1(CCC2)C=C2C#CC1"),
)
quantumMechanics(
    software='mopac',
    method='pm7',
    onlyCyclics = True,
    maxRadicalNumber = 0,
)
