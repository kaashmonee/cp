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
    n, m = mul()
    init = seq()
    desired = seq()
    colors = seq()

    # check the first case 
    # there are no common colors
    cm = colors[-1]
    x = -1
    for ind, color in enumerate(desired):
        if color == cm:
            x = ind
            if color != init[ind]:
                break

    desired_inds = dict()
    for ind, color in enumerate(desired):
        if color in desired_inds:
            desired_inds[color].append(ind)
        else:
            desired_inds[color] = [ind]

    for color in colors:
        

    if x == -1:
        print("NO")
        return

    


     

    

    # init_set = set([(ind, init[ind]) for ind in range(len(init))])
    # init_colors = set(init)
    # # init_color_map = {i: init[i] for i in range(len(init))}
    # desired_set = set([(ind, desired[ind]) for ind in range(len(init))])
    # changes = desired_set - init_set
    # color_changes = set([tup[1] for tup in changes])
    # clr_change_map = dict()
    # cur_color_map = dict()
    # cur_colors = init[::]

    # for tup in changes:
    #     # maps the color to the index
    #     if tup[1] not in clr_change_map:
    #         clr_change_map[tup[1]] = [tup[0]]
    #     else:
    #         clr_change_map[tup[1]].append(tup[0])

    # result = []

    # for clr in clrs:
    #     # i.e., there is a color that we don't want 
    #     if clr not in color_changes and clr not in init_colors:
    #         print("NO")
    #         return

    #     if clr in clr_change_map:
    #         ind = clr_change_map[clr][-1]
    #         result.append(clr_change_map[clr][-1])

    #         # cur_colors[clr].add(clr_change_map[clr][-1])
    #         prev_color = init[ind]
    #         cur_colors[ind] = clr

    #         clr_change_map[clr].pop()
    #         if len(clr_change_map[clr]) == 0:
    #             del clr_change_map[clr]

    #     else:
    #         if clr not in cur_color_map: 
    #             print("NO")
    #             return
    #         else:
    #             repaint = cur_colors_map[clr][0]
    #             results.append(repaint)








        

        
        


    


def main():

    tests = inp()



    for _ in range(tests):
        solve()


if __name__ == "__main__":
    main()
