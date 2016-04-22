database(
    thermoLibraries = ['primaryThermoLibrary', 'GRI-Mech3.0']   
)
# share 1 atoms with left side of 3-member ring
species(
    label='s1_3_3_ane',
    structure=SMILES("C1C2(C1)CC2"),
)
species(
    label='s1_3_3_ene',
    structure=SMILES("C1=CC12CC2"),
)
species(
    label='s1_3_4_ane',
    structure=SMILES("C1CC2(C1)CC2"),
)
species(
    label='s1_3_4_ene',
    structure=SMILES("C1=CC2(C1)CC2"),
)
species(
    label='s1_3_5_ane',
    structure=SMILES("C1CCC2(C1)CC2"),
)

species(
    label='s1_3_5_ene_1',
    structure=SMILES("C1=CC2(CC1)CC2"),
)

species(
    label='s1_3_5_ene_2',
    structure=SMILES("C1=CCC2(C1)CC2"),
)

species(
    label='s1_3_5_diene_1_3',## RENAME
    structure=SMILES("C1C=CC2(C=1)CC2"),
)

species(
    label='s1_3_6_ane',
    structure=SMILES("C1CCC2(CC1)CC2"),
)
species(
    label='s1_3_6_ene_1',
    structure=SMILES("C1=CC2(CCC1)CC2"),
)
species(
    label='s1_3_6_ene_2',
    structure=SMILES("C1=CCC2(CC1)CC2"),
)
species(
    label='s1_3_6_diene_1_4',
    structure=SMILES("C1=CC2(C=CC1)CC2"),
)
species(
    label='s1_3_6_diene_1_3',
    structure=SMILES("C1C=CC2(CC=1)CC2"),
)
# share 1 atoms with left side of 4-member ring
species(
    label='s1_4_4_ane',
    structure=SMILES("C1CCC12CCC2"),
)

species(
    label='s1_4_4_ene_1',
    structure=SMILES("C1CCC12CC=C2"),
)

species(
    label='s1_4_4_diene_1_5',
    structure=SMILES("C1C=CC12CC=C2"),
)

species(
    label='s1_4_5_ane',
    structure=SMILES("C1CCC12CCCC2"),
)

species(
    label='s1_4_5_ene_1',
    structure=SMILES("C1CCC12CCC=C2"),
)

species(
    label='s1_4_5_ene_2',
    structure=SMILES("C1CCC12CC=CC2"),
)

species(
    label='s1_4_5_ene_6',
    structure=SMILES("C1C=CC12CCCC2"),
)

species(
    label='s1_4_5_diene_1_3',
    structure=SMILES("C1CCC12C=CC=C2"),
)

species(
    label='s1_4_5_diene_1_6',
    structure=SMILES("C1C=CC12CCC=C2"),
)

species(
    label='s1_4_5_diene_2_6',
    structure=SMILES("C1C=CC12CC=CC2"),
)

species(
    label='s1_4_6_ane',
    structure=SMILES("C1CCC12CCCCC2"),
)

species(
    label='s1_4_6_ene_1',
    structure=SMILES("C1CCC12CCCC=C2"),
)

species(
    label='s1_4_6_ene_2',
    structure=SMILES("C1CCC12CCC=CC2"),
)

species(
    label='s1_4_6_ene_7',
    structure=SMILES("C1C=CC12CCCCC2"),
)

species(
    label='s1_4_6_diene_1_3',
    structure=SMILES("C1CCC12CC=CC=C2"),
)

species(
    label='s1_4_6_diene_1_4',
    structure=SMILES("C1CCC12C=CCC=C2"),
)

species(
    label='s1_4_6_diene_1_7',
    structure=SMILES("C1C=CC12CCCC=C2"),
)

species(
    label='s1_4_6_diene_2_7',
    structure=SMILES("C1C=CC12CCC=CC2"),
)

# share 1 atoms with left side of 5-member ring
species(
    label='s1_5_5_ane',
    structure=SMILES("C1CCC2(CCCC2)C1"),
)

species(
    label='s1_5_5_ene_1',
    structure=SMILES("C1CCC2(CCC=C2)C1"),
)
species(
    label='s1_5_5_ene_2',
    structure=SMILES("C1CCC2(CC=CC2)C1"),
)
species(
    label='s1_5_5_diene_1_3',
    structure=SMILES("C1CCC2(C=CC=C2)C1"),
)
species(
    label='s1_5_5_diene_1_6',
    structure=SMILES("C1=CC2(CCC=C2)CC1"),
)
species(
    label='s1_5_5_diene_1_7',
    structure=SMILES("C1=CCC2(CCC=C2)C1"),
)
species(
    label='s1_5_5_diene_2_7',
    structure=SMILES("C1=CCC2(CC=CC2)C1"),
)

species(
    label='s1_5_6_ane',
    structure=SMILES("C1CCC2(CCCCC2)C1"),
)

species(
    label='s1_5_6_ene_1',
    structure=SMILES("C1CCC2(CCCC=C2)C1"),
)
species(
    label='s1_5_6_ene_2',
    structure=SMILES("C1CCC2(CCC=CC2)C1"),
)

species(
    label='s1_5_6_ene_7',
    structure=SMILES("C1=CC2(CCCCC2)CC1"),
)
species(
    label='s1_5_6_ene_8',
    structure=SMILES("C1=CCC2(CCCCC2)C1"),
)
species(
    label='s1_5_6_diene_1_3',
    structure=SMILES("C1CCC2(CC=CC=C2)C1"),
)
species(
    label='s1_5_6_diene_1_4',
    structure=SMILES("C1CCC2(C=CCC=C2)C1"),
)
species(
    label='s1_5_6_diene_1_7',
    structure=SMILES("C1=CC2(CCCC=C2)CC1"),
)
species(
    label='s1_5_6_diene_1_8',
    structure=SMILES("C1=CCC2(CCCC=C2)C1"),
)
species(
    label='s1_5_6_diene_2_7',
    structure=SMILES("C1=CC2(CCC=CC2)CC1"),
)
species(
    label='s1_5_6_diene_2_8',
    structure=SMILES("C1=CCC2(CCC=CC2)C1"),
)
species(
    label='s1_5_6_diene_7_9',
    structure=SMILES("C1=CC2(CCCCC2)C=C1"),
)
# share 1 atoms with left side of 6-member ring
species(
    label='s1_6_6_ane',
    structure=SMILES("C1CCC2(CCCCC2)CC1"),
)

species(
    label='s1_6_6_ene_1',
    structure=SMILES("C1CCC2(CCCC=C2)CC1"),
)
species(
    label='s1_6_6_ene_2',
    structure=SMILES("C1CCC2(CCC=CC2)CC1"),
)
species(
    label='s1_6_6_diene_1_3',
    structure=SMILES("C1CCC2(CC=CC=C2)CC1"),
)
species(
    label='s1_6_6_diene_1_4',
    structure=SMILES("C1CCC2(C=CCC=C2)CC1"),
)
species(
    label='s1_6_6_diene_1_7',
    structure=SMILES("C1CCC2(CCCC=C2)C=C1"),
)
species(
    label='s1_6_6_diene_1_8',
    structure=SMILES("C1=CCC2(CCCC=C2)CC1"),
)
species(
    label='s1_6_6_diene_2_8',
    structure=SMILES("C1=CCC2(CCC=CC2)CC1"),
)
# share 2 atoms with left side of 3-member ring
species(
    label='s2_3_3_ane',
    structure=SMILES("C1C2CC12"),
)
species(
    label='s2_3_3_ene',
    structure=SMILES("C1=C2CC12"),
)
species(
    label='s2_3_4_ane',
    structure=SMILES("C1CC2CC12"),
)
species(
    label='s2_3_4_ene_1',
    structure=SMILES("C1=CC2CC12"),
)
species(
    label='s2_3_5_ane',
    structure=SMILES("C1C2CCCC21"),
)

species(
    label='s2_3_5_ene_1',
    structure=SMILES("C1C2C=CCC21"),
)

species(
    label='s2_3_6_ane',
    structure=SMILES("C1C2CCCCC21"),
)
species(
    label='s2_3_6_ene_1',
    structure=SMILES("C1C2C=CCCC21"),
)
species(
    label='s2_3_6_ene_2',
    structure=SMILES("C1C2CC=CCC21"),
)

species(
    label='s2_3_6_diene_1_3',
    structure=SMILES("C1C2C=CC=CC21"),
)

# share 2 atoms with left side of 4-member ring
species(
    label='s2_4_4_ane',
    structure=SMILES("C1CC2CCC21"),
)
species(
    label='s2_4_4_ene_1',
    structure=SMILES("C1CC2C=CC21"),
)
species(
    label='s2_4_5_ane',
    structure=SMILES("C1CC2CCCC21"),
)

species(
    label='s2_4_5_ene_1',
    structure=SMILES("C1CC2CC=CC21"),
)

species(
    label='s2_4_6_ane',
    structure=SMILES("C1CC2CCCCC21"),
)
species(
    label='s2_4_6_ene_1',
    structure=SMILES("C1CC2CCC=CC21"),
)
species(
    label='s2_4_6_ene_2',
    structure=SMILES("C1CC2CC=CCC21"),
)
# share 2 atoms with left side of 5-member ring
species(
    label='s2_5_5_ane',
    structure=SMILES("C12CCCC1CCC2"),
)

species(
    label='s2_5_5_ene_0',
    structure=SMILES("C12CCCC1=CCC2"),
)

species(
    label='s2_5_5_ene_1',
    structure=SMILES("C12CCCC1C=CC2"),
)

species(
    label='s2_5_5_ene_m',
    structure=SMILES("C1(CCC2)=C2CCC1"),
)
species(
    label='s2_5_5_diene_0_2',
    structure=SMILES("C12CCCC1=CC=C2"),
)

species(
    label='s2_5_5_diene_0_3',
    structure=SMILES("C12=CCC=C1CCC2"),
)

species(
    label='s2_5_5_diene_m_2',
    structure=SMILES("C1(C=CC2)=C2CCC1"),
)

species(
    label='s2_5_5_diene_0_4',
    structure=SMILES("C12=CCCC1=CCC2"),
)

species(
    label='s2_5_5_diene_0_5',
    structure=SMILES("C12=CCCC1C=CC2"),
)

species(
    label='s2_5_5_diene_0_6',
    structure=SMILES("C12CC=CC1=CCC2"),
)

species(
    label='s2_5_5_diene_1_5',
    structure=SMILES("C12C=CCC1C=CC2"),
)

species(
    label='s2_5_5_diene_1_6',
    structure=SMILES("C12CC=CC1C=CC2"),
)

species(
    label='s2_5_6_ane',
    structure=SMILES("C12CCCC1CCCC2"),
)

species(
    label='s2_5_6_ene_0',
    structure=SMILES("C12CCCC1=CCCC2"),
)

species(
    label='s2_5_6_ene_1',
    structure=SMILES("C12CCCC1C=CCC2"),
)

species(
    label='s2_5_6_ene_m',
    structure=SMILES("C1(CCCC2)=C2CCC1"),
)

species(
    label='s2_5_6_ene_2',
    structure=SMILES("C12CCCC1CC=CC2"),
)

species(
    label='s2_5_6_ene_5',
    structure=SMILES("C12=CCCC1CCCC2"),
)

species(
    label='s2_5_6_ene_6',
    structure=SMILES("C12C=CCC1CCCC2"),
)

species(
    label='s2_5_6_diene_m_1',
    structure=SMILES("C1(CCC=C2)=C2CCC1"),
)

species(
    label='s2_5_6_diene_m_2',
    structure=SMILES("C1(CC=CC2)=C2CCC1"),
)

species(
    label='s2_5_6_diene_m_7',
    structure=SMILES("C1(CCCC2)=C2C=CC1"),
)

species(
    label='s2_5_6_diene_0_2',
    structure=SMILES("C12CCCC1=CC=CC2"),
)

species(
    label='s2_5_6_diene_0_3',
    structure=SMILES("C12CCCC1=CCC=C2"),
)

species(
    label='s2_5_6_diene_0_4',
    structure=SMILES("C12=CCCC=C1CCC2"),
)

species(
    label='s2_5_6_diene_0_5',
    structure=SMILES("C12=CCCC1=CCCC2"),
)

species(
    label='s2_5_6_diene_0_6',
    structure=SMILES("C12C=CCC1=CCCC2"),
)
species(
    label='s2_5_6_diene_0_7',
    structure=SMILES("C12CC=CC1=CCCC2"),
)
species(
    label='s2_5_6_diene_1_3',
    structure=SMILES("C12CCCC1C=CC=C2"),
)
species(
    label='s2_5_6_diene_1_5',
    structure=SMILES("C12=CCCC1C=CCC2"),
)
species(
    label='s2_5_6_diene_1_6',
    structure=SMILES("C12C=CCC1C=CCC2"),
)
species(
    label='s2_5_6_diene_1_7',
    structure=SMILES("C12CC=CC1C=CCC2"),
)
species(
    label='s2_5_6_diene_2_5',
    structure=SMILES("C12=CCCC1CC=CC2"),
)
species(
    label='s2_5_6_diene_2_6',
    structure=SMILES("C12C=CCC1CC=CC2"),
)

species(
    label='s2_5_6_diene_5_7',
    structure=SMILES("C12=CC=CC1CCCC2"),
)
species(
    label='s2_5_6_diene_5_8',
    structure=SMILES("C12=CCC=C1CCCC2"),
)

# share 2 atoms with left side of 6-member ring
species(
    label='s2_6_6_ane',
    structure=SMILES("C12CCCCC1CCCC2"),
)

species(
    label='s2_6_6_ene_0',
    structure=SMILES("C12CCCCC1=CCCC2"),
)

species(
    label='s2_6_6_ene_1',
    structure=SMILES("C12CCCCC1C=CCC2"),
)

species(
    label='s2_6_6_ene_2',
    structure=SMILES("C12CCCCC1CC=CC2"),
)

species(
    label='s2_6_6_ene_m',
    structure=SMILES("C1(CCCC2)=C2CCCC1"),
)
species(
    label='s2_6_6_diene_m_1',
    structure=SMILES("C1(CCC=C2)=C2CCCC1"),
)

species(
    label='s2_6_6_diene_m_2',
    structure=SMILES("C1(CC=CC2)=C2CCCC1"),
)

species(
    label='s2_6_6_diene_0_2',
    structure=SMILES("C12CCCCC1=CC=CC2"),
)

species(
    label='s2_6_6_diene_0_3',
    structure=SMILES("C12CCCCC1=CCC=C2"),
)

species(
    label='s2_6_6_diene_0_4',
    structure=SMILES("C12=CCCC=C1CCCC2"),
)

species(
    label='s2_6_6_diene_0_5',
    structure=SMILES("C12=CCCCC1=CCCC2"),
)

species(
    label='s2_6_6_diene_0_6',
    structure=SMILES("C12C=CCCC1=CCCC2"),
)
species(
    label='s2_6_6_diene_0_7',
    structure=SMILES("C12CC=CCC1=CCCC2"),
)
species(
    label='s2_6_6_diene_0_8',
    structure=SMILES("C12CCC=CC1=CCCC2"),
)

species(
    label='s2_6_6_diene_1_3',
    structure=SMILES("C12CCCCC1C=CC=C2"),
)

species(
    label='s2_6_6_diene_1_6',
    structure=SMILES("C12C=CCCC1C=CCC2"),
)
species(
    label='s2_6_6_diene_1_7',
    structure=SMILES("C12CC=CCC1C=CCC2"),
)

species(
    label='s2_6_6_diene_1_8',
    structure=SMILES("C12CCC=CC1C=CCC2"),
)

species(
    label='s2_6_6_diene_2_7',
    structure=SMILES("C12CC=CCC1CC=CC2"),
)
# share 3 atoms with left side of 4-member ring
species(
    label='s3_4_4_ane',
    structure=SMILES("C1(C2)CC2C1"),
)

species(
    label='s3_4_4_ene_0',
    structure=SMILES("C12CC(C2)=C1"),
)

species(
    label='s3_4_4_diene_0_2',
    structure=SMILES("C1(C2)=CC2=C1"),
)

species(
    label='s3_4_5_ane',
    structure=SMILES("C12CC(C2)CC1"),
)

species(
    label='s3_4_5_ene_0',
    structure=SMILES("C12=CCC(C2)C1"),
)

species(
    label='s3_4_5_ene_1',
    structure=SMILES("C12CC(C2)C=C1"),
)

species(
    label='s3_4_5_ene_3',
    structure=SMILES("C12=CC(C2)CC1"),
)

species(
    label='s3_4_5_diene_0_2',
    structure=SMILES("C12=CC=C(C2)C1"),
)

species(
    label='s3_4_5_diene_0_3',
    structure=SMILES("C12=CCC(C2)=C1"),
)

species(
    label='s3_4_5_diene_1_3',
    structure=SMILES("C12C=C(C2)C=C1"),
)

species(
    label='s3_4_5_diene_3_4',
    structure=SMILES("C1(CC2)=CC2=C1"),
)
species(
    label='s3_4_6_ane',
    structure=SMILES("C1(C2)CC2CCC1"),
)

species(
    label='s3_4_6_ene_0',
    structure=SMILES("C1(C2)CC2=CCC1"),
)

species(
    label='s3_4_6_ene_1',
    structure=SMILES("C1(C2)CC2C=CC1"),
)

species(
    label='s3_4_6_ene_4',
    structure=SMILES("C1(C2)=CC2CCC1"),
)

species(
    label='s3_4_6_diene_0_2',
    structure=SMILES("C1(C2)CC2=CC=C1"),
)

species(
    label='s3_4_6_diene_0_3',
    structure=SMILES("C1(C2)=CCC=C2C1"),
)
species(
    label='s3_4_6_diene_0_4',
    structure=SMILES("C1(C2)=CC2=CCC1"),
)

species(
    label='s3_4_6_diene_1_4',
    structure=SMILES("C1(C2)=CC2C=CC1"),
)

species(
    label='s3_4_6_diene_1_5',
    structure=SMILES("C1(C2)=CC2CC=C1"),
)
# share 3 atoms with left side of 5-member ring
species(
    label='s3_5_5_ane',
    structure=SMILES("C1CC(C2)CCC21"),
)

species(
    label='s3_5_5_ene_1',
    structure=SMILES("C1=CC2CCC1C2"),
)

species(
    label='s3_5_5_diene_1_4',
    structure=SMILES("C1=CC2C=CC1C2"),
)
species(
    label='s3_5_6_ane',
    structure=SMILES("C1CC2CCC(C1)C2"),
)
species(
    label='s3_5_6_ene_1',
    structure=SMILES("C1=CC2CCC(C1)C2"),
)
species(
    label='s3_5_6_ene_5',
    structure=SMILES("C1CC2C=CC(C1)C2"),
)

species(
    label='s3_5_6_diene_1_5',
    structure=SMILES("C1=CC2C=CC(C1)C2"),
)
# share 3 atoms with left side of 6-member ring
species(
    label='s3_6_6_ane',
    structure=SMILES("C1(CCC2)CC2CCC1"),
)
species(
    label='s3_6_6_ene_0',
    structure=SMILES("C1(CCC2)CC2=CCC1"),
)

species(
    label='s3_6_6_ene_1',
    structure=SMILES("C1(CCC2)CC2C=CC1"),
)

species(
    label='s3_6_6_ene_4',
    structure=SMILES("C1(CCC2)C=C2CCC1"),
)

species(
    label='s3_6_6_diene_0_m',
    structure=SMILES("C1(CCC2)=CC2=CCC1"),
)
species(
    label='s3_6_6_diene_0_2',
    structure=SMILES("C1(CCC2)CC2=CC=C1"),
)
species(
    label='s3_6_6_diene_0_3',
    structure=SMILES("C1(CCC2)=CCC=C2C1"),
)
species(
    label='s3_6_6_diene_0_4',
    structure=SMILES("C1(C2)=CCCC2=CCC1"),
)
species(
    label='s3_6_6_diene_0_5',
    structure=SMILES("C1(C=CC2)CC2=CCC1"),
)
species(
    label='s3_6_6_diene_0_6',
    structure=SMILES("C1(CC=C2)CC2=CCC1"),
)
species(
    label='s3_6_6_diene_1_m',
    structure=SMILES("C1(CCC2)=CC2C=CC1"),
)
species(
    label='s3_6_6_diene_1_5',
    structure=SMILES("C1(C=CC2)CC2C=CC1"),
)
species(
    label='s3_6_6_diene_1_6',
    structure=SMILES("C1(CC=C2)CC2C=CC1"),
)
species(
    label='s3_6_6_diene_1_8',
    structure=SMILES("C1(CCC2)C=C2C=CC1"),
)

# batch 3
species(
    label='s2_4_6_diene_1_3',
    structure=SMILES("C12C=CC=CC1CC2"),
)

species(
    label='s2_4_6_diene_1_6',
    structure=SMILES("C12CCC=CC1C=C2"),
)

species(
    label='s2_4_6_diene_2_6',
    structure=SMILES("C12CC=CCC1C=C2"),
)

species(
    label='s2_4_6_ben',
    structure=SMILES("C12=CC=CC=C1CC2"),
)

species(
    label='s2_5_6_ben',
    structure=SMILES("C12=CC=CC=C1CCC2"),
)

species(
    label='s2_6_6_ben',
    structure=SMILES("C12=CC=CC=C1CCCC2"),
)

quantumMechanics(
    software='mopac',
    method='pm7',
    onlyCyclics = True,
    maxRadicalNumber = 0,
)
