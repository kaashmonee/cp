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
    n = inp()
    a = seq()

    pd = dict()
    for p in a:
        if p in pd:
            pd[p] += 1
        else:
            pd[p] = 1

    ainds = [(ind, a[ind]) for ind in range(n)]
    ainds = sorted(ainds, key=lambda tup: tup[1])
    for p in ainds:
        if pd[p[1]] == 1:
            print(p[0]+1)
            return

    print(-1)


def main():

    tests = inp()


    for _ in range(tests):
        solve()


if __name__ == "__main__":
    main()
