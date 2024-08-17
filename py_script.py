#!/usr/bin/python

## Function: plus two numbers

## Uasge: python py_script.py \
#         --first 2 \
#         --second 3

# load libraries
import argparse as ap
import yaml as yl

# load modules
from modules.func import plus

# read yml
with open('config.yml', 'r') as ymlfile:
    cfg = yl.safe_load(ymlfile)

VERSION = cfg['version']

# Usage
message_prog = 'python py_script.py (' + VERSION + ')'
message_description = 'plus two numbers'

# example
message_epilog = """
python py_script.py \
--first 2 \
--second 3 \
"""

## set argparse
parser = ap.ArgumentParser(
    prog=message_prog, # usage
    description=message_description, # function description
    epilog=message_epilog)

parser.add_argument('-f','--first', type=int, help='first number', default=0)
parser.add_argument('-s','--second', type=int, help='second number', default=0)

# get parse_args object
args = parser.parse_args()

# do something
result = plus(args.first, args.second)
print('first number:', args.first)
print('second number:', args.second)
print('result:', result)
