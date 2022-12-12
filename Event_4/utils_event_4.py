import typing as t
import sys
sys.path.append("/home/tomas/Personal_projects/AOC_2022/utils")
from python.utils import Downloader


class EventFourReader(Downloader):

    def __init__(self, input_path):
        super().__init__(input_path)

    def read_data(self):

        with open(self.input_path, 'r') as file:

            data = file.readlines()
        
        self.data = [x.rstrip('\n') for x in data ]
    
    def handle_data(self, overlap):

        self.read_data()
        ranges_ = [x.split(',') for x in self.data]
        ranges = [
            [
                set(range(int(x[0].split('-')[0]),int(x[0].split('-')[1]) + 1)),
                set(range(int(x[1].split('-')[0]),int(x[1].split('-')[1]) + 1))
            ]   for x in ranges_
        ]

        print(ranges)
        ct = 0
        for l in ranges:
            
            if not overlap:
                res = l[0] - l[1] if len(l[0]) < len(l[1]) else l[1] - l[0]
                if len(res) == 0:
                    ct += 1
            else:
                res = l[0].intersection(l[1])
                if len(res) > 0:
                    ct += 1
                

        return ct


        

    