database(
    thermoLibraries = ['primaryThermoLibrary', 'GRI-Mech3.0']   
)
# share 1 atoms with left side of 3-member ring
species(
    label='s1_3_3_ane',
    structure=SMILES("C1C2(C1)CC2"),
    pointGroup='D2d',
)
species(
    label='s1_3_3_ene',
    structure=SMILES("C1=CC12CC2"),
    pointGroup='C2v',
)
species(
    label='s1_3_4_ane',
    structure=SMILES("C1CC2(C1)CC2"),
    pointGroup='Cs',
)
species(
    label='s1_3_4_ene',
    structure=SMILES("C1=CC2(C1)CC2"),
    pointGroup='Cs',
)
species(
    label='s1_3_5_ane',
    structure=SMILES("C1CCC2(C1)CC2"),
    pointGroup='C2',
)

species(
    label='s1_3_5_ene_1',
    structure=SMILES("C1=CC2(CC1)CC2"),
    pointGroup='Cs??',
)

species(
    label='s1_3_5_ene_2',
    structure=SMILES("C1=CCC2(C1)CC2"),
    pointGroup='Cs??',
)

species(
    label='s1_3_5_diene_1_3',## RENAME
    structure=SMILES("C1C=CC2(C=1)CC2"),
    pointGroup='C2v',
)

species(
    label='s1_3_6_ane',
    structure=SMILES("C1CCC2(CC1)CC2"),
    pointGroup='Cs',
)
species(
    label='s1_3_6_ene_1',
    structure=SMILES("C1=CC2(CCC1)CC2"),
    pointGroup='Cs??',
)
species(
    label='s1_3_6_ene_2',
    structure=SMILES("C1=CCC2(CC1)CC2"),
    pointGroup='Cs??',
)
species(
    label='s1_3_6_diene_1_4',
    structure=SMILES("C1=CC2(C=CC1)CC2"),
    pointGroup='C2v',
)
species(
    label='s1_3_6_diene_1_3',
    structure=SMILES("C1C=CC2(CC=1)CC2"),
    pointGroup='Cs',
)
# share 2 atoms with left side of 3-member ring
species(
    label='s2_3_3_ane',
    structure=SMILES("C1C2CC12"),
    pointGroup='C2v',
)
species(
    label='s2_3_3_ene',
    structure=SMILES("C1=C2CC12"),
    pointGroup='Ci??',
)
species(
    label='s2_3_4_ane',
    structure=SMILES("C1CC2CC12"),
    pointGroup='C2',
)
species(
    label='s2_3_4_ene_1',
    structure=SMILES("C1=CC2CC12"),
    pointGroup='Cs',
)
species(
    label='s2_3_5_ane',
    structure=SMILES("C1C2CCCC21"),
    pointGroup='Cs',
)

species(
    label='s2_3_5_ene_1',
    structure=SMILES("C1C2C=CCC21"),
    pointGroup='Ci??',
)

species(
    label='s2_3_6_ane',
    structure=SMILES("C1C2CCCCC21"),
    pointGroup='Cs',
)
species(
    label='s2_3_6_ene_1',
    structure=SMILES("C1C2C=CCCC21"),
    pointGroup='Cs??',
)
species(
    label='s2_3_6_ene_2',
    structure=SMILES("C1C2CC=CCC21"),
    pointGroup='C2',
)

species(
    label='s2_3_6_diene_1_3',
    structure=SMILES("C1C2C=CC=CC21"),
    pointGroup='Cs',
)

# share 2 atoms with left side of 4-member ring
species(
    label='s2_4_4_ane',
    structure=SMILES("C1CC2CCC21"),
    pointGroup='C2h',
)
species(
    label='s2_4_4_ene_1',
    structure=SMILES("C1CC2C=CC21"),
    pointGroup='C2',
)
species(
    label='s2_4_5_ane',
    structure=SMILES("C1CC2CCCC21"),
    pointGroup='C2',
)

species(
    label='s2_4_5_ene_1',
    structure=SMILES("C1CC2CC=CC21"),
    pointGroup='Cs??',
)

species(
    label='s2_4_6_ane',
    structure=SMILES("C1CC2CCCCC21"),
    pointGroup='Cs??',
)
species(
    label='s2_4_6_ene_1',
    structure=SMILES("C1CC2CCC=CC21"),
    pointGroup='Cs??',
)
species(
    label='s2_4_6_ene_2',
    structure=SMILES("C1CC2CC=CCC21"),
    pointGroup='Cs??',
)

# share 3 atoms with left side of 5-member ring
species(
    label='s3_5_5_ane',
    structure=SMILES("C1CC(C2)CCC21"),
    pointGroup='C2v',
)

species(
    label='s3_5_5_ene_1',
    structure=SMILES("C1=CC2CCC1C2"),
    pointGroup='Cs',
)

species(
    label='s3_5_5_diene_1_4',
    structure=SMILES("C1=CC2C=CC1C2"),
    pointGroup='C2v',
)
species(
    label='s3_5_6_ane',
    structure=SMILES("C1CC2CCC(C1)C2"),
    pointGroup='Cs??',
)
species(
    label='s3_5_6_ene_1',
    structure=SMILES("C1=CC2CCC(C1)C2"),
    pointGroup='Cs??',
)
species(
    label='s3_5_6_ene_5',
    structure=SMILES("C1CC2C=CC(C1)C2"),
    pointGroup='Cs',
)

species(
    label='s3_5_6_diene_1_5',
    structure=SMILES("C1=CC2C=CC(C1)C2"),
    pointGroup='Cs??',
)
quantumMechanics(
    software='mopac',
    method='pm7',
    onlyCyclics = True,
    maxRadicalNumber = 0,
)
