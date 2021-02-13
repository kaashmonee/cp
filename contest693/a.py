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
#solved

def main():

    tests = inp()


    def solve():
        w, h, n = mul()
        # just have to check log base 2 of w and h and then sum them up
        # to see if they're less greater than or equal to n
        paps = 1
        while w > 0 and w % 2 == 0:
            w //= 2
            paps *= 2
        
        while h > 0 and h % 2 == 0:
            h //= 2
            paps *= 2

        if paps >= n:
            print("YES")
        else:
            print("NO")


    for _ in range(tests):
        solve()

if __name__ == "__main__":
    main()
