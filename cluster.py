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
            self.tail1 = n2node.tail1
            if 'tail2' in n2node.__dict__:
                self.tail2 = n2node.tail2
            else:
                self.tail2 = None
            self.sat = {b: v for b, v in n2node.sat.items()}
            self.bitdic = {b:s.copy() for b, s in n2node.bitdic.items() }
            self.clauses = n2node.clauses.copy()
            self.headsatbits = n2node.headsatbits.copy()
            self.block = n2node.block.clone()
            self.pblock = {}
            return # cloning done
        # type(n2node) == CVNode2
        self.n2 = n2node
        self.tail1 = n2node.tail
        self.headsatbits = n2node.tail.bgrid.bitset.copy()
        self.nov = n2node.tail.nov
        bdic = {b:s.copy() for b, s in n2node.bitdic.items()}
        super().__init__(n2node.sat.copy(), bdic, n2node.clauses.copy())
        self.add_sat(n2node.sat_dic(name[1]))
        self.block = Blocker(self)

    def clone(self):  # only for grown cluster (with 2 tails: tail1, tail2)
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
        self.tail2 = n2.tail
        sat = n2.sat_dic(n2cv)
        if not self.add_sat(sat):
            return None
        for cl in n2.clauses.values():
            if not self.add_k2(cl):
                return None
        self.headsatbits = self.headsatbits.union(self.tail2.bgrid.bitset)
        rsat = {}
        for b,sv in self.sat.items():
            if b not in self.headsatbits:
                rsat[b] = self.sat[b]
        return rsat

    def grow_with_filter(self, lower_tail, filters):
        for cv, cvn2 in lower_tail.cvn2s.items():
            dic = {}
            for filter in filters:
                if cv in filter[0]:
                    kn, sat = filter[1:]
                    dic.setdefault('kns',[]).append(kn)
                    dic.setdefault('sats',[]).append(sat)
            clu = self.clone()
            if type(clu.name) == tuple:
                clu.name = [clu.name, (lower_tail.nov, cv)]
            else:
                clu.name.append((lower_tail.nov, cv))
            for s in dic['sats']:
                if not clu.add_sat(s):
                    return
            for kn in dic['kns']:
                clu.remove_clause(kn)
            new_tail_sat = clu.add_n2(cvn2, cv)
            name = tuple(clu.name)
            Cluster.groups.setdefault(self.nov, []).append((name, clu))
        x = 0

    def grow(self, lower_tail):
        for cv, cvn2 in lower_tail.cvn2s.items():
            clu = Cluster(self.name, self.n2.clone())
            if clu.add_sat(self.sat):
                if type(clu.name) == tuple:
                    clu.name = [clu.name, (lower_tail.nov, cv)]
                else:
                    clu.name.append((lower_tail.nov, cv))
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
                    if b in self.tail1.bgrid.bits:
                        bgrid = self.tail1.bgrid
                        tail_nov = self.tail1.nov
                    else:
                        bgrid = self.tail2.bgrid
                        tail_nov = self.tail2.nov
                    return True, (tail_nov, bgrid.bv2cvs(b, self.sat[b])[0])
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
            # in case there are new-sat(bits), see if lower tails' head on them
            if len(new_bits) > 0:
                lnov = lower_nov
                while lnov >= Center.minnov:
                    bgrd = Center.snodes[lnov].tail.bgrid
                    bs = new_bits.intersection(bgrd.bitset) # tail bit overlaps
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

    def set_pblock(self, tails):
        bits = set(self.bitdic)
        for tail in tails:
            headbits = tail.bgrid.bitset.intersection(self.bitdic)
            print(f"{self.name}->{tail.nov}: head-bits: {headbits}")
            if len(headbits) > 0:
                self.block.set_pblock(headbits, tail)

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
