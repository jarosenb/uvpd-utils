import re


class Sequence:

    def __init__(self, raw_seq):
        self.raw_seq = re.sub(' ', '', raw_seq)

        if raw_seq[0]=='(':
            raise ValueError("Incorrect formatting of modifications")
        self.patt = '\(([0-9\.\-]+)\)'
        self.stripped_seq = re.sub(self.patt, '', self.raw_seq)

    def mods(self):
        mod_masses = iter(re.findall(self.patt, self.raw_seq))
        mod_dict = {}
        mstring = ''


        for k in re.split(self.patt, self.raw_seq)[:-1:2]:
            if k:
                mstring += k
                mod_dict[len(mstring)-1] = float(mod_masses.next())

        return mod_dict







