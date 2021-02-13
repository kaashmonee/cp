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

# choose the greater number
def problemb():
    num_cases = inp()

    def do_lcm(x, y):

        if x > y:
           greater = x
        else:
           greater = y

        while(True):
            if((greater % x == 0) and (greater % y == 0)):
                lcm = greater
                break
            greater += 1

        return lcm

    def divisible(s1, s2):
        # check to see if s2 is divisble
        # by s1
        if len(s2) <= len(s1):
            return s1 == s2 * (len(s1) // len(s2))

        return False



    # solution: find the LCM string and then check
    # to see if it's divisble by both a and b
    for _ in range(num_cases):
        str1 = strng()
        str2 = strng()

        lcm_lengths = do_lcm(len(str1), len(str2))
        # print("lcm_lengths:", lcm_lengths)
        smaller = str1 if len(str1) < len(str2) else str2
        larger = str2 if smaller != str2 else str1

        lcm_string = smaller * (lcm_lengths // len(smaller))
        if divisible(lcm_string, smaller) and divisible(lcm_string, larger):
            print(lcm_string)
        else:
            print("-1")


def main():
    problemb()

if __name__ == "__main__":
    main()




