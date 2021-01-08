def int2bin(x:int):
    for i in range(31,0,-1):
        if(x&(1<<i)):
            print("1",end='')
        print("0",end='')
    print(" \n")

int2bin(24)
