from center import Center

class Branch:
    def __init__(self, parent, name='R', sat=None):  # R:Root
        self.parent = parent
        self.name = name
        self.sumbdic = {}
        self.novs = []  # list of descending novs
        self.chain = {}
        if sat == None:
            self.sat = {}
        else:
            self.sat = sat

    def add_tail(self, nov, tail):
        self.novs.append(nov)
        self.chain[nov] = tail
        # {bit: tail} - on the bit tail has only ONE kn
        for b, kns in tail.bdic.items():
            vklst = self.sumbdic.setdefault(b,[])
            for kn in kns:
                vklst.append(tail.vk2dic[kn])

    def get_bestbit(self):
        max_cnt = 0
        bit = -1
        for b, vklst in self.sumbdic.items():
            cnt = len(vklst)
            if  cnt > max_cnt:
                bit = b
                max_cnt = cnt
        return bit

    def split(self):
        sbit = self.get_bestbit() 
        ssat0_tpl = (sbit, 0)  # { sbit: 0 }
        ssat1_tpl = (sbit, 1)  # { sbit: 1 }

        b1 = Branch(self, f"{self.name}-{ssat1_tpl}", self.sat)
        b1.sat.update(dict((ssat1_tpl,)))
        chain1 = self.clone_chain(ssat1_tpl)
        for nv, tail in chain1.items():
            b1.add_tail(nv, tail)
        if not b1.done():
            b1.split()

        b0 = Branch(self, f"{self.name}-{ssat0_tpl}", self.sat)
        # t=(21,0), dict((t,)) -> {21:0}
        b0.sat.update(dict((ssat0_tpl,)))
        x = 0

        return b0, b1
    
    def done(self):
        return False

    def clone_chain(self, ssat_tpl):
        nchain = {}
        for nov, tail in self.chain.items():
            if ssat_tpl[0] not in tail.bdic:
                print(f"{nov}/{ssat_tpl} not hit")
            nchain[nov] = tail.clone(ssat_tpl)
            inf = nchain[nov].metrics()
            print(inf)
        return nchain
        
    def show_chain(self):
        print(self.name)
        for nv in self.novs:
            print(f"{self.name}")
            msg = self.chain[nv].metrics()
            print(msg)
