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
    n, q, k = mul()
    a = seq()

    mem = dict()

    # a.insert(0, -1)
    while q > 0:
        li, ri = mul()
        tot = 0
        li -= 1
        ri -= 1
        if li == ri:
            print(k-1)
            q -= 1
            continue
        # print("mem:", mem)

        for ind in range(li, ri+1):

            left = ind-1
            right = ind+1

            if left < li:
                if right > ri:
                    tot += k-1
                    continue
                
                diff = a[right]-2

            elif right > ri:
                diff = k - a[left] - 1
            
            else:
                diff = a[right] - a[left] - 2
                mem[ind] = diff

            # mem[(left, right)] = diff
            # print("diff:", diff)
            print("mem:", mem)
            tot += diff

        q -= 1
        print(tot)


def main():

    # tests = inp()
    tests = 1

    for _ in range(tests):
        solve()


if __name__ == "__main__":
    main()
