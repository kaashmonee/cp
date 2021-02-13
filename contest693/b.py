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

    # def solve():
    #     n_candies = inp()
    #     candies = seq()
    #     w = sum(candies)

    #     def check(sack, cands):
    #         if sum(sack) == w // 2:
    #             return True
    #         elif sum(sack) > w // 2 or len(cands) == 0:
    #             return False

    #         for i in range(len(cands)):
    #             sack.append(cands[i])
    #             cands.pop(i)

    #             result = check(sack, cands)

    #             if result:
    #                 return True
                
    #             e = sack.pop()
    #             cands.insert(i, e)


    #     if w % 2 != 0:
    #         # w is odd
    #         print("NO")
    #         return

    #     if check([], candies):
    #         print("YES")
    #     else:
    #         print("NO")

    #     return

    def solve():
        n_candies = inp()
        candies = seq()
        w = sum(candies)

        if w % 2 != 0:
            print("NO")
            return

        num_ones = candies.count(1)
        if num_ones >= 2:
            print("YES")

        else:
            print("YES" if len(candies) % 2 == 0 else "NO")



        
    for _ in range(tests):
        solve()

if __name__ == "__main__":
    main()
