#/usr/bin/python3

import argparse
from utils_event_2 import EventTwoReader

parser = argparse.ArgumentParser(
        prog = 'AOC_day_two',
        description = 'The argparse for the advent of code for day two',
    )

parser.add_argument('--input_path', type=str, help='Input path for the task.')
parser.add_argument('--adj', action='store_true', help='Decide if to adjust the technique.')


args = parser.parse_args()

if __name__ == '__main__':

    reader = EventTwoReader(args.input_path)
    res = reader.handle_data(adj=args.adj)
    print(res)

