import logging
import time
import sys
import os

# read all text from an input file for a given day e.g. day=6, the filepath will be '..\input\d6_input.txt'
# 'extra' can be used for test input files e.g. extra='_part1_test1', the filepath will be '..\input\d6_input_part1_test1.txt'
def aoc_read_input(year, day, extra=""):

    # path of this file
    path = os.path.dirname(__file__)

    # full path of the file required
    filepath = f"{path}\\input\\d{str(day)}_input{extra}.txt"

    # if an aoc input file, check if already exists on pc otherwise download it
    if not extra:

        # if the input file does not already exist, download it from the internet
        if not os.path.exists(filepath):

            """ This step depends on the browser used. It can be done through network inspection or, in advanced browser like Chrome, 
            by simply clicking on the View site information button directly left of the url (shown as a padlock), then clicking Cookies.
            Copy this cookie content and paste it in a file called 'session.txt' and place it in the 'private' sub-directory of this project. """
            # if you want autodownload of input files, place the contents of the session cookie for advent of code from your browser
            # in a file called 'session.txt' in the sub-directory named private. Advent of code requires login for input data access.
            session_filepath = f"{path}\\private\\session.txt"
            with open(session_filepath) as input_file:
                user_session_id = input_file.read()
            user_agent = "aoc downloader"

            try:
                import requests
            except ImportError:
                sys.exit(
                    "You need requests module. Install it by running pip install requests.")

            # download from internet
            url = f'https://adventofcode.com/{year}/day/{day}/input'
            with requests.get(url, cookies={"session": user_session_id}, headers={"User-Agent": user_agent}) as response:
                aoc_data = response.text.rstrip('\n')

            # save internet txt to input file
            with open(filepath, 'w') as output_file:
                output_file.write(aoc_data)

    with open(filepath) as input_file:
        file_content = input_file.read()

    return file_content

# Assists with outputing the result of part 1 or part 2 of an aoc day challenge ... includes the time taken for the part to execute
# Can also be used for other functions by not specifying year, month and day. In this case, the function output is not printed ... just function name and timing information.
def aoc_timer(year=0, day=0, part=0):
    part = {1: 'one', 2: 'two'}.get(part)
    prepend = ''
    if year:
        prepend += '%s.' % year
    if day:
        prepend += '%s ' % day
    if part:
        prepend += 'part %s: ' % part
    def decorator(func):
        # @functools.wraps(func) ... func.__name__ reports wrapper rather than func
        def wrapper(*a, **kw):
            try:
                start = time.perf_counter()
                result = func(*a, **kw)
                delta = (time.perf_counter() - start) * 1000
                if not prepend:
                    print(f'finished {func.__name__} in {delta:.4f} ms')
                else:
                    print(f'{prepend}{result} ({delta:.4f} ms)')
            except Exception as e:
                logging.exception(f'exception when solving {prepend}: {e}')
            else:
                return result
        return wrapper
    return decorator