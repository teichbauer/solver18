from basics import verify_sat, test_clauses
from clause import Clause
from satx8 import SATS

class Center:
    maxnov = 0
    minnov = 0
    headbits = {}  # {<nov>:(3 bits)}
    bits = set([])
    sats = []
    snodes = {}
    blocker_dic = {}  # {<bit>:{}}
    cblocker_dic = {}  # {<bit>:{}}
    sumbdic = {}
    vk2bdic = {}  # <bit>:[<tail1>,<tail2>,...], <bit>:[],..}
    orig_vkm = None
    tails = {}

    # 8 sats:
    @classmethod
    def test_clauses(cls, clause_dic, sat_index):
        sat = SATS[sat_index]
        return test_clauses(clause_dic, sat)


    @classmethod
    def add_blocks(cls, nov, bchecker):
        for bit, set_lst in bchecker.block_dic.items():
            dic = cls.blocker_dic.setdefault(bit, {})
            lst = dic.setdefault(nov, [])
            for bsets in set_lst:
                dd = {}
                if type(bsets) == type({}):
                    dd.update(bsets)
                else:
                    for tp in bsets:
                        dd[tp[0]] = tp[1]
                lst.append(dd)
        for bit, bdic in bchecker.checkdic.items():
            dd = cls.cblocker_dic.setdefault(bit,{})
            for v, diclst in bdic.items():
                ddd = dd.setdefault(v,{})
                lst = ddd.setdefault(nov, [])
                for e in diclst:
                    d = {}
                    for k, val in e.items():
                        if k == "kn": # <kname>
                            d[k] = val
                        else:
                            d[k] = tuple(val)  # {1,2,3} -> (1,2,3)
                    lst.append(d)
            x = 9
        x = 0


    @classmethod
    def set_maxnov(cls, nov):
        cls.maxnov = nov
        cls.bits = set(range(nov))

    @classmethod
    def set_blinks(cls):
        nov = cls.maxnov
        x = 1
        # sn = cls.snodes[nov]

    @classmethod
    def get_tailchain(cls):
        chain = {}
        for nov, sn in cls.snodes.items():
            chain[nov] = sn.tail
        return chain

    @classmethod
    def bit_overlaps(cls, nov):
        print(f"Showing overlappings for {nov}")
        print("="*80)
        bdic0 = cls.sumbdic[nov]
        bdic = bdic0
        gcount = {}
        for b in bdic0:
            bcount = gcount.setdefault(f"nov-{nov}.{b}", {})
            bcount[nov] = (len(bdic0[b][0]), len(bdic0[b][1]))
            print("-"*20 + f" {nov}:{b} - {bdic0[b][0]},{bdic0[b][1]}")
            nv = nov - 3
            while True:
                bdic = cls.sumbdic[nv]
                cnt = gcount.setdefault(nv, {})
                print(f"{nv}:")
                for bit in bdic:
                    if bit == b:
                        c0 = len(bdic[b][0])
                        c1 = len(bdic[b][1])
                        m = f"  -> {nv}:{bit} - [{bdic[bit][0]},{bdic[bit][1]}]"
                        cnt[bit] = (c0, c1)
                        print(m)
                        print('---')
                print(f"-"*80)
                nv -= 3
                if nv == cls.last_nov:
                    break
        print(str(gcount))

    @classmethod
    def show_sumvk12m(cls, nov):
        dic = cls.sumvk12m[nov]
        ks = sorted(dic.keys())
        print(f"{nov} has {len(ks)} vks:")
        for k in ks:
            m = f"{k}:{str(dic[k][0].dic)}, {str(dic[k][1])}"
            print(m)
