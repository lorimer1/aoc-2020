# 2020 Advent of Code (AOC)
Advent of Code is an Advent calendar of small programming puzzles for a variety of skill sets and skill levels that can be solved in any programming language you like. People use them as a speed contest, interview prep, company training, university coursework, practice problems, or to challenge each other.

https://adventofcode.com/2020/about

# Coding Environment and Automatic Download of Input Files
Windows 10,
Python 3.9.0,
Visual Studio Code
    Extensions:
        Python (Microsoft),
        Pylance (Microsoft)

Download and save your input files in the 'input' folder.
    Name each file 'dn_input.txt' e.g. 'd1_input.txt'

Input files are read using the 'aoc_read_input' function in 'aoc_utils.py'

If you wish to use the automated download feature:
    Install the 'requests' module into Python i.e. 'python -m pip install requests'
    Add a folder named 'private' to the project root with a file named 'session.txt' i.e. 'private\session.txt'
    Add the value of your session cookie for aoc website from your browser:
        To obtain the cookie e.g. chrome ... right-click the padlock in the address bar and click cookies (use the value of the cookie named 'session' for advent of code site)

# New Python things I tried this year
Decorators: Custom decorator 'aoc_timer' was added to my functions to calculate and print timing information. This basically wraps the functions inside extra code that will time the running of the functions and print the return value of the functions with timing information. The decorator code is in 'aoc_utils.py'



