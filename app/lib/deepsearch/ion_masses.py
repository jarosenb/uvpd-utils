import numpy as np


def ion_masses(seq_object, ion_types, iam=False):


    base_diffs = {
        'a': -27.9949,
        'a+': -26.987075,
        'b': 0,
        'c': 17.026549,
        'x': 43.989830,
        'x+': 44.997655,
        'y': 18.010565,
        'y-': 17.00274,
        'y--': 15.994915,
        'z': 1.991841,
    }

    std_aa_mass = {
        'G': 57.02146,
        'A': 71.03711,
        'S': 87.03203,
        'P': 97.05276,
        'V': 99.06841,
        'T': 101.04768,
        'C': 103.00919,
        'L': 113.08406,
        'I': 113.08406,
        'N': 114.04293,
        'D': 115.02694,
        'Q': 128.05858,
        'K': 128.09496,
        'E': 129.04259,
        'M': 131.04049,
        'H': 137.05891,
        'F': 147.06841,
        'R': 156.10111,
        'Y': 163.06333,
        'W': 186.07931,
        }

    if iam:
        std_aa_mass['C'] += 57.021464

    seq = seq_object.stripped_seq

    aa_masses_with_mods = [std_aa_mass[aa] for aa in seq]

    for (idx, mass) in seq_object.mods().items():
        aa_masses_with_mods[idx] += mass

    sums_Nterm = np.cumsum(aa_masses_with_mods[:-1])
    sums_Cterm = np.cumsum(aa_masses_with_mods[::-1][:-1])

    all_ions = {}
    for iontype in ion_types:
        if iontype[0] in ['a', 'b', 'c']:
            all_ions[iontype] = sums_Nterm + base_diffs[iontype]
        else:
            all_ions[iontype] = sums_Cterm + base_diffs[iontype]

    return all_ions




#import pprint
#pprint.pprint(ion_masses("CPEPTIDEC", iam=True))



