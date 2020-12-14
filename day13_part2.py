# Advent of code
# Author = Rob Lorimer
YEAR=2020; DAY=13; PART=2

from aoc_utils import aoc_read_input, aoc_timer

@aoc_timer()
def solve(input):
    arrival, timetable = input.splitlines()
    bus_wait_times = {}
    for route in timetable.split(','):
        if not route == 'x':
            bus = int(route)
            bus_wait_times[bus] = (bus * (int(arrival)//bus) + bus) - int(arrival)
    best_bus = min(bus_wait_times, key=bus_wait_times.get)
    return best_bus * bus_wait_times[best_bus]

if __name__ == '__main__':
    puzzle_input = aoc_read_input(YEAR, DAY)
    print(f'Part {PART}: ', solve(puzzle_input))