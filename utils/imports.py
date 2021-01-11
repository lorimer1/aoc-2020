# add project directory to path
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#into_sets = partial(map, set)
from functools import partial


from functools import reduce


# combinations(numbers, 2)
# combinations(numbers, 3) 
from itertools import combinations 

# count(0, 3)
from itertools import count

# re_policy = re.compile(r'(\d+)-(\d+) (\w): (\w+)')
# policies = re_policy.findall(input)
import re

