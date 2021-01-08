"""
e.g  set the 0 th bit for 6 

6:   110
 :   001 
    -----  | (or)
     111
 Here from the binary representation of 6 we just changed the last 0 bit 

 Which is the same as 

 6  :    110
 1<<0:   001 
        -----  | (or)
         111

so if we say set the 2nd bit for 6 , it would be
 

6    :  011
 1<<2:  100 
        -----  | (or)
        111
 """

def set_nth_bit(x: int, n: int):
   # return x | 1 << n
    return bin(x| 1<<n)[2:]
    #print it in binary with removing the inital 0b 

print(set_nth_bit(6,0))

print(set_nth_bit(6,2))
