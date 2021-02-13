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
        a, b, k = mul()
        boys = seq()
        girls = seq()
        edges = list(zip(boys, girls))
        num_edges = len(edges)

        bgraph = dict()
        ggraph = dict()

        for edge in edges:
            boy, girl = edge
            if boy in bgraph:
                bgraph[boy].append(girl)
            else:
                bgraph[boy] = [girl]

            if girl in ggraph:
                ggraph[girl].append(boy)
            else:
                ggraph[girl] = [boy]

        possible_pairs = 0
        for edge in edges:
            boy, girl = edge
            possible_pairs += (num_edges - (len(bgraph[boy]) + len(ggraph[girl])) + 1)

        print(possible_pairs//2)

    for _ in range(tests):
        solve()


if __name__ == "__main__":
    main()
