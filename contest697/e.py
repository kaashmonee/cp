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
        n, k = mul()
        blgrs = seq()
        blgrs = sorted(blgrs)
        print("blgrs:", blgrs)
        max_sum = sum(blgrs[-k:])
        print("max_sum:", max_sum)

        ways = [0]

        def ks(sack, bloggers):
            # base case
            if len(sack) >= k:
                if sum(sack) == max_sum:
                    return True

                return False

            # not base case
            for ind, blogger in enumerate(bloggers):

                sack.append(blogger)
                bloggers.pop(ind)

                success = ks(sack, bloggers)

                if success:
                    ways[0] += 1
                else:
                    sack.pop()
                    bloggers.insert(ind, blogger)

        ks([], blgrs)

        print(ways[0] % mod)

    for _ in range(tests):
        solve()


if __name__ == "__main__":
    main()
