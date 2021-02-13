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

    sols = [0] * n

    for i in range(n-1, -1, -1):
        nxt_ind = i + a[i]
        next_score = 0

        if nxt_ind < n:
            sols[i] = a[i] + sols[i + a[i]]
        else:
            sols[i] = a[i]

    print(max(sols))


def main():

    tests = inp()

    for _ in range(tests):
        solve()


if __name__ == "__main__":
    main()
