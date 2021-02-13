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
    v1, v2 = mul()
    t, d = mul()
    time = t

    limits = [v2]
    while time > 1:
        limits.append(limits[-1] + d)
        time -= 1

    time = t
    dist = 0
    limits = limits[::-1]
    start = v1
    ind = 0
    # print("limits:", limits)
    while time > 0:
        # print("limit:", limits[ind])
        # print("start before:", start)
        if start < limits[ind]:
            if limits[ind] - start <= d:
                start = limits[ind]
            else:
                start += d
        else:
            start = limits[ind]

        # print("start after:", start)

        dist += start
        # print("dist:", dist)
        ind += 1
        time -= 1

    print(dist)




def main():

    # tests = inp()
    tests = 1

    for _ in range(tests):
        solve()


if __name__ == "__main__":
    main()
