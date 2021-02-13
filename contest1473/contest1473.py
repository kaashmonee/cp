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


def problema():
    num_cases = inp()

    for _ in range(num_cases):
        n, d = mul()
        arr = seq()

        def solve(arr, d):
            for i in range(len(arr)):
                for j in range(i+1, len(arr)):
                    if arr[i]+arr[j] <= d:
                        return True


            # if there are no pairs that sum to d or less
            # then check to see if every element is less than or
            # equal to d and return the result (i.e., 0 applciations)
            # of ai = aj + ak
            return len(list(filter(lambda x: x <= d, arr))) == len(arr)

        print("YES" if solve(arr, d) else "NO")



def main():
    problema()

if __name__ == "__main__":
    main()


