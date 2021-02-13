import sys
# problem a
# template by:
# https://github.com/rajatg98

'''input

'''
import sys
import math
import bisect
from sys import stdin,stdout
from math import gcd,floor,sqrt,log
from collections import defaultdict as dd
from bisect import bisect_left as bl,bisect_right as br

sys.setrecursionlimit(100000000)

inp    =lambda: int(input())
strng  =lambda: input().strip()
jn     =lambda x,l: x.join(map(str,l))
strl   =lambda: list(input().strip())
mul    =lambda: map(int,input().strip().split())
mulf   =lambda: map(float,input().strip().split())
seq    =lambda: list(map(int,input().strip().split()))

ceil   =lambda x: int(x) if(x==int(x)) else int(x)+1
ceildiv=lambda x,d: x//d if(x%d==0) else x//d+1

flush  =lambda: stdout.flush()
stdstr =lambda: stdin.readline()
stdint =lambda: int(stdin.readline())
stdpr  =lambda x: stdout.write(str(x))

mod=1000000007

#main code

def main():

    tests = inp()

    def solve():
        q, d = mul()
        xs = seq()
        k = 10*d + 9

        mem = dict()
        # initialize mem
        mem[d] = True


        def ks(sack, pool, desired):
            if sack == desired:
                return True

            if pool <= 0:
                return False
            
            for y in range(pool):
                if y in mem:
                    return mem[y]

                sack += y
                pool -= y
                if ks(sack, pool, desired):
                    mem[desired] = True
                    return True
                
                sack -= y
                pool += y
                mem[sack+y] = False

        for x in xs:
            if x > k:
                print("YES")
            elif x <= k - 10:
                result = ks(0, x, x)
                print("table:", mem)
                print("YES" if result else "NO")
            else: 
                # 10d <= x <= 10d+9
                print("YES")

        
    for _ in range(tests):
        solve()


if __name__ == "__main__":
    main()
