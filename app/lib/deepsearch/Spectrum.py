import numpy as np
import csv

class Spectrum():
    def __init__(self, data):
        split_data =[r.split('\t') for r in data.split('\r\n')]


        masslist = [-np.inf]
        intlist = [0.0]
        for row in split_data:
            try:
                masslist.append(float(row[0]))
                intlist.append(float(row[1]))
            except (ValueError, IndexError):
                pass

        self.masslist = np.array(masslist)
        self.intlist = np.array(intlist)