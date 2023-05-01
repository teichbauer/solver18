from pathfinder import PathFinder
from bitgrid import BitGrid
from center import Center
from layer import Layer
from basics import display_vkdic, ordered_dic_string, verify_sat

class SatNode:

    def __init__(self, parent, sh, vkm):
        choice = vkm.make_choice()  # avks be pooped out from vkm.vkdic
        self.parent = parent
        self.repo = Center
        if parent == None:
            self.nov = Center.maxnov
            Center.root_snode = self
        else:
            self.nov = parent.nov - 3
        self.sh = sh
        self.vkm = vkm  # all 3vks in here
        Center.snodes[self.nov] = self
        self.next = None
        self.touched = choice['touched']
        self.next_sh = self.sh.reduce(choice["bits"])
        self.bgrid = BitGrid(choice, self.nov)
        self.split_vkm()

    def split_vkm(self):
        
        Center.headbits[self.nov] =  self.bgrid.bitset
        self.chdic = {}

        bdic = Center.sumbdic.setdefault(self.nov, {})
        vk2dic = {}

        block_bv_dic = {}
        print(f"------- {self.nov} -----------")
        # show_vkdic = {}
        for kn in self.touched:
            vk = self.vkm.pop_vk(kn)        # pop out 3vk
            vk12 = self.bgrid.reduce_vk(vk) # make it vk12
            # show_vkdic[vk12.kname] = vk12
            if vk12.nob == 1:
                b, v = vk12.hbit_value()
                cvs = tuple(vk12.cvs)
                print(f"{kn}-{vk12.dic}{cvs}  becomes sat: {b}:{v}{cvs}")
                block_bv_dic.setdefault(b,{})[v] = vk12.cvs
                block_bv_dic[b]['kn'] = kn
            else:  # vk12.nob == 2
                for b, v in vk12.dic.items():
                    bdic.setdefault(b, set([])).add(kn)
                vk2dic[kn] = vk12
                Center.add_vk2(vk12)
        # display_vkdic(show_vkdic)
        self.layer = Layer(self.bgrid, vk2dic, bdic, block_bv_dic)
        Center.tailbits = Center.tailbits - self.layer.bgrid.bitset
        self.find_overlapped_vks()
        x = 0
    # ---- def split_vkm(self) --------

    def find_overlapped_vks(self):
        if self.nov == Center.maxnov: return
        nv = self.nov + 3
        while nv <= 60:
            t = Center.snodes[nv].layer
            obits = self.bgrid.bitset.intersection(t.bdic)
            obits_cnt = len(obits)
            if obits_cnt > 0:
                done_kns = []
                for ob in obits:
                    for kn in t.bdic[ob]:
                        vk = t.vk2dic[kn]
                        d = {}
                        for b in vk.bits:
                            if b in obits:
                                d[b] = vk.dic[b]
                        cvs = self.bgrid.bits_cvs(d)
                        if len(d) == 2:
                            t.blbmgr.add_cbd(
                                self.nov,
                                vk.kname,
                                (cvs, vk.cvs,  None)
                            )
                        else:   # len(d) == 1
                            vk1 = vk.clone(list(d))
                            blck = tuple(vk1.dic.items())[0]
                            t.blbmgr.add_cbd(
                                self.nov,
                                vk.kname,
                                (cvs, vk.cvs, blck)
                            )
            nv += 3
        x = 8

    def heads_schwanz(self):
        head = set([])
        schwanz = set(self.layer.vk2dic)
        for vd in self.layer.blbmgr.cbdic.values():
            for kn in vd:
                head.add(kn)
                if kn in schwanz:
                    schwanz.remove(kn)
        return head, schwanz

    def spawn(self):
        if len(self.vkm.vkdic) > 0:
            # as long as there exist vk3 in self.vkm.vkdic, go next (nov -= 3)
            self.next = SatNode(self,  # parent
                                self.next_sh.clone(),
                                self.vkm)
            return self.next.spawn()
        else:
            Center.minnov = self.nov
            nv = Center.maxnov
            while nv >= self.nov:
                hd, swz = Center.snodes[nv].heads_schwanz()
                print(f"{nv}-heads: {hd}")
                print(f"{nv}-schwz: {swz}")
                layer = Center.snodes[nv].layer
                layer.bchecker.build_checkdic()
                Center.add_blocks(nv, layer.bchecker)
                nv -= 3

            pfinder = PathFinder()
            return pfinder.sats
            

    def path_sat(self, pname):
        sat = {}
        secs = pname.split('-')
        for sec in secs:
            pair = sec.split('.')
            snode = Center.snodes[int(pair[0])]
            snv_sat = snode.bgrid.grid_sat(int(pair[1]))
            sat.update(snv_sat)
        return sat
