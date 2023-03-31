from basics import set_bit, get_bit
from vklause import VKlause


class BitGrid:
    BDICS = {
        0: {2: 0, 1: 0, 0: 0},
        1: {2: 0, 1: 0, 0: 1},
        2: {2: 0, 1: 1, 0: 0},
        3: {2: 0, 1: 1, 0: 1},
        4: {2: 1, 1: 0, 0: 0},
        5: {2: 1, 1: 0, 0: 1},
        6: {2: 1, 1: 1, 0: 0},
        7: {2: 1, 1: 1, 0: 1},
    }

    def __init__(self, choice, nov):  #
        # grid-bits: high -> low, descending order
        self.bits = tuple(reversed(choice["bits"]))  # bits [1, 6, 16]
        self.bitset = set(choice["bits"])
        self.avks = choice["avks"]
        self.nov = nov
        self.covers = tuple(vk.cmprssd_value() for vk in self.avks)
        chlst = [v for v in range(8) if v not in self.covers]
        # self.chvset = frozenset(chlst)
        self.chvset = set(chlst)
        self.cv_sats = {}
        for cv in chlst:
            self.cv_sats[cv] = {
                self.bits[b]: v for b, v in self.BDICS[cv].items()
            }

    def bits_cvs(self, dic):
        '''
        example: {46:1, 44:1, 36:0} -> {0, 1, 2, 3, 4, 5, 7} (6 is hit)
         from [*,*,*] (000,001,010,...) - [1,1,0] ->(0,1,2,3,4,5,7)
        '''
        bits = list(dic)
        g = [2, 1, 0]
        cvs = set([])
        v = 0
        while len(bits) > 0:
            b = bits.pop()
            val = dic[b]
            ind = self.bits.index(b)
            g.remove(ind)
            v = set_bit(v, ind, val)
        cvs = self.vary_bits(v, g, cvs)
        cvs = cvs.difference(self.covers)
        return cvs

    def bv2cvs(self, b, v):
        ''' in case (nov.21)-self.bits: [54, 50, 11], and for a (b,v):(50,1),
            return a list of cvs:
        010 / cv:2  - {54:0, 50:1, 11:0}
        011 / cv:3  - {54:0, 50:1, 11:1}
        110 / cv:6  - {54:1, 50:1, 11:0}
        111 / cv:7  - {54:1, 50:1, 11:1}
        return cvs:(2,3,6,7); if avk.v is 3, take it out, getting: (2,6,7)
        '''
        if b not in self.bits: return None
        ind = self.bits.index(b)
        cvs = []
        ncvs = []
        for cv in self.chvset:
            if get_bit(cv, ind) == v:
                cvs.append(cv)
            else:
                ncvs.append(cv)
        return cvs, ncvs


    def grid_sat(self, cv):
        # return a copy of 3 bit/bv - sat for the given cv
        return {self.bits[b]: v for b, v in self.BDICS[cv].items()}

    def hit(self, satdic):
        for avk in self.avks:
            if avk.hit(satdic):
                return True
        return False

    def reduce_vk(self, vk):
        # vk is vk3 with 1 or 2 bit(s) in self.bits,
        # but not 3 - vk is not a avk (totally contained in self.bits)
        scvs, outdic = self.cvs_and_outdic(vk)
        cvs = self.chvset.intersection(scvs)
        return VKlause(vk.kname, outdic, self.nov, cvs)

    def vary_bits(self, val, bits, cvs):
        # set val[b] = 0 and 1 for each b in bits, 
        # collecting each val after each setting into cvs
        if len(bits) == 0:
            cvs.add(val)
        else:
            bit = bits.pop()
            for v in (0, 1):
                nval = set_bit(val, bit, v)
                if len(bits) == 0:
                    cvs.add(nval)
                else:
                    self.vary_bits(nval, bits[:], cvs)
        return cvs

    def cvs_and_outdic(self, vk):  # vk is vk3 with 1 or 2 bit(s) in self.bits
        g = [2, 1, 0]  #
        # cvs may contain 2 or 4 values in it
        cvs = set([])
        # vk's dic values within self.grid-bits, forming a value in (0..7)
        # example: grids: (16,6,1), vk.dic:{29:0, 16:1, 1:0} has
        # {16:1,1:0} iwithin grid-bits, forming a value of 4/1*0 where
        # * is the variable value taking 0/1 - that will be set by
        # self.vary_bits call, but for to begin, set v to be 4/100
        v = 0
        out_dic = {}  # dic with 1 or 2 k/v pairs, for making vk12
        for b in vk.dic:
            if b in self.bits:
                ind = self.bits.index(b)  # self.bits: descending order
                g.remove(ind)
                v = set_bit(v, ind, vk.dic[b])
            else:
                out_dic[b] = vk.dic[b]
        # get values of all possible settings of untouched bits in g
        cvs = self.vary_bits(v, g, cvs)
        return cvs, out_dic
