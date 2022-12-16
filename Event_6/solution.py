#/usr/bin/python3

import argparse
from utils_event_6 import EventSixReader

parser = argparse.ArgumentParser(
        prog = 'AOC_day_two',
        description = 'The argparse for the advent of code for day two',
    )

parser.add_argument('--input_path', type=str, help='Input path for the task.')
parser.add_argument('--message_length',type=int, help='Decide the length of the encrypted message')

args = parser.parse_args()

if __name__ == '__main__':

    reader = EventSixReader(args.input_path)
    reader.handle_data(args.message_length)
    #res = reader.handle_data(args.group)
    #print(res)

