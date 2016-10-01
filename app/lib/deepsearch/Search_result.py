from ion_masses import ion_masses
from np_search import searchppm
from Sequence import Sequence
from Spectrum import Spectrum
import numpy as np



def SearchResult(self, scrubbed_form):


    sequence = Sequence(scrubbed_form['sequence'])
    spectrum = Spectrum(scrubbed_form['spectrum'])
    modlist = scrubbed_form['searchlist']
    ion_types = scrubbed_form['ions']
    ppm = scrubbed_form['ppm']



    # all_ion_types = ['a', 'a+', 'b', 'c', 'x', 'x+', 'y', 'y-', 'y--', 'z']

    aions = ion_masses(sequence, ion_types)
    masslist = spectrum.masslist

    length = len(sequence.stripped_seq)
    total = np.size(modlist)
    result = np.zeros((np.size(modlist), 4))
    result = np.vstack((np.array(['Mass Shift', 'Total Fragment Matches', 'N-terminal Matches', 'C-terminal matches']), result))

    i=1
    for mod in modlist:
        sumN = 0
        sumC = 0
        for (ion, masses) in aions.items():
            iondict_entry = searchppm(masslist, masses + mod, ppm=ppm)
            if ion[0] in ['a', 'b', 'c']:
                sumN += np.sum(iondict_entry > 0)
            elif ion[0] in ['x', 'y', 'z']:
                sumC += np.sum(iondict_entry > 0)

        result[i,:] = np.array([str(mod), str(int(sumN+sumC)), str(int(sumN)), str(int(sumC))])
        i += 1

        self.update_state(state='PROGRESS',
                          meta={'current': i, 'total': total,
                                'status': "processing..."})


    return {'current': 100, 'total': 100, 'status': 'Task completed!',
            'result': result.tolist() }







