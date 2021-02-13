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
    n, k = mul()
    mtns = seq()
    last = -1

    i = 0

    diffs = [math.inf] + [mtns[i+1] - mtns[i] for i in range(len(mtns)-1)]

    for boulder in range(k):
        # you could optimize this by remembering "i"
        if i > 0 and mtns[i-1] < mtns[i]:
            i -= 1
            # print("case 1:", i)

        
        while i < len(mtns)-1 and mtns[i] >= mtns[i+1]:
            # print("i:", i)
            # print("mtns:", mtns)
            i += 1

        if i == len(mtns)-1:
            # exit out of the while loop and do nothing
            last = -1
            continue

        # only do this if the boulder didn't roll off the cliff
        # i < len(mtns)-1
        mtns[i] += 1
        last = i

        if i == len(mtns)-1:


        # print("case 2:", i)

    if last == -1:
        print(last)
    else:
        print(last+1)


def main():

    tests = inp()

    for _ in range(tests):
        solve()


if __name__ == "__main__":
    main()
