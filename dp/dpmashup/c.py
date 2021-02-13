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

    # keeps track of 
    dp = {
        "A": math.inf,
        "B": math.inf,
        "C": math.inf,
        "AB": math.inf,
        "AC": math.inf,
        "BC": math.inf,
        "ABC": math.inf,
    }
    unseen = set(["A", "B", "C"])

    while n > 0:
        s = strng().split()
        price = int(s[0])
        vits = "".join(sorted(s[1]))

        if "A" in vits: unseen -= set(["A"])
        if "B" in vits: unseen -= set(["B"])
        if "C" in vits: unseen -= set(["C"])

        if price < dp[vits]:
            dp[vits] = price

        n -= 1

    result = min([
        dp["A"] + dp["B"] + dp["C"],
        dp["AB"] + dp["C"],
        dp["AC"] + dp["B"],
        dp["BC"] + dp["A"],
        dp["AB"] + dp["BC"],
        dp["AC"] + dp["BC"],
        dp["AC"] + dp["AB"],
        dp["ABC"],
    ])

    if len(unseen) > 0:
        print(-1)
        return

    print(result)


def main():

    # tests = inp()
    tests = 1

    for _ in range(tests):
        solve()


if __name__ == "__main__":
    main()
