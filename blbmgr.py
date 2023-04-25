from basics import flip_tuple_bitvalue

class BlbManager:
    def __init__(self, owner, block_bv_dic=None):
        self.owner = owner
        self.block_bv_dic = {}
        # cbdic (conditional block-dic):
        # {<nov>:{
        #   <kn>: (  - vk.kname that has 1 bit in <nov>-bgrid-bits
        #   (cvs),   - cvs of the layer[nov] this kn has 1 bit
        #   (local-cvs)  - cvs in cvks_dic the kn to be removed
        #   (b,v) )  - bit and val which triggers block
        #              if None in place of (b,v): every local-cv are blocked
        #   <kn>:(),..},
        # <nov>:{},
        # }
        self.cbdic = {} 
        if block_bv_dic:
            self.add_block_bv_dic(block_bv_dic)

    def cbdic_oppo(self, nv, tpl):
        if nv in self.cbdic:
            nblck = flip_tuple_bitvalue(tpl[2], 1) # (12,0)->(12,1)
            for kn, t in self.cbdic[nv].items():
                if nblck == t[2]:
                    cmm_lnv_cvs = tpl[0].intersection(t[0])
                    cmm_hnv_cvs = tpl[1].intersection(t[1])
                    if len(cmm_hnv_cvs) > 0 and len(cmm_lnv_cvs) > 0:
                        dic = {
                               self.owner.nov: tuple(cmm_hnv_cvs),
                               nv: tuple(cmm_lnv_cvs)
                        }
                        return dic
        return None

    def add_cbd(self, nv, kn, tpl):
        if tpl[2] != None:
            oppo = self.cbdic_oppo(nv, tpl)
            if oppo:
                self.owner.bchecker.block_dic.setdefault('*',[]).append(oppo)
        d = self.cbdic.setdefault(nv, {})
        d[kn] = tpl
        x = 0

    def add_block_bv_dic(self, block_bv_dic):
        for bit in block_bv_dic:
            ddic = block_bv_dic[bit].copy()
            kname = ddic.pop('kn')
            cdic = self.owner.bchecker.checkdic.setdefault(bit, {})
            for bv, xcvs in ddic.items():
                lst = cdic.setdefault(bv,[])
                bd = self.block_bv_dic.setdefault(bit, {})
                cvs = bd.setdefault(bv, set([]))
                for cv in xcvs:
                    if cv not in cvs:
                        cvs.add(cv)
                lst.append({'kn': kname, self.owner.nov: cvs})
        block_bv_dic = self.expand_bmap(block_bv_dic)
        if len(block_bv_dic) > 0:
            self.add_block_bv_dic(block_bv_dic)

    def expand_bmap(self, block_bv_dic):
        new_block_bv_dic = {}
        while len(block_bv_dic) > 0:  # bits is a set
            bit, bv_cvs_dic = block_bv_dic.popitem()
            # kn2s = bdic.get(bit, []) may ge modified, so use a copy
            kn2s = self.owner.bdic.get(bit, []).copy()
            if len(kn2s) == 0:
                continue
            xkn = bv_cvs_dic.pop('kn', None)
            for kn2 in kn2s:
                vk2 = self.owner.vk2dic[kn2]
                for bv,  xcvs in bv_cvs_dic.items():
                    comm_cvs = vk2.cvs.intersection(xcvs)
                    if len(comm_cvs) > 0:
                        # since vk2 in vk2dic is a ref, and here the vk2
                        # is modified, replace this vk2 with a clone, so tha
                        # the modification will not harm the original vk2
                        vk2_clone = vk2.clone()
                        self.owner.vk2dic[kn2] = vk2_clone

                        vk2_clone.pop_cvs(comm_cvs)
                        if len(vk2_clone.cvs) == 0:
                            self.owner.remove_vk2(kn2)

                        self.owner.remove_kn2_from_cvk_dic(comm_cvs, kn2)

                        # suppose {bit:bv} is blocking, meaning that
                        # bv cannot happen - if it happens, every cv in comm_cvs
                        # -> self.owner.cvks_dic[cv] will be hit: turning False
                        # so, only (NOT bv) is possible.
                        # but if vk2[bit] == bv, then vk2 is voided by (NOT bv)
                        if vk2_clone.dic[bit] == bv:
                            continue
                        # if vk2[bit] != bv, this vk[bit] == (NOT bv) and this 
                        # will knock off this b:v, generating a new block:
                        # vk2[b]: v. here b is the other bit in vk2
                        vk1 = vk2_clone.clone([bit]) # vk2 drops bit -> vk1
                        b, v = vk1.hbit_value()
                        new_block_bv_dic.setdefault(b,{})[v] = comm_cvs
                        new_block_bv_dic[b]['kn'] = vk2.kname
        return new_block_bv_dic

    def clone_block_bv_dic(self):
        dic = {}
        for b, d in self.block_bv_dic.items():
            dic[b] = {}
            for bv, cvs in d.items():
                dic.setdefault(b, {})[bv] = cvs.copy()
        return dic
