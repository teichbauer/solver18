from center import Center

class BlockChecker:
    def __init__(self, Layer):
        self.Layer = Layer
        self.checkdic = {}
        self.block_dic = {}
        self.block_refs = []  # ele: ((lower-Layer-cvs), <kn>, <sat-dic>)

    def make_cvsats(self):
        for vbit, d in self.checkdic.items():
            for bv, lst in d.items():
                for dd in lst:
                    if len(dd) > 2: # length: 3
                        # ke: (kn, C0011), e1: (60:{1,2,3}), e2: (21,{3,4})
                        ke, e1, e2 = list(dd.items())
                        entry = (e2[1], ke[1], {vbit: int(not bv)})
                        self.block_refs.append(entry)
                        for cv in e1[1]:
                            cvd = self.Layer.cvsats.setdefault(cv,{})
                            nvlst = cvd.setdefault(e2[0],[])
                            nvlst.append(entry)
                x = 0
            x = 8
        x = 9

    def show_cvsats(self, cvsats):
        msg = f"Layer-{self.Layer.nov}:\n"
        for cv in sorted(cvsats):
            novdic = cvsats[cv]
            msg += f"  {cv}: " + "{\n"
            for nv, lst in novdic.items():
                msg += f"    {nv}: [\n"
                msg += "          "
                for e in lst:
                    msg += f"{e},\t"
                msg += "\n        ],\n"
            msg += "      }\n"
        return msg

    def build_checkdic(self):
        for lower_nov, entry in self.Layer.blbmgr.cbdic.items():
            for kn, tp in entry.items():
                if tp[2] == None:
                    star_lst = self.block_dic.setdefault('*',[])
                    dic = {
                        self.Layer.nov: tuple(tp[1]), 
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
                            Layer_cvs = d.pop(self.Layer.nov)
                            cmm_cvs = Layer_cvs.intersection(tp[1])

                            # add to checkdic
                            checks = self.checkdic[bb].setdefault(vv, [])
                            dic = {
                                'kn': kn,
                                self.Layer.nov:tp[1],
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
                                        self.Layer.nov: tuple(cmm_cvs), 
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
                                    st.add((self.Layer.nov,tuple(cmm_cvs)))
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
                            self.Layer.nov: tp[1], 
                            lower_nov: tp[0]})
                        x = 1
    # def build_checkdic(self):


    