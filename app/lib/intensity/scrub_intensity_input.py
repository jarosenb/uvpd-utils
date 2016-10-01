import numpy as np
from process_sequence import Sequence
from process_spectrum import Spectrum
from Search_result import SearchResult
import csv

def scrub_intensity_input(form):

    myspec = Spectrum(form.raw.data)
    myseq = Sequence(form.sequence.data)

    modlist = []
    if form.mods.data:
        modlist = [float(i) for i in form.mods.data.split(',')]

    tic = 1.0
    if form.tic.data:
        tic = float(form.tic.data)

    ppm = form.ppm.data

    ion_returns = np.array([form.a.data, form.ap1.data, form.b.data, form.c.data, form.x.data, form.xp1.data, form.y.data, form.ym1.data,form.ym2.data, form.z.data])
    all_ion_types = np.array(['a', 'a+', 'b', 'c', 'x', 'x+', 'y', 'y-', 'y--', 'z'])
    myions = all_ion_types[ion_returns].tolist()

    processed_input = {
        'sequence': myseq,
        'spectrum': myspec,
        'mods': modlist,
        'tic': tic,
        'ions': myions,
        'ppm': ppm
    }

    return SearchResult(processed_input)
