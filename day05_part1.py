# Advent of code
# Author = Rob Lorimer
YEAR=2020; DAY=5; PART=1

from utils import aoc

def binary_to_decimal(binary):
    decimal, pos = 0, 0
    reversed = binary[::-1]
    for d in reversed:
        decimal = decimal + d * pow(2, pos)
        pos+=1
    return decimal    


def get_seat(barcode):
    row_text = barcode[:7]
    row_binary = []
    for d in row_text:
        if d=="F":
            row_binary.append(0)
        else:
            row_binary.append(1)
    row = binary_to_decimal(row_binary)

    col_text = barcode[-3:]
    col_binary = []
    for d in col_text:
        if d=="L":
            col_binary.append(0)
        else:
            col_binary.append(1)
    col = binary_to_decimal(col_binary)

    seat = row * 8 + col

    return seat


@aoc.puzzle_timer()
def solve(input):
    seats=[]
    lines = input.splitlines()
    for line in lines:
        seats.append(get_seat(line))
    return max(seats)

if __name__ == '__main__':
    puzzle_input = aoc.puzzle_input(YEAR, DAY)
    print(f'Part {PART}: ', solve(puzzle_input))