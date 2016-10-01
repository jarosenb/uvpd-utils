import numpy as np


class ThrashSpectrum:
    def __init__(self, thrash_input, charge):

        output = {c:[[-np.inf,0]] for c in range(1,charge+1)}

        for line in thrash_input.split('\n'):

            ln = line.strip().split(',')

            try:

                charge = int(round(float(ln[2]) / float(ln[1])))

                output[charge].append([float(ln[2]), float(ln[4])])

            except (ValueError, IndexError, KeyError):
                pass

        for i in output:
            us = np.array(output[i])


            if us.size > 0:
                us = us[us[:,0].argsort()]
            output[i] = us

        self.ions = output


