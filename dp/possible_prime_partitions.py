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
# probmlem: https://www.geeksforgeeks.org/count-of-ways-to-split-a-given-number-into-prime-segments/
# solution

def solve(s):

    # dp approach
    # define dp memoization table
    # dp[i] = the number of ways that you can split up
    # s[:i] into prime partitions

    def is_prime(ns):
        n = int(ns)
        if n % 2 == 0: return False

        d = 3
        while d**2 <= n:
            if n % d == 0:
                return False
            d += 2

        return True

    dp = dict()
    dp[0] = 1

    def solve_rec(ns, i):
        # ns is the number but is a string
        # i is the index

        if i in dp:
            return dp[i]

        cnt = 0

        for j in range(1, 7):
            # number shouldn't have leading zero and 
            # it should be prime
            if (i - j >= 0 and is_prime(ns[i-j:i]) and ns[i-j] != "0"):
                cnt += solve_rec(ns, i - j)
                cnt %= mod

        dp[i] = cnt
        return dp[i]

    return solve_rec(s, len(s))

    


def run_tests():
    tests = [
        "3175",
        "11753",
        "373",
    ]

    results = [
        3,
        4,
        3            
    ]
    for i in range(len(tests)):
        print(solve(tests[i]))

    print("All tests passed...")


def main():
    run_tests()


if __name__ == "__main__":
    main()
