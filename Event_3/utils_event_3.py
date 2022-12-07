import typing as t
import sys
sys.path.append("/home/tomas/Personal_projects/AOC_2022/utils")
from python.utils import Downloader, get_middle_word
import string


class EventThreeReader(Downloader):

    def __init__(self, input_path):
        super().__init__(input_path)
        self.prio_map = {
            y:x for x,y in zip(range(1,53),string.ascii_lowercase + string.ascii_lowercase.upper())
        }

    def read_data(self):

        with open(self.input_path, 'r') as file:

            data = file.readlines()
        
        self.data = [x.rstrip('\n') for x in data ]
    
    def handle_data(self,group: bool):

        self.read_data()
        if not group:
            things = [[x[:get_middle_word(x)],x[get_middle_word(x):]] for x in self.data]
        else:
            things = [self.data[(i-3):i] for i in range(3,len(self.data) + 1,3)]
            print(len(self.data))
        priorities = [self.prio_map[list(set(x[0]).intersection(x[1]).intersection(x[2]))[0]] for x in things]
        return sum(priorities)


        

    