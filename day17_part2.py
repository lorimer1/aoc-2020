# Advent of code
# Author = Rob Lorimer
YEAR=2020; DAY=17; PART=2

import aoc
import copy

ACTIVE, INACTIVE = '#','.'
CYCLES = 6
OFFSETS = (-1,0,1)

@aoc.puzzle_timer()
def solve(input):
    grid = {}

    # initialise 2D  grid at z=0
    z,w=0,0
    for y, line in enumerate(input.splitlines()):
        for x, c in enumerate(line):
            grid[(x,y,z,w)] = c

    for cycle in range(CYCLES):
        # add new layer of empty units 
        # i.e. extend the full grid by 1 unit in all directions
        grid_copy = copy.deepcopy(grid)
        for k in grid_copy.keys(): # use a copy for iteration vars so changes to grid don't cause side-effects
            x,y,z,w = k
            for dx in OFFSETS:
                for dy in OFFSETS:
                    for dz in OFFSETS:
                        for dw in OFFSETS:
                            xt=x+dx; yt=y+dy; zt=z+dz; wt=w+dw
                            test_k=(xt,yt,zt,wt)
                            if test_k not in grid:
                                grid[test_k]=INACTIVE
        
        # create a new gid from the old; make changes to that so we don't get side affects during iteration of orginal
        grid_next = copy.deepcopy(grid)
        for k,v in grid.items():
            active_count=0
            x,y,z,w = k
            for dx in OFFSETS:
                for dy in OFFSETS:
                    for dz in OFFSETS:
                        for dw in OFFSETS:
                            xt=x+dx; yt=y+dy; zt=z+dz; wt=w+dw
                            test_k=(xt,yt,zt,wt)
                            test_v=grid.get(test_k, INACTIVE)
                            if k==test_k: #skip testing our unit
                                continue
                            if test_v==ACTIVE:
                                active_count+=1
            if v==ACTIVE and not active_count in (2,3):
                grid_next[k]=INACTIVE
            if v==INACTIVE and active_count==3:
                grid_next[k]=ACTIVE

        grid=copy.deepcopy(grid_next)

    return len([v for v in grid.values() if v==ACTIVE])  

if __name__ == '__main__':
    puzzle_input = aoc.puzzle_input(YEAR, DAY)
    print(f'Part {PART}: ', solve(puzzle_input))