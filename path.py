from pathnode import PathNode

class Path(PathNode):
    def __init__(self, name, sat, bitdic, clauses):
        self.name = name
        # from super/PathNode:
        #   .sat
        #   .bitdic - {<bit>:set{kn,kn,..}, <bit>:set{}, ...}
        #   .clauses
        # -------------------------
        # bdic: deeper copy of bitdic than bitdic.copy():
        bdic = {b:s.copy() for b, s in bitdic.items()}
        super().__init__(sat.copy(), bdic, clauses.copy())

    # def get_leg(self, name):
    #     return self.sat, self.bitdic, self.clauses

    def clone(self):
        p = Path(self.name.copy(), self.sat, self.bitdic, self.clauses)
        return p

    def add_n2(self, n2, n2cv):
        sat = n2.sat_dic(n2cv)
        if not self.add_sat(sat):
            return False
        else:
            for cl in n2.clauses.values():
                if not self.add_k2(cl):
                    return False
            return True
