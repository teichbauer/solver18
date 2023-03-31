from center import Center

class BlockChecker:
    def __init__(self, tail):
        self.tail = tail
        self.checkdic = {}
        self.block_dic = {}

    def build_checkdic(self):
        for lower_nov, entry in self.tail.blbmgr.cbdic.items():
            for kn, tp in entry.items():
                if tp[2] == None:
                    star_lst = self.block_dic.setdefault('*',[])
                    dic = {
                        self.tail.nov: tuple(tp[1]), 
                        lower_nov: tuple(tp[0])
                    }
                    star_lst.append(dic)
                else:
                    bb, vv = tp[2]
                    rv = (vv + 1) % 2
                    if bb in self.checkdic and rv in self.checkdic[bb]:
                        rds = self.checkdic[bb][rv]
                        for rd in rds:
                            d = rd.copy()
                            d.pop('kn')
                            tail_cvs = d.pop(self.tail.nov)
                            cmm_cvs = tail_cvs.intersection(tp[1])

                            # add to checkdic
                            checks = self.checkdic[bb].setdefault(vv, [])
                            dic = {
                                'kn': kn,
                                self.tail.nov:tp[1],
                                lower_nov:tp[0]}
                            if not dic in checks:
                                checks.append(dic)
                            
                            # add to block_dic, if cmm_cvs not empty
                            if len(cmm_cvs) > 0:
                                nv, the_cvs = d.popitem()
                                if nv == lower_nov:
                                    add_it = True
                                    cvs = the_cvs.intersection(tp[0])
                                    dd = {
                                        self.tail.nov: tuple(cmm_cvs), 
                                        nv: tuple(cvs)
                                    }
                                    for dx in self.block_dic['*']:
                                        if dx == dd:
                                            add_it = False
                                    if add_it:
                                        lst = self.block_dic.setdefault('*',[])
                                        lst.append(dd)
                                else:
                                    lst = self.block_dic.setdefault(bb, [])
                                    st = set([])
                                    st.add((self.tail.nov,tuple(cmm_cvs)))
                                    st.add((nv, tuple(the_cvs)))
                                    st.add((lower_nov, tuple(tp[0])))
                                    if st not in lst:
                                        lst.append(st)
                            x = 1
                    else:
                        cdic = self.checkdic.setdefault(bb, {})
                        dics = cdic.setdefault(vv, [])
                        dics.append({
                            'kn': kn, 
                            self.tail.nov: tp[1], 
                            lower_nov: tp[0]})
                        x = 1


    