from generate_ion_masses import ion_masses
from np_search import searchppm
import numpy as np

class SearchResult:
    def __init__(self, input):

        sequence = input['sequence']
        spectrum = input['spectrum']
        modlist = input['mods']
        tic = input['tic']
        ppm = input['ppm']
        ion_types = input['ions']

        aions = ion_masses(sequence, ion_types)
        masslist = spectrum.masslist
        intlist = spectrum.intlist

        length = len(sequence.stripped_seq)

        iondict_apo = {}
        iondict_holo = {i: np.zeros(length) for i in ion_types}

        for (ion, masses) in aions.items():
            iondict_entry = searchppm(masslist, masses, ppm=ppm)
            iondict_entry = intlist[(iondict_entry > 0) * iondict_entry]
            if ion[0] in ['a', 'b', 'c']:
                iondict_entry = np.concatenate([iondict_entry, [0.]])
            else:
                iondict_entry = np.concatenate([[0.], iondict_entry[::-1]])
            iondict_apo[ion] = iondict_entry / tic

        for mod in modlist:
            for (ion, masses) in aions.items():
                iondict_entry = searchppm(masslist, masses + mod, ppm=ppm)
                iondict_entry = np.array(intlist)[(iondict_entry > 0) * iondict_entry]
                if ion[0] in ['a', 'b', 'c']:
                    iondict_entry = np.concatenate([iondict_entry, [0.]])
                else:
                    iondict_entry = np.concatenate([[0.], iondict_entry[::-1]])
                iondict_holo[ion] += iondict_entry / tic

        self.iondict_apo = iondict_apo
        self.iondict_holo = iondict_holo
        self.iondict_all = {key: iondict_apo[key] + iondict_holo[key] for key in iondict_apo}
        self.length = length
        self.ions = ion_types

    def apo_csv(self):
        # return ['Position'] + self.iondict_apo.keys()
        bigarr = np.arange(1, self.length + 1).astype('str')

        header = np.array(['Residue Position', 'Sum (all ions)', 'Sum (N-terminal)', 'Sum (C-terminal)'] + self.ions)

        sum_nterm = np.sum(np.stack([np.zeros(self.length)]+[self.iondict_apo[ion] for ion in self.ions if ion[0] in ('a', 'b', 'c')], axis=1),
                               axis=1)


        sum_cterm = np.sum(np.stack([np.zeros(self.length)]+[self.iondict_apo[ion] for ion in self.ions if ion[0] in ('x', 'y', 'z')], axis=1),
                               axis=1)

        sum_all = sum_nterm + sum_cterm

        body = np.stack([bigarr, sum_all, sum_nterm, sum_cterm] + [self.iondict_apo[ion] for ion in self.ions], axis=1)

        result = np.vstack((header, body))
        return result

    def holo_csv(self):
        bigarr = np.arange(1, self.length + 1).astype('str')

        header = np.array(['Residue Position', 'Sum (all ions)', 'Sum (N-terminal)', 'Sum (C-terminal)'] + self.ions)
        sum_nterm = np.sum(np.stack([self.iondict_holo[ion] for ion in self.ions if ion[0] in ('a', 'b', 'c')], axis=1),
                           axis=1)
        sum_cterm = np.sum(np.stack([self.iondict_holo[ion] for ion in self.ions if ion[0] in ('x', 'y', 'z')], axis=1),
                           axis=1)
        sum_all = sum_nterm + sum_cterm

        body = np.stack([bigarr, sum_all, sum_nterm, sum_cterm] + [self.iondict_holo[ion] for ion in self.ions], axis=1)

        result = np.vstack((header, body))
        return result

    def all_csv(self):
        bigarr = np.arange(1, self.length + 1).astype('str')

        header = np.array(['Residue Position', 'Sum (all ions)', 'Sum (N-terminal)', 'Sum (C-terminal)'] + self.ions)
        sum_nterm = np.sum(np.stack([self.iondict_all[ion] for ion in self.ions if ion[0] in ('a', 'b', 'c')], axis=1),
                           axis=1)
        sum_cterm = np.sum(np.stack([self.iondict_all[ion] for ion in self.ions if ion[0] in ('x', 'y', 'z')], axis=1),
                           axis=1)
        sum_all = sum_nterm + sum_cterm

        body = np.stack([bigarr, sum_all, sum_nterm, sum_cterm] + [self.iondict_all[ion] for ion in self.ions], axis=1)

        result = np.vstack((header, body))
        return result

