# Advent of code
# Author = Rob Lorimer
YEAR=2020; DAY=11; PART=2

import aoc
from copy import deepcopy
import math

def seat_status(grid, row, col):
    if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
        return grid[row][col]
    else:
        return '.'

r, c = 0, 1  # index of x and y axis in a point

def get_angle(seat1, seat2): 
    return math.atan2(seat2[c] - seat1[c], seat1[r] - seat2[r]) % (2 * math.pi)

def get_test_angles():
    test_angles = []
    test_angles.append(get_angle((0,0),(-1,0))) # 0 deg
    test_angles.append(get_angle((0,0),(-1,1))) # 45 deg
    test_angles.append(get_angle((0,0),(0,1))) # 90 deg
    test_angles.append(get_angle((0,0),(1,1))) # 135 deg
    test_angles.append(get_angle((0,0),(1,0))) # 180 deg
    test_angles.append(get_angle((0,0),(1,-1))) # 225 deg
    test_angles.append(get_angle((0,0),(0,-1))) # 270 deg
    test_angles.append(get_angle((0,0),(-1,-1))) # 315 deg
    return test_angles

def get_seats(grid):
    seats = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "#" or grid[row][col] == "L": 
                seats.append((row,col))
    return seats

def seat_test(grid, test_seat, test_angles):
    tr, tc = test_seat
    seats = get_seats(grid)
    if test_seat in seats: seats.remove(test_seat)
    seats_on_angles = []
    for seat in seats:
        if get_angle(test_seat, seat) in test_angles:
            seats_on_angles.append(seat)
    
    # sort each seat by it's length from our test_seat, sort seats by distance from our test_seat
    seats_on_angles.sort(key=lambda seat: math.hypot(seat[c] - test_seat[c], seat[r] - test_seat[r]))

    # rank each seat based on the number of seats on the same angle. 0 for closest, 1 for next closest
    ranks = {seat: sum(get_angle(test_seat, seat) == get_angle(test_seat, other_seat)
                for other_seat in seats_on_angles[:i]) for i, seat in enumerate(seats_on_angles)}
    
    # keep only closest
    visible_seats = {key:val for key, val in ranks.items() if val == 0}
    taken_seats_count = 0
    for key in visible_seats.keys():
        if grid[key[r]][key[c]]=="#":
            taken_seats_count += 1

    if grid[tr][tc] == "L":
        if taken_seats_count == 0:
            return "#"
        else:
            return "L"

    if grid[tr][tc] == "#":
        if taken_seats_count >= 5:
            return "L"
        else:
            return "#"
    return "."

@aoc.puzzle_timer()
def solve(input):
    test_angles = get_test_angles()
    grid_current = []
    grid_next = [list(line) for line in input.splitlines()]
    while grid_next!=grid_current:
        grid_current = deepcopy(grid_next)
        for row in range(len(grid_current)):
            for col in range(len(grid_current[0])):
                grid_next[row][col] = seat_test(grid_current, (row, col), test_angles)
    return sum(s.count('#') for s in grid_current)

if __name__ == '__main__':
    puzzle_input = aoc.puzzle_input(YEAR, DAY)
    print(f'Part {PART}: ', solve(puzzle_input))