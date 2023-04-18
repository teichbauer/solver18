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
            self.layer1 = n2node.layer1
            if 'layer2' in n2node.__dict__:
                self.layer2 = n2node.layer2
            else:
                self.layer2 = None
            self.sat = {b: v for b, v in n2node.sat.items()}
            self.bitdic = {b:s.copy() for b, s in n2node.bitdic.items() }
            self.clauses = n2node.clauses.copy()
            self.headsatbits = n2node.headsatbits.copy()
            self.block = n2node.block.clone()
            self.pblock = {}
            return # cloning done
        # type(n2node) == CVNode2
        self.n2 = n2node
        self.layer1 = n2node.layer
        self.headsatbits = n2node.layer.bgrid.bitset.copy()
        self.nov = n2node.layer.nov
        bdic = {b:s.copy() for b, s in n2node.bitdic.items()}
        super().__init__(n2node.sat.copy(), bdic, n2node.clauses.copy())
        self.add_sat(n2node.sat_dic(name[1]))
        self.block = Blocker(self)

    def clone(self):  # only for grown cluster (with 2 layers: layer1, layer2)
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
        self.layer2 = n2.layer
        self.nxt_nv = self.layer2.nov - 3

        sat = n2.sat_dic(n2cv)
        if not self.add_sat(sat):
            return None
        for cl in n2.clauses.values():
            if not self.add_k2(cl):
                return None
        self.headsatbits = self.headsatbits.union(self.layer2.bgrid.bitset)
        rsat = {}
        for b,sv in self.sat.items():
            if b not in self.headsatbits:
                rsat[b] = self.sat[b]
        return rsat

    def grow_with_filter(self, lower_layer, filters):
        for cv, cvn2 in lower_layer.cvn2s.items():
            clu = self.clone()
            if type(clu.name) == tuple:
                clu.name = [clu.name, (lower_layer.nov, cv)]
            else:
                clu.name.append((lower_layer.nov, cv))
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
            new_layer_sat = clu.add_n2(cvn2, cv)
            name = tuple(clu.name)
            if self.nov - 6 > Center.minnov:
                if clu.build_cvsats(Center.layers[self.nov - 6]):
                    Cluster.groups.setdefault(self.nov, []).append((name, clu))
        self.nxt_nv = lower_layer.nov - 3


    def set_satfilter(self, lyr):
        ''' the self.sat can
            1. touch lyr's head-bits, resulting cvs limitation
            2. touch lyr.bitdic: 
              2.1 making some vk2 -> sat under vk.cvs
              2.2 if a vk has 2 bits touched sat - hit/voided
        '''
        self.cvsats = {}
        lheadbits = lyr.bgrid.bitset # ---------- 1 ---------------
        cvs = lyr.bgrid.chvset  # all cvs of lyr
        head_sat_bits = lheadbits.intersection(self.sat)
        if len(head_sat_bits) > 0:
            for cvtb in head_sat_bits:
                allowed = lyr.bgrid.bv2cvs(cvtb, self.sat[cvtb])[0]
                cvs = cvs.intersection(allowed)
        dic = self.cvsats.setdefault(lyr.nov, {})
        dic['cvs'] = list(cvs)
        sat_bs = set(self.sat)   # ---------- 2 ---------------
        bs = sat_bs.intersection(lyr.bdic)
        kns = set()
        for b in bs:
            kns.update(lyr.bdic[b])
        for kn in kns:
            vk = lyr.vk2dic[kn]
            tbits = sat_bs.intersection(vk.bits)
            if len(tbits) == 2:
                if vk.hit(self.sat):
                    for cv in vk.cvs:
                        if cv in dic['cvs']:
                            dic['cvs'].remove(cv)
                            dic.pop(cv, None)
                            if len(dic['cvs']) == 0:
                                return
                else:
                    for cv in vk.cvs:
                        if cv in dic['cvs']:
                            dic.setdefault(cv,[]).append((vk.kname, None))
            else:  # 1 bit of vk in sat
                b = tbits.pop()
                if vk.dic[b] == self.sat[b]:
                    obit = vk.other_bit(b)
                    nsat = {obit: int(not vk.dic[obit])}
                    if obit in self.sat:  # new sat touched self.sat
                        if self.sat[obit] != nsat[obit]: # sat-conflict
                            for cv in vk.cvs:            # remove this cv
                                if cv in dic['cvs']:     # if it is in dic[cvs]
                                    dic['cvs'].remove(cv) # from dic[cvs]
                                    dic.pop(cv, None)    # pop out cv totally
                                    if len(dic['cvs']) == 0:
                                        return None
                    else: # nsat does not touch self.sat
                        for cv in vk.cvs:
                            if cv in dic['cvs']:
                                dic.setdefault(cv,[]).append((vk.kname, nsat))
                else:  # vk.dic[b] != self.sat[b] -> this vk be dropped
                    for cv in vk.cvs:
                        if cv in dic['cvs']:
                            dic.setdefault(cv,[]).append((vk.kname, None))
        return self.cvsats[lyr.nov]
    
    def build_cvsats(self, lyr):
        dic = self.set_satfilter(lyr)
        if not dic: return None
        # lyr-head-bit touch cluster(self).tail(vk2-bits)?
        head_tail_bits = lyr.bgrid.bitset.intersection(self.bitdic)
        if len(head_tail_bits) > 0:
            for b in head_tail_bits:
                for kn in self.bitdic[b]:
                    cl = self.clauses[kn]
                    obit = cl.other_bit(b)
                    sat = {obit: int(not cl.dic[obit])}
                    cvs, ncvs = lyr.bgrid.bv2cvs(b, cl.dic[b])
                    for cv in dic['cvs']:
                        # when 3 vals in an ele in lst: cut-off from cluster
                        lst = dic.setdefault(cv,[])
                        if cv in cvs:
                            t = ('cluster', cl.kname, sat.copy())
                            if t not in lst:
                                lst.append(t) # add sat
                        elif cv in ncvs:
                            t = ('cluster', cl.kname, None)
                            if t not in lst:
                                lst.append(t) # no sat
        # find double (both bits)touch vk-pairs btwn lyr.vk2 and self.vk2s
        touch_bits = set(lyr.bdic).intersection(self.bitdic)
        kns = set()
        for b in touch_bits:    # collect lyr-kns touching self.clauses
            kns.update(self.bitdic[b])
        kns = kns.intersection(Center.vk2pairs)
        for kn in kns:
            for xkn in Center.vk2pairs[kn]:
                if xkn in lyr.vk2dic:
                    vk = lyr.vk2dic[xkn]
                    res = self.clauses[kn].evaluate_overlap(vk)
                    if res == 1:
                        continue
                    for cv in vk.cvs:
                        if cv in dic['cvs']:
                            # when 2 vals in an ele in lst, cut-off from lyr
                            lst = dic.setdefault(cv,[])
                            if type(res) == dict:
                                b,v = res.popitem()
                                nsat = {b: int(not v)}
                                lst.append((vk.kname, nsat))  # add sat
                            elif res == 0:
                                lst.append((vk.kname, None))  # no sat
        return True
    # end of: ----- def build_cvsats(self, lyr):

    def grow_layercv(self, lyr, cv, filters):
        cvn2 = lyr.cvn2s[cv]
        clu = self.clone()
        lyr_filter = {}
        for ftr in filters:
            if ftr[0] == 'cluster':
                clu.remove_clause(ftr[1])
                if ftr[2]:
                    if not clu.add_sat(ftr[2]):
                        print(f"lyr({lyr.nov}-{cv})-cluster-kn:{ftr[1]}: sat:{ftr[2]}")
                        return False
            else:
                lyr_filter[ftr[0]] = ftr[1]
        for kn, cl in cvn2.clauses.items():
            if kn in lyr_filter:
                st = lyr_filter[kn]
                if st:
                    if not clu.add_sat(st):
                        print(f"lyr({lyr.nov}-{cv})-kn:{kn}: sat:{st}")
                        return False
                continue
            if not clu.add_k2(cl):
                print(f"lyr({lyr.nov}-{cv})-kn:{cl.kname}")
                return False
        nxt_nv = lyr.nov - 3
        clu.name = self.name[:]
        clu.name.append((lyr.nov, cv))
        if nxt_nv >= Center.minnov:
            next_lyr = Center.layers[nxt_nv]
            if not clu.build_cvsats(next_lyr):
                print(f"lyr({lyr.nov}-{cv}): no [cvs]")
                return False
            clu.nxt_nv = nxt_nv
        else:
            clu.nxt_nv = -1
        return clu
        


    def grow(self, lower_layer):
        for cv, cvn2 in lower_layer.cvn2s.items():
            clu = Cluster(self.name, self.n2.clone())
            if clu.add_sat(self.sat):
                if type(clu.name) == tuple:
                    clu.name = [clu.name, (lower_layer.nov, cv)]
                else:
                    clu.name.append((lower_layer.nov, cv))
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
                    if b in self.layer1.bgrid.bits:
                        bgrid = self.layer1.bgrid
                        layer_nov = self.layer1.nov
                    else:
                        bgrid = self.layer2.bgrid
                        layer_nov = self.layer2.nov
                    return True, (layer_nov, bgrid.bv2cvs(b, self.sat[b])[0])
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
            # see if lower layers' head on them
            if len(new_bits) > 0:
                lnov = lower_nov
                while lnov >= Center.minnov:
                    bgrd = Center.snodes[lnov].layer.bgrid
                    bs = new_bits.intersection(bgrd.bitset) # layer bit overlaps
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

    def set_pblock(self, layers):
        bits = set(self.bitdic)
        for layer in layers:
            headbits = layer.bgrid.bitset.intersection(self.bitdic)
            print(f"{self.name}->{layer.nov}: head-bits: {headbits}")
            if len(headbits) > 0:
                self.block.set_pblock(headbits, layer)

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
