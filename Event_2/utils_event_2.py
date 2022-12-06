import typing as t
import sys
sys.path.append("/home/tomas/Personal_projects/AOC_2022/utils")
from python.utils import Downloader


class EventTwoReader(Downloader):

    def __init__(self, input_path):
        super().__init__(input_path)
        self.mapping = {
            'A X': 1 + 3,
            'A Y': 2 + 6,
            'A Z': 3 + 0,
            'B X': 1 + 0,
            'B Y': 2 + 3,
            'B Z': 3 + 6,
            'C X': 1 + 6,
            'C Y': 2 + 0,
            'C Z': 3 + 3
        }

        self.mapping_adj = {
            'A X': 3 + 0,
            'A Y': 1 + 3,
            'A Z': 2 + 6,
            'B X': 1 + 0,
            'B Y': 2 + 3,
            'B Z': 3 + 6,
            'C X': 2 + 0,
            'C Y': 3 + 3,
            'C Z': 1 + 6,
        }

    def read_data(self):

        with open(self.input_path, 'r') as file:

            data = file.readlines()
        
        self.data = [x.rstrip('\n') for x in data ]
    
    def handle_data(self,adj: bool=False):

        self.read_data()
        mapping = self.mapping if not adj else self.mapping_adj
        score = [mapping[x] for x in self.data]
        
        return sum(score)


        

    