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
strseq =lambda: list(map(str, input().strip().split()))

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
    s = strng()
    letters = strseq()
    print("letters:", letters)

    mem = [[False] * n for _ in range(n)]
    for i in range(n):
        mem[i][i] = s[i] in letters
    

    mem[0][1] = s[0] in letters

    for i in range(n-1):
        for j in range(i+1, n):
            mem[i][j] = mem[i][j-1] and (s[j] in letters)
    import pprint
    mem = [list(map(int, row)) for row in mem]
    pprint.PrettyPrinter().pprint(mem)

    # result = sum([sum(d.values()) for d in mem.values()])
    result = sum([sum(row) for row in mem])
    print(result)



def main():

    # tests = inp()
    tests = 1

    for _ in range(tests):
        solve()


if __name__ == "__main__":
    main()
