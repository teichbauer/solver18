from center import Center
from cluster import Cluster
from basics import sortdic, print_bitdic, my_setdiff, bits_combo_dics

class PathFinder:
    def __init__(self):
        for nv in sorted(Center.layers):
            layer = Center.layers[nv]
            layer.bchecker.make_cvsats()
            # msg = layer.bchecker.show_cvsats(layer.cvsats)
        clupool = self.grow_pair_pool(60)
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
            # if cluster.name == 
            # [(60, 1), (57, 4), (54, 2), (51, 1), (48, 5), 
            #  (45, 4), (42, 7), (39, 0), (36, 2), (33, 0), 
            #  (30, 7), (27, 5), (24, 7), (21, 6)]:
            # if cluster.name == [(60, 1), (57, 4), (54, 2), (51, 1)]:
            vk3s = [Center.orig_vkm.vkdic['C0068'],
                    Center.orig_vkm.vkdic['C0139'],
                    Center.orig_vkm.vkdic['C0181'],
                    Center.orig_vkm.vkdic['C0195']]
            # if cluster.name == [(60, 1), (57, 4), (54, 2), (51, 1), (48, 5), (45, 4), (42, 7), (39, 0)]:
            # hit -> True
            # if cluster.name == [(60, 1), (57, 4), (54, 2), (51, 1), (48, 5), (45, 4), (42, 7)]:
            # hit -> True C0139 {9: 1, 38: 1, 39: 0}
            if cluster.name == [(60, 1), (57, 4), (54, 2), (51, 1), (48, 5), (45, 4)]:
                hit = False
                for vk3 in vk3s:
                    hit = vk3.hit(cluster.sat)
                    if hit:
                        x = 99
            if cluster.name == [(60, 1), (57, 4), (54, 2), (51, 1), (48, 5)]:
                x = 0
            if cluster.name == [(60, 1), (57, 4), (54, 2), (51, 1)]:
                x = 0
            if cluster.name == [(60, 1), (57, 4), (54, 2)]:
                x = 0

            #  cluster.sat: {...,9:1, 39:0, ...}
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
                print(f"lyr({nv}-{cv}):")
                clu = cluster.grow_layercv(lyr, cv, filters)
                if clu:
                    lyrcv_sat = lyr.bgrid.grid_sat(cv)
                    lyrcv_sat_res = clu.add_sat(lyrcv_sat)
                if clu and lyrcv_sat_res:
                    if clu.nxt_nv == -1:
                        print(f"bottom: {clu.name}")
                    else:
                        print(f"next-cvs:{clu.cvsats[nv - 3]['cvs']}")
                    npool.append(clu)
                else:
                    print(f"lyr({nv}-{cv}) failed")
            if nv > Center.minnov:
                nxt_lyr = Center.layers[nv - 3]
            else:
                nxt_lyr = None
            if not self.search(npool, nxt_lyr):
                continue
        return None

    def collect_sats(self,cluster):
        vk2s = []
        for kn, vk3 in Center.orig_vkm.vkdic.items():
            bits = set(cluster.sat).intersection(vk3.bits)
            ssat = { b:cluster.sat[b] for b in bits }
            if len(ssat) == 2:
                vk2s.append(vk3)
            m = f"{kn}: {vk3.dic}\t"
            L = 'O'
            if vk3.hit(ssat):
                L = 'H'
            print(f"{m} <=> {ssat}  : {L}")
            x = 0
        rest_bits = Center.bits.difference(cluster.sat)
        self.make_sats(cluster.sat.copy(), vk2s, rest_bits)
        return 

    def make_sats(self, sat, vk2s, bits):
        free_dics = bits_combo_dics(bits)
        for sdic in free_dics:
            for vk in vk2s:
                if not vk.hit(sdic):
                    break
            ss = sat.copy()
            ss.update(sdic)
            self.sats.append(ss)
        x = 9



