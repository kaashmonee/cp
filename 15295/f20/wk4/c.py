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
    arr = seq()
    if len(arr) == 2:
        if arr[0] == arr[1]:
            print(1)
            return

        print(2)
        return
            
    
    # make the dictionary that contains all the indices
    ind_dict = dict()
    for ind, e in enumerate(arr):
        if e not in ind_dict:
            ind_dict[e] = [ind]
        else:
            ind_dict[e].append(ind)


    # now zigzag through the list
    unq_es = set(arr)
    max_len = -1
    seen = set()
    in_seen = lambda tup: tup in seen or (tup[1], tup[0]) in seen

    for e1 in unq_es:
        for e2 in unq_es:
            if e1 == e2 or in_seen((e1, e2)):
                continue

            # zig zag
            e1inds = sorted(ind_dict[e1])
            e2inds = sorted(ind_dict[e2])
            cur = e1inds
            nxt = e2inds

            if nxt[0] < cur[0]:
                cur, nxt = nxt, cur

            cur_len = 0
            while len(cur) > 0 and len(nxt) > 0:
                while len(nxt) > 0 and cur[0] > nxt[0]:
                    nxt.pop(0)

                cur_len += 1
                cur.pop(0)
                cur, nxt = nxt, cur

            if cur_len > max_len:
                max_len = cur_len

            # indicate that we've already done this before 
            seen.add((e1, e2))

    if max_len > 1:
        print(max_len+1)
    else:
        print(max_len)



def main():

    tests = 1
    # tests = inp()

    for _ in range(tests):
        solve()


if __name__ == "__main__":
    main()
