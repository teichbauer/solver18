from center import Center
from pathnode import PathNode
from blocker import Blocker
from basics import sortdic, print_clause_dic, print_bitdic

class Cluster(PathNode):
    clusters = {}
    groups = {}

    def __init__(self, name, n2node):
        self.name = name
        if type(n2node) == Cluster:  # n2node is a cluster clone it
            self.n2 = n2node.n2
            self.nov = n2node.nov
            self.Layer1 = n2node.Layer1
            if 'Layer2' in n2node.__dict__:
                self.Layer2 = n2node.Layer2
            else:
                self.Layer2 = None
            self.sat = {b: v for b, v in n2node.sat.items()}
            self.bitdic = {b:s.copy() for b, s in n2node.bitdic.items() }
            self.clauses = n2node.clauses.copy()
            self.headsatbits = n2node.headsatbits.copy()
            self.block = n2node.block.clone()
            self.pblock = {}
            return # cloning done
        # type(n2node) == CVNode2
        self.n2 = n2node
        self.Layer1 = n2node.Layer
        self.headsatbits = n2node.Layer.bgrid.bitset.copy()
        self.nov = n2node.Layer.nov
        bdic = {b:s.copy() for b, s in n2node.bitdic.items()}
        super().__init__(n2node.sat.copy(), bdic, n2node.clauses.copy())
        self.add_sat(n2node.sat_dic(name[1]))
        self.block = Blocker(self)

    def clone(self):  # only for grown cluster (with 2 Layers: Layer1, Layer2)
        clu = Cluster(tuple(self.name), self)
        return clu
    
    def remove_clause(self, kn):
        if kn in self.clauses:
            vk = self.clauses.pop(kn)
            for bit in vk.bits:
                self.bitdic[bit].remove(kn)
                if len(self.bitdic[bit]) == 0:
                    del self.bitdic[bit]
        
    def add_n2(self, n2, n2cv):
        self.Layer2 = n2.Layer
        sat = n2.sat_dic(n2cv)
        if not self.add_sat(sat):
            return None
        for cl in n2.clauses.values():
            if not self.add_k2(cl):
                return None
        self.headsatbits = self.headsatbits.union(self.Layer2.bgrid.bitset)
        rsat = {}
        for b,sv in self.sat.items():
            if b not in self.headsatbits:
                rsat[b] = self.sat[b]
        return rsat

    def grow_with_filter(self, lower_Layer, filters):
        for cv, cvn2 in lower_Layer.cvn2s.items():
            clu = self.clone()
            if type(clu.name) == tuple:
                clu.name = [clu.name, (lower_Layer.nov, cv)]
            else:
                clu.name.append((lower_Layer.nov, cv))
            excl_kns = []
            sat2b_added = []
            for filter in filters:  # filter: [set(lower-cvs), kn, <sat-dic>]
                if cv in filter[0]:
                    kn, sat = filter[1:]
                    excl_kns.append(kn)
                    sat2b_added.append(sat)
            for kn in excl_kns:
                clu.remove_clause(kn)
            for s in sat2b_added:
                if not clu.add_sat(s):
                    return
            new_Layer_sat = clu.add_n2(cvn2, cv)
            name = tuple(clu.name)
            if clu.grow_cvsats(new_Layer_sat):
                Cluster.groups.setdefault(self.nov, []).append((name, clu))
        x = 0

    def grow_cvsats(self, new_sat):
        return True

    def grow(self, lower_Layer):
        for cv, cvn2 in lower_Layer.cvn2s.items():
            clu = Cluster(self.name, self.n2.clone())
            if clu.add_sat(self.sat):
                if type(clu.name) == tuple:
                    clu.name = [clu.name, (lower_Layer.nov, cv)]
                else:
                    clu.name.append((lower_Layer.nov, cv))
                clu.add_n2(cvn2, cv)
                name = tuple(clu.name)
                Cluster.groups.setdefault(self.nov, []).append((name, clu))
        x = 0

    def body_sat(self):
        bits = set(self.sat) - self.headsatbits
        dset = {b: self.sat[b] for b in bits}
        return bits, dset

    def test_sat(self, tsat):
        for b, v in tsat.items():
            assert(b in self.sat), "tsat not qualified"
            if self.sat[b] != v:
                if b in self.headsatbits:
                    if b in self.Layer1.bgrid.bits:
                        bgrid = self.Layer1.bgrid
                        Layer_nov = self.Layer1.nov
                    else:
                        bgrid = self.Layer2.bgrid
                        Layer_nov = self.Layer2.nov
                    return True, (Layer_nov, bgrid.bv2cvs(b, self.sat[b])[0])
                return True, None
        return False, None

    def merge_cluster(self, cl):
        if (54,2) in self.name and (51,1) in self.name and \
              (48,1) in cl.name and (45,0) in cl.name:
            x = 8
        c = self.clone()
        c.name += cl.name
        if not c.block.update(cl.block):
            return None
        if not c.pblock_filter(self.block.pblock_dic, cl):
            return None
        if c.add_sat(cl.sat):
            old_sat = c.sat.copy()
            for clause in cl.clauses.values():
                if not c.add_k2(clause):
                    return None
            lower_nov = cl.nov - 6
            new_bits = set(c.sat) - set(old_sat)
            # in case there are new-sat(bits), 
            # see if lower Layers' head on them
            if len(new_bits) > 0:
                lnov = lower_nov
                while lnov >= Center.minnov:
                    bgrd = Center.snodes[lnov].Layer.bgrid
                    bs = new_bits.intersection(bgrd.bitset) # Layer bit overlaps
                    for b in bs:
                        v = c.sat[b]
                        c.block.add_block((lnov, bgrd.bv2cvs(b, v)[1]))
                    lnov -= 3
            return (c, lower_nov)
        return None

    def block_filter(self, grp):
        newgrp = []
        for g in grp:
            if not self.block.name_inblock(g[0]):
                newgrp.append(g[1])
        return newgrp

    def set_pblock(self, Layers):
        bits = set(self.bitdic)
        for Layer in Layers:
            headbits = Layer.bgrid.bitset.intersection(self.bitdic)
            print(f"{self.name}->{Layer.nov}: head-bits: {headbits}")
            if len(headbits) > 0:
                self.block.set_pblock(headbits, Layer)

    def pblock_filter(self, pbdic, lower_clustr):
        ss = set(lower_clustr.name)
        for nv,cv in ss:
            if nv in pbdic and cv in pbdic[nv]:
                for kn, op in pbdic[nv][cv].items():
                    self.remove_clause(kn)
                    if op != '-':  # op is a new sat
                        if not self.add_sat(op):
                            return False
        # no conflict that causes this cluster to hit
        return True
