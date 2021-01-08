"""
explanation
    421
1   001
2   010
3   011
or can also be written as 

1   1<<0 : 0000 0001
2   1<<1 : 0000 0010
3   1<<2 : 0000 0100


eg. 
3   011
    001 
   ------ &
    001
so now to see if a nth bit is set , we AND the bit with 1 if the result is zero its not set or else its set

e.g Is 2nd bit set 
6   110
    100  ( 2nd bit is set to 1 and others are zero then we AND it) 
    ---- &
    100 
Hence 2nd bit is set 

e.g is 0 bit set ?
6   110
    001  ( 0th bit is set to 1 and others are set to zer and Then AND it)
   ----- &
    000
Hence 0th bit is not set 

This can also be said as (from the bit representation above) if you want to check the nth bit then bit shift n times with 1
eg. 2nd bit set ?
6:      110
1<<2:   100 ( bit shift 2 times) 
        ---
        100
Observation:
    Given a number , we shift over by n bits on the number and then AND it , we obtain  0 then nth bit is not set or else it is set
    In 6  is 2nd bit set ?
     6 , we shift over 2 times then AND it, we get that the bit is set (eg above)
"""

def isnthbit(x: int,n : int):
    if x & ( 1 << n):
        return "True -Is set"
    return "False - not set"

print (isnthbit(73,3))
