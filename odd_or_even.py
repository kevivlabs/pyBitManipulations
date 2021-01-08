def is_even_odd(x: int):
    if x & 1 == 0:
        return "Even"
    return "Odd"

"""
explanation
    421
1   001
2   010
3   011
4   100
5   101
6   110
7   111

eg. 
3   011
    001 
   ------ &
    001

4   100
    001 
   ------ &
    000   
Observation: 
already most odd numbers 
 Odd binary numbers always end in '1' and even binary numbers always end in '0'. This is evident when you compare the numbers in the table.
  In fact, to double a binary number, all you have to do is add a zero bit on the right side.
  Decimal numbers take up less space than binary numbers
  Binary numbers take up more space than decimal numbers
"""

print (is_even_odd(33))
print (is_even_odd(22))

