from Sequence import Sequence
from Spectrum import Spectrum

import numpy as np

def scrub_deepsearch_input(form):

    myspec = form.raw.data
    myseq = form.sequence.data

    ppm = form.ppm.data

    ion_returns = np.array(
        [form.a.data, form.ap1.data, form.b.data, form.c.data, form.x.data, form.xp1.data, form.y.data, form.ym1.data,
         form.ym2.data, form.z.data])
    all_ion_types = np.array(['a', 'a+', 'b', 'c', 'x', 'x+', 'y', 'y-', 'y--', 'z'])
    myions = all_ion_types[ion_returns].tolist()

    InitMass = form.InitMass.data
    FinalMass = form.FinalMass.data
    Increment = form.Increment.data

    size = int((FinalMass - InitMass) / Increment) + 1

    to_search = (np.arange(size) * Increment + InitMass).tolist()

    processed_input = {
        'sequence': myseq,
        'spectrum': myspec,
        'searchlist': to_search,
        'ions': myions,
        'ppm': ppm
    }

    return processed_input

