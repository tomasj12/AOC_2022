#/usr/bin/python3

import argparse
from utils_event_1 import EventOneReader

parser = argparse.ArgumentParser(
        prog = 'AOC_day_one',
        description = 'The argparse for the advent of code for day one',
    )

parser.add_argument('--input_path', type=str, help='Input path for the task.')
parser.add_argument('--top_n', type=int, help = 'Top n calories')

args = parser.parse_args()

if __name__ == '__main__':

    reader = EventOneReader(args.input_path)
    res = reader.handle_data()
    if args.top_n == 1:
        print(f'The most calories are {res[0]}')
    else:
        print(f'The sum of top {args.top_n} is {sum(res[:args.top_n])}')

