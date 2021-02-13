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
    n, k, p = mul()
    people = sorted(seq())
    keys = sorted(seq())

    print("people:", people)
    print("keys:", keys)

    # compute prefix sums of keys and people from the office
    # just consider one side (since left and right side are identicl)

    # prints the closest index to the office 
    closest_ind_keys = min(range(len(keys)), key = lambda i: abs(keys[i]-p)) 
    closest_ind_people = min(range(len(people)), key = lambda i: abs(people[i]-p))  

    lk = keys[:closest_ind_keys] if keys[closest_ind_keys] < p else keys[:closest_ind_keys+1]
    rk = keys[closest_ind_keys+1:] if keys[closest_ind_keys] < p else keys[closest_ind_keys:]
    lp = people[:closest_ind_people] if keys[closest_ind_people] < p else keys[:closest_ind_people+1]
    rp = people[closest_ind_people+1:] if keys[closest_ind_people] < p else keys[closest_ind_people:]



def main():

    # tests = inp()
    tests = 1

    for _ in range(tests):
        solve()


if __name__ == "__main__":
    main()
