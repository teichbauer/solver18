from clause import Clause

class PathNode:
    def __init__(self, sat=None, bitdic=None, clauses= None):
        self.sat = sat if sat else {}
        self.bitdic = bitdic if bitdic else {}     # {<bit>:set{kname,...},..}
        self.clauses = clauses if clauses else {}  # {<kname>: k2-clause,...}

    def clone(self):
        p = PathNode()
        p.bitdic = {b:s.copy() for b, s in self.bitdic.items() }
        p.clauses = self.clauses.copy()
        p.sat = self.sat.copy()
        return p
    
    def remove_clause(self, kn):
        if kn in self.clauses:
            vk = self.clauses.pop(kn)
            for bit in vk.bits:
                self.bitdic[bit].remove(kn)
                if len(self.bitdic[bit]) == 0:
                    del self.bitdic[bit]

    def add_k2(self, vk):  # vk can be clause, or vklause
        dic = vk.dic.copy()
        dicbits = set(dic)
        touch = dicbits.intersection(self.sat)
        if len(touch) > 0:
            b = touch.pop()
            if dic[b] == self.sat[b]:
                dic.pop(b)
                sbit, sval = dic.popitem()
                return self.add_sat({sbit: int(not sval)})
            else:
                return True
        touch = dicbits.intersection(self.bitdic)
        if type(vk) == Clause:
            cl = Clause(vk.kname, dic, vk.mark)
        else:
            cl = Clause(vk.kname, dic, (vk.nov, tuple(vk.cvs)))
            if 'okname' in vk.__dict__:
                cl.okname = vk.okname

        if len(touch) == 2:   # 2 bits in self.bitdic
            # collect kns that share 1 or 2 bit
            kns = set()
            for bit in dicbits:
                for kn in self.bitdic[bit]:
                    kns.add(kn)
            # vk(kn) with shares 2 bit as cl: -> dkns
            dkns = set()
            while len(kns) > 0:
                kn = kns.pop()
                if self.clauses[kn].bits == cl.bits:
                    dkns.add(kn)
            # among dkns, find kn's ev
            sat_added = False
            for kn in dkns:
                clx = self.clauses[kn]
                ev = cl.evaluate_overlap(clx)
                # vk has a duplicate (ev == 0): dont add it, stop here 
                if ev == 0: return True  
                # ev != 1 : ev is a dic
                if ev != 1: 
                    sat_added = True  # vk becomes a new sat that is now added
                    b, v = ev.popitem()
                    res = self.add_sat({b: int(not v)})
                    if not res: 
                        return False  # conflict: return False
                    # if there is no conflict, go to next kn in dkns
                # in case ev == 1, vk is not entangled, add it in the following
            # if vk added as a new sat, return True
            if sat_added: return True

        for bit in dicbits:
            self.bitdic.setdefault(bit, set()).add(vk.kname)
        self.clauses[vk.kname] = cl
        return True

    def add_sat(self, input_sat):
        '''
        a sat bit:value pair like {5:1} means: the value on bit 5 must be 1,
        othewise this will make F=()^()^.. fail. So, if a k2 has bit 5,
        and: a): bv is 1 -> this ke can eliminate bit-5, k2 becomes sat-bit;
        b), bv is 0 -> this k2 can be eliminated, the 5:1 makes it so.
        '''
        sat = input_sat.copy()
        while len(sat) > 0:
            sbit, sval = sat.popitem()
            if sbit in self.sat:
                if self.sat[sbit] == sval:
                    continue
                else:
                    return False # self.done = "conflict"
            else:
                self.sat[sbit] = sval
            new_sat = {}
            while sbit in self.bitdic:
                kn = self.bitdic[sbit].pop()
                if len(self.bitdic[sbit]) == 0:
                    del self.bitdic[sbit]
                cl = self.clauses.pop(kn)  # cl is no more in self.clauses
                obit = cl.other_bit(sbit)

                # clear cl's obit from bitdic
                if obit in self.bitdic:
                    self.bitdic[obit].remove(kn)
                if len(self.bitdic[obit]) == 0:
                    del self.bitdic[obit]

                if cl.dic[sbit] == sval:
                    new_sat[obit] = int(not cl.dic[obit])
                    # news[obit] = new_sat[obit]
                else:
                    pass
            if len(new_sat) > 0:
                res = self.add_sat(new_sat)
                if not res:
                    return False
        return True
