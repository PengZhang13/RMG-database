import re

def getExternalSymmetryNumberFromPointGroup(pointGroup):
	"""
	INPUT: point group in `str` type
	OUTPUT: external symmetry number
	"""
	if pointGroup in ['Cs', 'Ci', 'Cinfv', 'Kh']: 
		return 1
	elif pointGroup in ['Dinfh']:
		return 2
	elif pointGroup in ['T', 'Th', 'Td']:
		return 12
	elif pointGroup in ['O', 'Oh']:
		return 24
	elif pointGroup in ['I', 'Ih']:
		return 60

	# for point groups with n embeded
	pattern1 = re.compile(ur'[CDS]\d')
	pattern2 = re.compile(ur'[CDS]\d[vhd]')
	

	match1 = re.search(pattern1, pointGroup)
	match2 = re.search(pattern2, pointGroup)
	if not match1:
		return 1
	elif not match2:
		start_char = match1.group(0)[0]
		n = int(match1.group(0)[1])
		if start_char == 'S':
			return n/2.0
		elif start_char == 'C':
			return n
		elif start_char == 'D':
			return 2*n
	else:
		start_char = match2.group(0)[0]
		n = int(match2.group(0)[1])
		if start_char == 'S':
			return n/2.0
		elif start_char == 'C':
			return n
		elif start_char == 'D':
			return 2*n
