from basics import get_bit, set_bit, set_bits


class VKlause:
    ''' veriable klause - klause with 1, 2 or 3 bits.
        nov is the value-space bit-count, or number-of-variables
        this vk can be a splited version from a origin vk
        the origin field refs to that (3-bits vk)
        '''

    def __init__(self, kname, dic, nov=0, cvs=set([])):
        self.kname = kname    # this vk can be a partial one: len(bits) < 3)
        self.dic = dic  # { 7:1, 3: 0, 0: 1}, or {3:0, 1:1} or {3:1}
        # all bits, in descending order
        self.bits = sorted(dic.keys(), reverse=True)  # [7,3,0]
        # void bits of the nov-bits
        self.nob = len(self.bits)             # 1, 2 or 3
        self.nov = nov
        self.cvs = cvs  # a set of values (as chvkdic[v]) this vk is in

    def hbit_value(self): # return pair: bit[0], val[bts[0]]
        b = self.bits[0]
        return b, self.dic[b]

    def sat1(self): # only for vk1
        b, v = self.hbit_value()
        return b, int(not v)

    def lbit_value(self):
        b = self.bits[-1]
        return b, self.dic[b]

    def cut_bit(self, bit):
        if self.nob < 2 or not (bit in self.bits):
            raise Exception(f"vk1 cannot be cut or {bit} not in {self.kname} ")
        self.dic.pop(bit)
        self.bits.remove(bit)
        self.nob -= 1

    def clone(self, 
            bits2b_dropped=None,    # bits to be dropped, if this is given:
            delta_cvs=None):        # optional: cvs {'-':[], '+':[]}
        # bits2b_dropped: list of bits to be dropped.
        # They must be the top-bits
        dic = self.dic.copy()
        if delta_cvs:
            cvs = self.cvs.copy()
            if '-' in delta_cvs:
                cvs = cvs - set(delta_cvs['-'])
            elif '+' in delta_cvs:
                cvs = cvs.union(delta_cvs['+'])
        else:
            # cvs = set([])
            cvs = self.cvs.copy()
            
        if bits2b_dropped and len(bits2b_dropped) > 0:
            for b in bits2b_dropped:
                # drop off this bit from dic.
                dic.pop(b, None)
            return VKlause(self.kname.replace('C', 'M'),
                           dic, self.nov, cvs)
        if len(dic) > 0:
            return VKlause(self.kname, dic, self.nov, cvs)
        return None

    def cmprssd_value(self, ref_bits=None):
        ''' compress to 3 bits: [2,1,0] keep the order. get bin-value.
            example: {6:1,4:1,0:0} -> 6(110), {9:0,5:1,1:1} -> 3(011) '''
        if ref_bits:  # ref-bits: [16,6,1]
            cvs = []
            sbits = set(ref_bits).intersection(self.bits)
            vlst = []
            for b in sbits:
                ind = 2 - ref_bits.index(b)  # b == 6, ind: 1; b==16, ind = 2
                vlst.append((ind, self.dic[b]))
                # set_bit(v, ind, self.dic[b])

            for cv in range(8):
                vb_hit = True
                for vbp in vlst:
                    vb_hit = vb_hit and get_bit(cv, vbp[0]) == vbp[1]
                if vb_hit:
                    cvs.append(cv)
            return cvs
        else:
            v = 0
            bs = list(reversed(self.bits))  # ascending: as in [0,4,6]
            for pos, bit in enumerate(bs):
                v = set_bit(v, pos, self.dic[bit])
        return v

    def set_value_and_mask(self):
        ''' For the example klause { 7:1,  5:0,     2:1      }
                              BITS:   7  6  5  4  3  2  1  0
            the relevant bits:        *     *        *
                          self.mask:  1  0  1  0  0  1  0  0
            surppose v = 135 bin(v):  1  0  0  0  0  1  1  1
            x = v AND mask =          1  0  0  0  0  1  0  0
            bits of v left(rest->0):  ^     ^        ^
                  self.value(132)  :  1  0  0  0  0  1  0  0
            This method set self.mask
            '''
        mask = 0
        value = 0
        for k, v in self.dic.items():
            mask = mask | (1 << k)
            if v == 1:
                value = value | (1 << k)
        self.value = value
        self.mask = mask

    def sat_hit_count(self, sat):  # sat can have 1, 2 or 3 bit(s)
        ''' count how many bits in sat are in self.bits, and
            sat[b] ==2 or sat[b] == self.dic[b] 
            '''
        count = 0
        for b, v in sat.items():
            if b in self.bits and (v == 2 or v == self.dic[b]):
                count += 1
        return count

    def hit(self, v):  # hit means here: v let this klause turn False
        if type(v) == type(1):
            if 'mask' not in self.__dict__:
                self.set_value_and_mask()
            fv = self.mask & v
            return not bool(self.value ^ fv)
        elif type(v) == type([]):  # sat-list of [(b,v),...]
            # if self.kname == 'C004':
            #     x = 1
            lst = [(k, v) for k, v in self.dic.items()]
            in_v = True
            for p in lst:
                # one pair/p not in v will make in_v False
                in_v = in_v and (p in v)
            # in_v==True:  every pair in dic is in v
            # in_v==False: at least one p not in v
            return in_v
        elif type(v) == type({}):  # v is a sat-dic
            c = self.sat_hit_count(v)
            return c == self.nob

    def partial_hit_residue(self, sdic):
        total_hit = False
        vk12 = None
        td = {}
        for bit, value in self.dic.items():
            # v = sh.varray[bit]
            if bit in sdic:
                # one mis-match enough makes it not-hit.
                # if not-hit, tdic(empty or not) not used
                if value != sdic[bit]:
                    return False, None
                else:
                    pass
            else:
                td[bit] = value
        if len(td) == 0:
            total_hit = True
        else:
            vk12 = VKlause(self.kname, td)
        return total_hit, vk12

    def equals(self, vk):
        if self.bits != vk.bits:
            return False
        for b in self.bits:
            if self.dic[b] != vk.dic[b]:
                return False
        return True

    def pop_cvs(self, cvs):
        for cv in cvs:
            if cv in self.cvs:
                self.cvs.remove(cv)
            
    def add_cvs(self, cvs):
        for cv in cvs:
            self.cvs.add(cv)
