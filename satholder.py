from basics import get_bit, get_sdic, set_bits
from datetime import datetime


class SatHolder:
    """ Manages variable-/bit-names. """

    def __init__(self, varray):
        self.varray = varray
        self.ln = len(varray)

    def pop(self, v=None):
        if v == None:
            if self.ln > 0:
                self.ln -= 1
                return self.varray.pop(0)
            else:
                return None
        else:
            if v in self.varray:
                self.ln -= 1
                self.varray.remove(v)
                return v
            else:
                return None

    def reduce(self, topbits):
        """ topbits: a list of bits, E.G.:[16,6,1]
        taking topbits(3 pieces) from varray
        return a new satholder with new new varray
        After this.self.varray has reverse (high..low) bit-order."""
        varray = [b for b in self.varray if b not in topbits]
        self.varray = list(reversed(topbits[:]))  # [1,6,16]
        self.ln = len(topbits)
        return SatHolder(varray)

    def drop_vars(self, vars):  # drop 1 var or list/set of vars from varray
        if type(vars) == type(0):
            if vars in self.varray:
                self.varray.remove(vars)
                self.ln -= 1
        else:  # list or set
            for v in vars:
                self.drop_vars(v)
        return self

    def clone(self):
        return SatHolder(self.varray[:])

    def get_sats(self, val):
        assert val < (2 ** self.ln)
        satdic = {}
        for ind, vn in enumerate(self.varray):
            v = get_bit(val, ind)
            satdic[vn] = v
        return satdic

    def full_sats(self):
        sats = {v: 2 for v in self.varray}
        return sats
