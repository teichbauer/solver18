from basics import expand_bitcombo

class Clause:
    def __init__(self, name, dic, mark=None):
        self.kname = name
        self.bits = sorted(dic, reverse=True)
        self.dic = dic
        self.mark = mark

    def other_bit(self, b):
        ''' Only for vk with 2 bits: return the other bit '''
        if b in self.bits:
            bits = self.bits[:]
            bits.remove(b)
            return bits[0]
        return None

    def clone(self):  
        return Clause(self.kname, self.dic.copy(), self.mark)

    def evaluate_overlap(self, cl):
        ''' Only for vk2, and only for self.bits == cl.bits            
            1. self.dic == cl.dic - return 0: 
                cl is a duplicate of self
            2. if self.dic[b0] == cl.dic[b0] and  self.dic[b1] != cl.dic[b1]
                - return a sat{b0: self.dic[b0]}
               The reasoning:
                 (a + b)(a + ¬b)    = 
                 a(a+b) + ¬b(a+b)   = 
                 a + ab + a¬b + ¬bb =
                 a(1+b+¬b)          = 
                 a
            3. self.dic[b0] != cl.dic[b0] and self.dic[b1] != cl/dic[b1]
                - return 1:
                cl and self are not entangled
        '''
        assert(self.bits == cl.bits),f"{self.kname} and {cl.kname} not overlap."
        b0, b1 = self.bits
        if self.dic[b0] == cl.dic[b0]:
            if self.dic[b1] == cl.dic[b1]:
                return 0
            #  self.dic[b0] == cl.dic[b0] and self.dic[b1] != cl.dic[b1]
            return {b0: self.dic[b0]}
        elif self.dic[b1] == cl.dic[b1]:
            return {b1: self.dic[b1]}
        return 1
        
    
    def sats(self):
        # self.bits==[2,5] => [{2:0, 5:0}, {2:0, 5:1}, {2:1, 5:0}, {2:1, 5:1}]
        dics = expand_bitcombo(self.bits)
        sats = []                 # dics that are not covered by self.dic
        for dic in dics:
            if dic != self.dic:   # collect all that is not self.dic
                sats.append(dic)  # into sats
        return sats


    def verify(self, sats):  # sats must not have a single 2 among the values
        if set(self.bits).issubset(set(sats)):
            b0, b1 = self.bits
            if self.dic[b0] == sats[b0] and self.dic[b1] == sats[b1]:
                # print(f"{self.kname} = hit(False)")
                return False
            return True
        raise Exception(f"{self.kname} not in sat")

