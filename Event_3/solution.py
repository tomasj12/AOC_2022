#/usr/bin/python3

import argparse
from utils_event_3 import EventThreeReader

parser = argparse.ArgumentParser(
        prog = 'AOC_day_two',
        description = 'The argparse for the advent of code for day two',
    )

parser.add_argument('--input_path', type=str, help='Input path for the task.')
parser.add_argument('--group', action='store_true', help='Input path for the task.')

args = parser.parse_args()

if __name__ == '__main__':

    reader = EventThreeReader(args.input_path)
    res = reader.handle_data(args.group)
    print(res)

