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

# creates an m x n matrix
matr   =lambda m, n: [[0] * n for _ in range(m)]

# list to str
lststr =lambda L: " ".join(list(map(str, L)))

mod=1000000007

#main code
def solve():
    N = inp()

    # obtains prime factors
    def pf(n):
        f = []

        while n % 2 == 0:
            f.append(2)
            n //= 2

        for i in range(3, int(math.sqrt(n))+1, 2):

            while n % i == 0:
                f.append(i)
                n //= i

        if n > 2:
            f.append(n)

        return f


    pfs = pf(N)
    pmax_mult = max(set(pfs), key=pfs.count)
    num_pmm = sum([1 if x == pmax_mult else 0 for x in pfs])
    result = [pmax_mult for _ in range(num_pmm)]
    for n in pfs:
        if n != pmax_mult:
            result[-1] *= n

    print(len(result))
    print(lststr(result))
    # i = len(pfs)-1
    # print("pfs:", pfs)

    # while i > 0:
    #     if pfs[i] % pfs[i-1] != 0:
    #         pfs = pfs[:i-1] + [pfs[i] * pfs[i-1]] + pfs[i+1:]
    #         i = len(pfs)-1
    #     else:
    #         i -= 1

    # print(len(pfs))
    # print(lststr(pfs))


# def lcml(a):
#     lcm = a[0]
#     for i in a[1:]:
#         lcm = lcm*i//math.gcd(lcm, i)

#     return lcm


def main():

    tests = inp()

    for _ in range(tests):
        solve()


if __name__ == "__main__":
    main()
