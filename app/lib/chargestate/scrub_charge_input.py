from process_sequence import Sequence
from ThrashSpectrum import ThrashSpectrum
from charge_results import ChargeResult
import numpy as np

def scrub_charge_input(form):
    charge = form.charge.data

    myspec = ThrashSpectrum(form.raw.data, charge)
    myseq = Sequence(form.sequence.data)



    ppm = form.ppm.data

    ion_returns = np.array(
        [form.a.data, form.ap1.data, form.b.data, form.c.data, form.x.data, form.xp1.data, form.y.data, form.ym1.data,
         form.ym2.data, form.z.data])
    all_ion_types = np.array(['a', 'a+', 'b', 'c', 'x', 'x+', 'y', 'y-', 'y--', 'z'])
    myions = all_ion_types[ion_returns].tolist()

    processed_input = {
        'sequence': myseq,
        'spectrum': myspec,
        'charge' :charge,
        'ions': myions,
        'ppm': ppm
    }



    return ChargeResult(processed_input)