import typing as t
import sys
sys.path.append("/home/tomas/Personal_projects/AOC_2022/utils")
from python.utils import Downloader, get_middle_word
import string
import re


class EventFiveReader(Downloader):

    def __init__(self, input_path):
        super().__init__(input_path)
        self.prio_map = {
            y:x for x,y in zip(range(1,53),string.ascii_lowercase + string.ascii_lowercase.upper())
        }

    def read_data(self):

        with open(self.input_path, 'r') as file:

            data = file.readlines()
        
        self.data = [x.rstrip('\n') for x in data]
        crates_ = []
        movements_ = []
        
        for i in range(len(self.data)):
            if self.data[i] == '':
                crates_.extend(self.data[:i])
                movements_.extend(self.data[i+1:])
                break
        
        stacks = crates_[-1].rstrip().lstrip().split('   ')
        crates_ = [x for x in crates_[:-1]]
        crates = {str(k+1):[] for k in range(len(stacks))}
        for x in crates_:
            k = 0
            j = 2
            for i in range(len(stacks)):
                crates[str(i+1)].append(x[k:j+1])
                k += 4
                j += 4
        self.crates = {}
        for i in range(len(stacks)):
            self.crates[str(i+1)] = [x for x in crates[str(i+1)] if x != '   '][::-1]
        self.movements = [[int(re.findall(r'\d+',x)[0]),re.findall(r'\d+',x)[1],re.findall(r'\d+',x)[2]] for x in movements_]

    
    def handle_data(self,order: bool):

        self.read_data()

        for move in self.movements:
            if not order:
                self.crates[move[2]].extend(self.crates[move[1]][-move[0]:][::-1])
            else:
                self.crates[move[2]].extend(self.crates[move[1]][-move[0]:])
            self.crates[move[1]] = self.crates[move[1]][:-move[0]]
        


        

    