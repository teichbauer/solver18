from blbmgr import BlbManager
from center import Center
from blockchecker import BlockChecker
from cvnode2 import CVNode2
from hashlib import md5


def merge_vkpair(vk2a, vk2b): # vk2a and vk2b must have common-cvs
    '''
    #         vk2a         vk2b                 return
    #---------------------------------------------------
    # dic1:{ 11:0, 21:1}, dic2:{11:1, 21:1} -> {(21,1)}
    # dic1:{ 11:0, 21:1}, dic2:{11:0, 21:0} -> {(11,0)}
    # dic1:{ 11:0, 21:1}, dic2:{11:1, 21:0} -> {}
    # -------------------------------------
    # it should not be possible to have dict == dict:
    # dic1:{ 11:0, 21:1}, dic2:{11:0, 21:1} -> {(11,0),(21,1)} 
    '''
    s1 = set(tuple(vk2a.dic.items()))
    s2 = set(tuple(vk2b.dic.items()))
    s = s1.intersection(s2)
    if len(s) == 0:
        return None
    if len(s) == 2:
        raise Exception(f'{vk2a.kname} and {vk2b.kname} are duplicates')
    t = s.pop()
    return t


class Layer:
    def __init__(self, bgrid, vk2dic, bitdic, block_bv_dic=None):
        self.bgrid = bgrid
        self.nov = bgrid.nov
        self.vk2dic = vk2dic
        self.cvsats = {cv: {} for cv in bgrid.chvset}
        self.combos = []
        # vk2-bdic : all vk1s will be removed in sort_vks
        self.bdic = self.copy_bdic(bitdic)
        self.bchecker = BlockChecker(self)
        if block_bv_dic != None:  # block_bv_dic==None: for clone
            self.sort_vks(vk2dic)
            self.blbmgr = BlbManager(self, block_bv_dic) 
        # find pairs of vk2s (vka, vkb) bitting on the same 2 bits, and
        # vka.cvs vkb.cvs do have intersection -> tuple_lst  list of tuples:
        #  (vka, vkb, sat_tpl, xcvs)
        tuple_lst = self.proc_pairs()
        if tuple_lst:
            self.pair2blocker(tuple_lst)
        self.eval_combos()
        Center.layers[self.nov] = self
        # generate: self.node2s and self.cvn2s
        self.generate_n2s()

    def fill_cvsats(self, block_dic, lower_lyr):
        pass

    def sort_vks(self, vk2dic):  # fill self.cvks_dic
        self.cvks_dic = {v: set([]) for v in self.bgrid.chvset }
        # only care about vk2s. All vk1s will become sats
        for kn, vk in vk2dic.items():  
            for cv in vk.cvs:
                self.cvks_dic[cv].add(kn)
        x = 0

    def remove_vk2(self, kn):
        # vk2.cvs became empty, remove it from vk2dic, and bdic
        vk = self.vk2dic.pop(kn, None)
        for b in vk.bits:
            if kn in self.bdic[b]:
                self.bdic[b].remove(kn)
                if len(self.bdic[b]) == 0:
                    del self.bdic[b]
        return vk
    
    def generate_n2s(self):
        self.node2s = {}  # {<key>: cvnode2, ...} key: md5 from kns of a cv
        self.cvn2s  = {}  # {<cv>: cvnode2(ref),.. }
        for chv in self.bgrid.chvset:
            m = md5()
            m.update(str(sorted(self.cvks_dic[chv])).encode('utf-8'))
            key = m.hexdigest()
            if key in self.node2s:
                n2 = self.node2s[key]
                n2.cvs.add(chv)
            else:
                n2 = CVNode2(self,chv)
                self.node2s[key] = n2
                if len(self.cvks_dic[chv]) == 0:
                    n2.done = True
                else:
                    for kname in self.cvks_dic[chv]:
                        n2.add_k2(self.vk2dic[kname])
            self.cvn2s[chv] = n2
        x = 0

    def proc_pairs(self):
        # find pairs of vk2s (vka, vkb) bitting on the same 2 bits, and
        # vka.cvs vkb.cvs do have intersection
        pairs = []
        combo_pairs = []
        if 'C0115' in self.vk2dic:
            xx = 9
        vks = tuple(self.vk2dic.values())
        length = len(vks)
        i = 0
        while i < length - 1:
            x = i + 1
            while x < length:
                xvk = vks[x]
                if vks[i].bits == xvk.bits:
                    if vks[i].dic == xvk.dic:
                        combo_pairs.append((vks[i], xvk))
                    else:
                        xcvs = vks[i].cvs.intersection(xvk.cvs)  # common cvs
                        if len(xcvs) > 0:  # vk-i and xvk share xcvs != {}
                            vk1 = merge_vkpair(vks[i], xvk)
                            if vk1:
                                pairs.append((vks[i], xvk, vk1, xcvs))
                x += 1
            i += 1        
        for vka, vkb in combo_pairs:
            self.set_combo(vka, vkb)

        if len(pairs) == 0:
            return None
        return pairs

    def set_combo(self, vka, vkb):
        '''
        # in case vka and vkb having the same bits and the same dic,
        # 1. self.combos.append((vk1, vkb))
        # 2. make a new COMBOn: with uniofied cvs
        # 3 remove vka and vkb, 
        # 4. add COMBOn to vk2dic
        # 5. add COMBOn to self.cvks_dic[cvs]
        '''
        vk2 = vka.clone()
        # vk2-combo-n, shouldn't be more than 9 if this. So n:0..9
        vk2.kname = f"COMBO{len(self.combos)}"
        vk2.cvs = vk2.cvs.union(vkb.cvs)
        self.remove_vk2(vka.kname)    
        self.remove_kn2_from_cvk_dic(vka.cvs, vka.kname)
        self.remove_vk2(vkb.kname)
        self.remove_kn2_from_cvk_dic(vkb.cvs, vkb.kname)
        self.combos.append((vka, vkb))
        vk2.okname = f"{vka.kname}+{vkb.kname}"
        self.vk2dic[vk2.kname] = vk2
        x = 0

    def eval_combos(self):
        '''
        # for every combon vk2, if its bits overlpas with any existing 
        # sat in blbmgr: 
        # 1. pop off the sat-cvs
        # 2. if b in bits: for each bv in sat[b]:{bv0: cvs0, bv1: cvs1}
        #    if vk2[b] == bv, vk2 will create new sat
        # 3. put vk2.kname for all vk2.cvs in self.cvks_dic
        # -------------------------------------------------------------
        '''
        block_bv_dic = {}
        for index in range(len(self.combos)):
            vk2 = self.vk2dic[f'COMBO{index}']
            satbits = set(self.blbmgr.block_bv_dic).intersection(vk2.bits)
            for sb in satbits:
                for bv, cvs in self.blbmgr.block_bv_dic[sb].items():
                    # bv: val on the sat bit, covering cvs
                    xcvs = vk2.cvs.intersection(cvs)
                    vk2.pop_cvs(xcvs)
                    if vk2.dic[sb] != bv: 
                        if len(xcvs) > 0:
                            vk1 = vk2.clone([sb])
                            b, v = vk1.hbit_value()
                            block_bv_dic[b] = { v: xcvs, 'kn': vk1.kname }
            for cv in vk2.cvs:
                self.cvks_dic[cv].add(vk2.kname)
            x = 9
        if len(block_bv_dic) > 0:
            self.blbmgr.add_block_bv_dic(block_bv_dic)


    def pair2blocker(self, pair_tpls): # tpl: (vk-a, vk-b, sat-tpl, comm_cvs)
        block_bv_dic = {}
        for vka, vkb, stpl, cvs in pair_tpls:
            vka1 = vka.clone()
            kna = vka.kname
            vka1.pop_cvs(cvs)  # for every cv in cvs, sat replace vka/vkb
            if len(vka1.cvs) == 0:
                self.remove_vk2(kna)
            else:
                self.vk2dic[kna] = vka1
            self.remove_kn2_from_cvk_dic(cvs, kna)

            vkb1 = vkb.clone()
            knb = vkb.kname
            vkb1.pop_cvs(cvs)
            if len(vkb1.cvs) == 0:
                self.remove_vk2(knb)
            else:
                self.vk2dic[knb] = vkb1
            self.remove_kn2_from_cvk_dic(cvs, knb)

            block_bv_dic[stpl[0]] = { stpl[1]: cvs }
            block_bv_dic[stpl[0]]['kn'] = kna

        self.blbmgr.add_block_bv_dic(block_bv_dic)

    def add_vk2(self, vk2):
        self.vk2dic[vk2.kname] = vk2
        for cv in vk2.cvs:
            self.cvks_dic[cv].add(vk2.kname)

    def remove_kn2_from_cvk_dic(self, cvs, kn2):
        for cv in cvs:
            # cv may be missing in cvks_dic, in that case : []
            if kn2 in self.cvks_dic.get(cv, []):  
                self.cvks_dic[cv].remove(kn2)

    def copy_bdic(self, bdic):
        dic = {}
        for bit, val in bdic.items():
            dic[bit] = list(val)
        return dic

    def copy_cvks_dic(self, cvks_dic):
        dic = {}
        for cv, val in cvks_dic.items():
            dic[cv] = set(val)
        return dic
