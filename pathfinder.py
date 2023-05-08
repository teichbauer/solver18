from center import Center
from cluster import Cluster
from basics import sortdic, sat_diff, bits_combo_dics

class PathFinder:
    def __init__(self):
        for nv in sorted(Center.layers):
            layer = Center.layers[nv]
            layer.bchecker.make_cvsats()
            # msg = layer.bchecker.show_cvsats(layer.cvsats)
        clupool = self.grow_pair_pool(Center.maxnov)
        self.sat_dic = {}
        self.sats = []
        self.search(clupool, Center.layers[54])        

    def grow_pair_pool(self, hnv):  # paring layers: high-nov to lower-nov
        pair_pool = []
        highlayer, lowlayer = Center.layers[hnv], Center.layers[hnv-3]
        for cv, cvn2 in highlayer.cvn2s.items():
            cluster = Cluster((hnv, cv), cvn2)
            d = highlayer.cvsats[cv].get('*', None)
            if d and not cluster.add_sat(d[0]):
                continue
            filters = []
            if lowlayer.nov in highlayer.cvsats[cv]:
                filters = highlayer.cvsats[cv][lowlayer.nov]
            cluster.grow_pairs(lowlayer, filters, pair_pool)
            x = 0
        return pair_pool

    def search(self, pool, lyr):
        while len(pool):
            cluster = pool.pop(0)
            nv = cluster.nxt_nv
            if nv == -1:
                self.collect_sats(cluster)
                continue
            # lyr = Center.layers[nv]
            cvdic = cluster.cvsats[nv]
            print("----------------")
            print(f"cluster:{cluster.name}-[{cvdic['cvs']}]")
            npool = []   # new pool for next layer
            for cv in cvdic['cvs']:
                filters = cvdic.get(cv, [])
                # print(f"lyr({nv}-{cv}):")
                clu = cluster.grow_layercv(lyr, cv, filters)
                if clu:
                    lyrcv_sat = lyr.bgrid.grid_sat(cv)
                    lyrcv_sat_res = clu.add_sat(lyrcv_sat)
                    if lyrcv_sat_res:
                        npool.append(clu)
                    else:
                        print(f"fail: sat-conflict")
                else:
                    print(f"{cv}-th fail.")
            if nv > Center.minnov:
                nxt_lyr = Center.layers[nv - 3]
            else:
                nxt_lyr = None
            if not self.search(npool, nxt_lyr):
                continue
        return None

    def collect_sats(self,cluster):
        name_tpl = tuple(cluster.name)
        vk2s = []
        for kn, vk3 in Center.orig_vkm.vkdic.items():
            bits = set(cluster.sat).intersection(vk3.bits)
            ssat = { b:cluster.sat[b] for b in bits }
            if len(ssat) == 2:
                vk2s.append(vk3)
            # m = f"{kn}: {vk3.dic}\t"
            # L = 'O'
            # if vk3.hit(ssat):
            #     L = 'H'
            # print(f"{m} <=> {ssat}  : {L}")
            # x = 0
        rest_bits = Center.bits.difference(cluster.sat)
        self.make_sats(name_tpl, cluster.sat.copy(), vk2s, rest_bits)
        return 

    def make_sats(self, name_tpl, sat, vk2s, bits):
        free_dics = bits_combo_dics(bits.copy())
        print(f"Collecting for {name_tpl}")
        print(self.sat_name(name_tpl))
        x = 0
        for sdic in free_dics:
            for vk in vk2s:
                inbit = bits.intersection(vk.bits).pop()
                vk2 = vk.clone([inbit])
                if vk2.hit(sdic) and vk.dic[inbit] == sdic[inbit]:
                    break
            ss = sat.copy()
            ss.update(sdic)
            lst = self.sat_dic.setdefault(name_tpl,[])
            lst.append(ss)
            self.sats.append(ss)
        x = 9

    def sat_name(self, names):
        if (45,5) in names:
            if (27,1) in names:
                return "sat: 0, 1"
            elif (27,5) in names:
                return "sat: 4, 5"
        elif (45,7) in names:
            if (27,1) in names:
                return "sat: 2, 3"
            elif (27,5) in names:
                return "sat: 6, 7"

