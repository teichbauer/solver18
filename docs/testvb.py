'''
发上等愿， 结中等缘， 享下等福
择高处立， 寻平处住， 向宽处行
----------
求其上者得其中
求其中者得其下
求其下者无所得
'''
import pdb

def set_bit(val, bit_index, new_bit_value):
    """Set the bit_index (0-based) bit of val to x (1 or 0)
    and return the new val.
    the input param val remains unmodified, for val is passed-in by-value !
    """
    mask = 1 << bit_index  # mask - integer with just the chosen bit set.
    val &= ~mask  # Clear the bit indicated by the mask (if x == 0)
    if new_bit_value:
        val |= mask  # If x was True, set the bit indicated by the mask.
    return val  # Return the result, we're done.


def vary_bits(val, bits, cvs=set([])):
    # set val[b] = 0 and 1 for each b in bits, 
    # collecting each val after each setting into cvs
    # pdb.set_trace()
    if len(bits) == 0:
        cvs.add(val)
    else:
        bit = bits.pop()
        for v in (0, 1):
            nval = set_bit(val, bit, v)
            if len(bits) == 0:
                cvs.add(nval)
            else:
                vary_bits(nval, bits[:], cvs)
    return cvs
    
if __name__ == '__main__':
    #  bits:  3210
    # ----------------
    val = 6 # 0110
    bits = [3,2,1,0]
    cvs = vary_bits(val, bits)
    print(f'cvs: {cvs} ')