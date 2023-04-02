from center import Center
from cluster import Cluster
from basics import sortdic, print_bitdic, print_clause_dic, test_clauses

class PathFinder:
    def __init__(self):
        self.cluster_groups = Cluster.groups
        for nv in sorted(Center.tails):
            Center.tails[nv].bchecker.make_cvsats()
        self.grow_pairs(60)
        
        self.grow_cluster(60)
        hit_cnt = self.downwards()
        self.find_path()

    def grow_pairs(self, hnv):  # paring layers: high-nov to lower-nov
        while hnv >= Center.minnov:
            if hnv == Center.minnov:
                break
            highlayer, lowlayer = Center.tails[hnv], Center.tails[hnv-3]
            for cv, cvn2 in highlayer.cvn2s.items():
                cluster = Cluster((hnv, cv), cvn2)
                Cluster.clusters[hnv] = cluster
                cluster.grow(lowlayer)
            hnv -= 6
        x = 9

    def grow_cluster(self, tail_nv):
        while tail_nv > Center.minnov:
            tail = Center.tails[tail_nv]
            ntail = Center.tails[tail_nv - 3]
            for cv, cvn2 in tail.cvn2s.items():
                cluster = Cluster((tail.nov,cv), cvn2)
                Cluster.clusters[tail_nv] = cluster
                # grow cluster between (tail, ntail)
                cluster.grow(ntail)
            tail_nv -= 6
        x = 8

    def downwards(self):
        cnt = 0
        nov = Center.maxnov
        while nov in Cluster.groups:
            # nov: 60, 54, 48, 42, 36, 30, 24
            for name, cluster in self.cluster_groups[nov]:
                print(f"{name}-cluster.")  # cluster.name:((60,1),(57,2))
                nv = nov - 6
                body_satbits, body_sat = cluster.body_sat()
                while nv in self.cluster_groups:
                    for nam, cl in self.cluster_groups[nv]:
                        if cluster.block.name_inblock(nam):
                            continue
                        ibits = body_satbits.intersection(cl.sat)
                        if len(ibits) > 0:
                            idic = {b: body_sat[b] for b in ibits}
                            hit, nm = cl.test_sat(idic)
                            if hit:
                                if nm:
                                    bnv, cvs = nm
                                    for cv in cvs:
                                        cluster.block.add_block((bnv, cv))
                                    cnt += len(cvs)
                                    print(f"({bnv}, {cvs}) hit")
                                    continue
                                else:
                                    cluster.block.add_block(nam)
                                    cnt += 1
                                    print(f"{nam}-hit")
                    nv -= 6
            print("=================")
            nov -= 6 # nov/while loop, 60 ->54 ->48 ->42 ->36 ->30 ->24
        return cnt

    def find_path(self):
        lnv, lind = 60, 0
        nlnv = lnv - 6
        cluster = self.cluster_groups[lnv][lind][1]
        path = [ cluster ]
        if not self.pathdown(path, cluster, self.cluster_groups[nlnv]):
            lind += 1
        else:
            x = 9

    def pathdown(self, path, clustr, ngrp):
        # set pblock for the next 2 lower tails
        nv = clustr.nov - 6
        tails = []
        while nv >= Center.minnov and nv >= clustr.nov - 9:
            tails.append(Center.snodes[nv].tail)
            nv -= 3
        clustr.set_pblock(tails)
        grp = clustr.block_filter(ngrp)

        nv = clustr.nov - 6
        while nv >= Center.minnov:
            res = test_clauses(Center.tails[nv].vk2dic, clustr.sat)
            nv -= 3

        ind = 0
        found = False
        while not found:
            nclstr = grp[ind]
            for i in (0,1,2,3,4,5,6,7):
                res = Center.test_clauses(clustr.clauses, i)
                rea = Center.test_clauses(nclstr.clauses, i)

            nx = clustr.merge_cluster(nclstr)
            if not nx:
                ind += 1
                if ind > (len(grp) - 1):
                    return None
            else:
                cl, mv = nx
                path.append(cl)
                mgrp = Cluster.groups[mv]
                mx = self.pathdown(path, cl, mgrp)
                if not mx:
                    ind += 1
                else:
                    return True
        x = 0
        