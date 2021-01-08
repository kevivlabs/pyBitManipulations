"""
~1 -> 0
~0 -> 1
Observation

1<<0    : 0000 0001
~(1<<0) : 1111 1110
1<<1    : 0000 0010
~(1<<1) : 1111 1101

e.g Unset the 1st bit in 6 

6:  110
    101 
    ---- &
    100
 Hence 1st bit is unset

 The 101 is obtained by bit shifting  1st bit which is 010 and then using the NOT operation 101

 Hence anything AND with 0 will unset



"""

def unset_nth_bit(x: int, n: int):
    return x & ~(1 << n)
print (unset_nth_bit(6,1))
print (unset_nth_bit(6,2))