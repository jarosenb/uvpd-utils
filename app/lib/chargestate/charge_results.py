import numpy as np
from generate_ion_masses import ion_masses
from np_search import searchppm

class ChargeResult:
    def __init__(self, input_dict):

        spectrum = input_dict['spectrum']
        sequence = input_dict['sequence']
        charge = input_dict['charge']
        ppm = input_dict['ppm']
        ion_types = input_dict['ions']


        length = len(sequence.stripped_seq)
        ion_mass = ion_masses(sequence, ion_types)


        self.result_nterm = np.zeros((length-1, charge))
        for ion in [i for i in ion_types if i[0] in ['a', 'b', 'c']]:
            for charge in spectrum.ions:
                masses = spectrum.ions[charge][:,0]
                ints = spectrum.ions[charge][:,1]

                search_result = searchppm(masses, ion_mass[ion], ppm=ppm)

                searched_intensities = ints[(search_result > 0) * search_result]
                self.result_nterm[:, charge-1] += searched_intensities

        self.result_cterm = np.zeros((length - 1, charge))
        for ion in [i for i in ion_types if i[0] in ['x', 'y', 'z']]:
            for charge in spectrum.ions:
                masses = spectrum.ions[charge][:, 0]
                ints = spectrum.ions[charge][:, 1]
                search_result = searchppm(masses, ion_mass[ion], ppm=ppm)

                searched_intensities = ints[(search_result > 0) * search_result]
                self.result_cterm[:, charge - 1] += searched_intensities





