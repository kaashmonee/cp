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
def solve():
    px, py = mul()
    ords = strng()

    works = "YES"

    if px > 0:
        if ords.count("R") < px:
            print("NO")
            return
        
    if px < 0:
        if ords.count("L") < abs(px):
            print("NO")
            return

    if py < 0:
        if ords.count("D") < abs(py):
            print("NO")
            return

    if py > 0:
        if ords.count("U") < py:
            print("NO")
            return

    print("YES")
    return

def main():

    tests = inp()

    for _ in range(tests):
        solve()


if __name__ == "__main__":
    main()
