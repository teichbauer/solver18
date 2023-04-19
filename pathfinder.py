from center import Center
from cluster import Cluster
from basics import sortdic, print_bitdic, print_clause_dic, my_setdiff

class PathFinder:
    def __init__(self):
        self.cluster_groups = Cluster.groups
        for nv in sorted(Center.layers):
            layer = Center.layers[nv]
            layer.bchecker.make_cvsats()
            # msg = layer.bchecker.show_cvsats(layer.cvsats)
        self.grow_pairs(60)
        clupool = [pa[1] for pa in Cluster.groups[60]]
        self.search(clupool, Center.layers[54])        

    def grow_pairs(self, hnv):  # paring layers: high-nov to lower-nov
        while hnv >= Center.minnov:
            if hnv == Center.minnov:
                break
            highlayer, lowlayer = Center.layers[hnv], Center.layers[hnv-3]
            for cv, cvn2 in highlayer.cvn2s.items():
                cluster = Cluster((hnv, cv), cvn2)
                d = highlayer.cvsats[cv].get('*', None)
                if d and not cluster.add_sat(d[0]):
                    continue
                filters = []
                if lowlayer.nov in highlayer.cvsats[cv]:
                    filters = highlayer.cvsats[cv][lowlayer.nov]
                cluster.grow_with_filter(lowlayer, filters)
                x = 0
            break   # just build 60-57 pairs: 7x7=49
            hnv -= 6
        x = 9

    def search(self, pool, lyr):
        while len(pool):
            cluster = pool.pop(0)
            # if cluster.name == [(60, 1), (57, 4), (54, 2), (51, 1), (48, 5), (45, 4), (42, 7), (39, 0), (36, 2), (33, 0), (30, 7), (27, 5), (24, 7)]:
            if cluster.name == [(60, 1), (57, 4)]:
                x = 0
            nv = cluster.nxt_nv
            if nv == -1:
                self.collect_sats(cluster)
                continue
            # lyr = Center.layers[nv]
            cvdic = cluster.cvsats[nv]
            print("----------------")
            print(f"cluster:{cluster.name}-[{cvdic['cvs']}]")
            npool = []
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
        sat = {}
        for t in cluster.name:
            nov, cv = t
            sat.update(Center.layers[nov].bgrid.grid_sat(cv))
        for kn, vk3 in Center.orig_vkm.vkdic.items():
            bits = set(sat).intersection(vk3.bits)
            ssat = { b:sat[b] for b in bits }
            print(f"{kn}: {vk3.dic} <=> {ssat}")
            x = 0
        x = 9
