#/usr/bin/python3

import argparse
from utils_event_4 import EventFourReader

parser = argparse.ArgumentParser(
        prog = 'AOC_day_two',
        description = 'The argparse for the advent of code for day two',
    )

parser.add_argument('--input_path', type=str, help='Input path for the task.')
parser.add_argument('--overlap', action='store_true', help='Investigate if there are overlapping ranges')


args = parser.parse_args()

if __name__ == '__main__':

    reader = EventFourReader(args.input_path)
    res = reader.handle_data(args.overlap)
    print(res)

