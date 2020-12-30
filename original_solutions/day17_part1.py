# Advent of code
# Author = Rob Lorimer
YEAR=2020; DAY=17; PART=1

# add project directory to path
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import aoc
import copy

ACTIVE, INACTIVE = '#','.'
CYCLES = 6
OFFSETS = (-1,0,1)


def print_grid(grid):
    """ prints current state of the grid """
    z_keys = [k[2] for k in grid.keys()]
    for z in range(min(z_keys),max(z_keys)+1):
        print (f'\nz={z}')
        y_keys = [k[1] for k in grid.keys()]
        for y in range(min(y_keys),max(y_keys)+1):
            line=''        
            x_keys = [k[0] for k in grid.keys()]
            for x in range(min(x_keys),max(x_keys)+1):
                line+=grid[(x,y,z)]
            print(line)          

@aoc.puzzle_timer()
def solve(input):
    grid = {}

    # initialise 2D  grid at z=0
    z=0
    for y, line in enumerate(input.splitlines()):
        for x, c in enumerate(line):
            grid[(x,y,z)] = c

    for cycle in range(CYCLES):
        # add new layer of empty units 
        # i.e. extend the full grid by 1 unit in all directions
        grid_copy = copy.deepcopy(grid)
        for k in grid_copy.keys(): # use a copy for iteration vars so changes to grid don't cause side-effects
            x, y, z = k
            for dx in OFFSETS:
                for dy in OFFSETS:
                    for dz in OFFSETS:
                        xt=x+dx; yt=y+dy; zt=z+dz
                        test_k=(xt,yt,zt)
                        if test_k not in grid:
                            grid[test_k]=INACTIVE
        
        # create a new gid from the old; make changes to that so we don't get side affects during iteration of orginal
        grid_next = copy.deepcopy(grid)
        for k,v in grid.items():
            active_count=0
            x, y, z = k
            for dx in OFFSETS:
                for dy in OFFSETS:
                    for dz in OFFSETS:
                        xt=x+dx; yt=y+dy; zt=z+dz
                        test_k=(xt,yt,zt)
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

        # print_grid(grid)

    return len([v for v in grid.values() if v==ACTIVE])  

if __name__ == '__main__':
    puzzle_input = aoc.puzzle_input(YEAR, DAY)
    print(f'Part {PART}: ', solve(puzzle_input))