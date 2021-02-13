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
    thms = seq()
    mishka = seq()

    missed = []
    for thm, behavior in zip(thms, mishka):
        if behavior > 0:
            missed.append(0)
        else:
            missed.append(thm)

    # find the max
    # combined interval sol
    combined = []
    combined.append(missed[0])
    for i in range(1, len(missed)):
        cur = combined[-1] + missed[i]
        combined.append(cur)

    max_intvl_val = -math.inf
    max_intvl = (0, 0)


    for i in range(k-1, n):
        if i == k-1:
            tot = combined[i]
        else:
            tot = combined[i] - combined[i-k]

        if tot > max_intvl_val:
            max_intvl_val = tot
            max_intvl = (i-k+1, i)

    mishka = mishka[:max_intvl[0]] + ([1] * k) + mishka[max_intvl[1]+1:]
    tot_theorems = 0
    for ind, thm in enumerate(thms):
        tot_theorems += thm * mishka[ind]

    print(tot_theorems)



def main():

    # tests = inp()
    tests = 1

    for _ in range(tests):
        solve()


if __name__ == "__main__":
    main()
