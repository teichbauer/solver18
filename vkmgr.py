from basics import print_json


class VKManager:
    def __init__(self, vkdic, initial=False):
        self.vkdic = vkdic
        if initial:
            self.make_bdic()

    def clone(self):
        vkdic = {kn: vk.clone() for kn, vk in self.vkdic.items()}
        vkm = VKManager(vkdic)
        vkm.bdic = {b: s.copy() for b, s in self.bdic.items()}
        return vkm

    def pop_vk(self, kn):
        vk = self.vkdic.pop(kn)
        for bit in vk.bits:
            if kn in self.bdic[bit]:
                self.bdic[bit].remove(kn)
                if len(self.bdic[bit]) == 0:
                    self.bdic.pop(bit)
            else:
                raise Exception(f"pop {kn} failed")
        return vk

    def drop_bits(self, bits, kns, vks):
        for bit in bits:
            self.bdic.pop(bit)
        for vk in vks:
            self.vkdic.pop(vk.kname)
        for kn in kns:
            if kn in self.vkdic:
                vk = self.vkdic.pop(kn)
                # vk.clone(bits) will return a clone with dropped bits
                # the original vk will not be modified
                self.vkdic[kn] = vk.clone(bits)
            else:
                x = 1

    def printjson(self, filename):
        print_json(self.nov, self.vkdic, filename)

    def make_bdic(self):
        self.bdic = {}
        for kn, vk in self.vkdic.items():
            for b in vk.dic:
                if b not in self.bdic:  # hope this is faster than
                    self.bdic[b] = set([])  # bdic.setdefault(b,set([]))
                self.bdic[b].add(kn)

    def make_choice(self):
        "return: {'ancs': (tkn1, tkn2,),'bits': bits[,,],'touched':[,,..,]}"
        best_choice = None
        max_tsleng = -1
        max_tcleng = -1
        best_bits = None
        kns = set(self.vkdic.keys())  # candidates-set of kn for besy-key
        while len(kns) > 0:
            kn = kns.pop()
            vk = self.vkdic[kn]
            # sh_sets: {<bit>:<set of kns sharing this bit>,..} for each vk-bit
            sh_sets = {}  # dict keyed by bit, value is a set of kns on the bit
            bits = vk.bits
            for b in bits:
                sh_sets[b] = self.bdic[b].copy()
            # dict.popitem() pops a tuple: (<key>,<value>) from dict
            tsvk = sh_sets.popitem()[1]  # [0] is the bit/key, [1] is the set
            tcvk = tsvk.copy()
            for s in sh_sets.values():
                tsvk = tsvk.intersection(s)
                tcvk = tcvk.union(s)

            chc = (tsvk, tcvk - tsvk)
            kns -= tsvk  # take kns in tsvk out of candidates-set
            ltsvk = len(tsvk)
            if ltsvk < max_tsleng:
                continue
            ltcvk = len(tcvk)
            if not best_choice:
                best_choice = chc
                max_tsleng = ltsvk
                max_tcleng = ltcvk
                best_bits = bits
            else:
                if best_choice[0] == tsvk:
                    continue
                # see if to replace the best_choice?
                replace = False
                if max_tsleng < ltsvk:
                    replace = True
                elif max_tsleng == ltsvk:
                    if max_tcleng < ltcvk:
                        replace = True
                    elif max_tcleng == ltcvk:
                        if bits > best_bits:
                            replace = True
                if replace:
                    best_choice = chc
                    max_tsleng = ltsvk
                    max_tcleng = ltcvk
                    best_bits = bits
        result = {
            "avks": [self.pop_vk(kn) for kn in best_choice[0]],
            "touched": best_choice[1],
            "bits": best_bits,
        }
        return result

    # end of def make_choice(self):
