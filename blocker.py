from center import Center

class Blocker:
    def __init__(self, parent):
        self.parent = parent
        self.nov = parent.nov
        self.block_dic = {}
        self.block_set = set()
        self.pblock_dic = {}

    def clone(self):
        c = Blocker(self.parent)
        c.block_dic = {nov: lst.copy() for nov, lst in self.block_dic.items()}
        c.block_set = self.block_set.copy()
        return c
    
    def set_pblock(self, bits, layer):
        for bit in bits:
            self.collect_pblocks(bit, layer)

    def collect_pblocks(self, bit, layer):
        dic = self.pblock_dic.setdefault(layer.nov, {})
        kns = self.parent.bitdic[bit]
        for kn in kns:
            vk = self.parent.clauses[kn]
            cvs, ncvs = layer.bgrid.bv2cvs(bit, vk.dic[bit])
            # vk.dic[bit] != layercv.sat[bit]
            for cv in ncvs:
                dic.setdefault(cv,{})[kn] = '-'
            # vk.dic[bit] == layercv.sat[bit]
            obit = vk.other_bit(bit)
            okns = self.parent.bitdic[obit].copy()
            if len(okns) == 0:
                continue
            newsat = {obit: int(not vk.dic[obit])}
            while len(okns) > 0:
                okn = okns.pop()
                for cv in cvs: # vk.dic -> new-sat: {<other-bit-of-vk>:<not v>}
                    dic.setdefault(cv, {})[okn] = newsat
                x = 1
            x = 9


    def update(self, block):
        for nv, xlst in block.block_dic.items():
            lst = self.block_dic.setdefault(nv, [])
            for cv in xlst:
                if cv not in lst:
                    lst.append(cv)
            if len(lst) == len(Center.snodes[nv].layer.bgrid.chvset):
                return False
            for e in block.block_set:
                self.block_set.add(e)
        return True

    def add_block(self, arg):
        if type(arg) == dict:  # arg: {nov: [cvs]}
            nov, cvs = arg.popitem()
            lst = self.block_dic.setdefault(nov, [])
            for cv in cvs:
                if cv not in lst:
                    lst.append(cv)
                    self.block_set.add((nov,cv))
            L = len(Center.snodes[nov].layer.bgrid.chvset)
            if len(self.block_dic[nov]) == L:
                return False
        elif type(arg) == tuple:
            if type(arg[0]) == int:  # arg: (48,2)
                if type(arg[1]) == int:
                    return self.add_block({arg[0]: [arg[1]]})
                else:  # arg[1] is list or set
                    return self.add_block({arg[0]: arg[1]})
            # arg: ((),())
            self.block_set.add(arg)
        return True
    
    def name_inblock(self, name):
        if name in self.block_set:
            return True
        ss = set(name)
        cx = self.block_set.intersection(ss)
        in_it = len(cx) > 0
        return in_it

    