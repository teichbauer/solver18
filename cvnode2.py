from pathnode import PathNode

class CVNode2(PathNode):
    def __init__(self, tail, cv):
        super().__init__()
        self.tail = tail
        if type(cv) == int:
            self.cvs = set([cv])
        elif type(cv) == set:
            self.cvs = cv
        self.done = False  # False, True, "conflict"
        self.lower_blocks = set()

    def clone(self):
        n2 = CVNode2(self.tail, self.cvs.copy())
        n2.bitdic = {b:s.copy() for b, s in self.bitdic.items() }
        n2.clauses = self.clauses.copy()
        n2.done = self.done
        n2.lower_blocks = self.lower_blocks.copy()
        return n2

    def add_sat(self, sat):
        '''
        a sat bit:value pair like {5:1} means: the value on bit 5 must be 1,
        othewise this will make F=()^()^.. fail. So, if a k2 has bit 5,
        and: a): bv is 1 -> this ke can eliminate bit-5, k2 becomes sat-bit;
        b), bv is 0 -> this k2 can be eliminated, the 5:1 makes it so.
        '''
        res = super().add_sat(sat)
        if not res:
            self.done = 'conflict'
            return False
        return True

    def sat_dic(self, cv):
        sdic = self.sat.copy()
        sdic.update(self.tail.bgrid.cv_sats[cv])
        return sdic

    def add_cvn2(self, cvn2):
        for b,v in cvn2.sat.items():
            if not self.add_sat({b:v}):
                return False
        for cl in cvn2.clauses.values():
            if not self.add_k2(cl):
                return False
        return True
        


