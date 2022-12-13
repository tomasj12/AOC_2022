#/usr/bin/python3

import argparse
from utils_event_5 import EventFiveReader

parser = argparse.ArgumentParser(
        prog = 'AOC_day_two',
        description = 'The argparse for the advent of code for day two',
    )

parser.add_argument('--input_path', type=str, help='Input path for the task.')
parser.add_argument('--order', action='store_true', help='Change order of the crates moved')


args = parser.parse_args()

if __name__ == '__main__':

    reader = EventFiveReader(args.input_path)
    reader.handle_data(args.order)
    res = [y[-1] for x,y in reader.crates.items()]
    print(''.join(res).replace('[','').replace(']',''))
    #res = reader.handle_data(args.group)
    #print(res)

