""" 
b0 b1   XOR( b0,b1)
--------------------
0  0    0
0  1    1
1  0    1
1  1    0

its like xor eax,eax ( to make it zero)


e.g Toogle 0th bit in 6

6         :   110
(1<<0)    :   001 ( same as set 0th bit to 1)
              --- ^
              111

e.g toogle 2nd bit in 6

6: 110
:  100 ( 1<<2 )
   ---- ^
   010



"""

def toggle_bit(x: int, n :int):
        return x ^ (1<<n)
#print (toggle_bit(6,0))
y = toggle_bit(6,0)
print(y)
y= toggle_bit(y,0)
print(y)