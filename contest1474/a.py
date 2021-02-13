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

    n_cases = inp()

    def solve(n, b):
        if n == 0:
            return ""

        # n >= 1        
        a = "1"
        d = str(int(a) + int(b[0]))
        # print("n:", n, "b:", b, "d:", d)
        for ind in range(1, n):
            s = b[ind]
            # print("d:", d)
            if d[ind-1] == "2":
                if s == "1":
                    a += "0"
                elif s == "0":
                    a += "1"
                
                d += "1"

            elif d[ind-1] == "1":
                if s == "1":
                    a += "1"
                    d += "2"
                elif s == "0":
                    a += "0"
                    d += "0"

            elif d[ind-1] == "0":
                a += "1"
                if s == "0":
                    d += "1"
                elif s == "1":
                    d += "2"


        return a


    for _ in range(n_cases):
        length = inp()
        second_int = strng()
        print(solve(length, second_int))



if __name__ == "__main__":
    main()
