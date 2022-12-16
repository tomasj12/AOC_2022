import typing as t
import sys
sys.path.append("/home/tomas/Personal_projects/AOC_2022/utils")
from python.utils import Downloader, get_middle_word
import string
import re


class EventSixReader(Downloader):

    def __init__(self, input_path):
        super().__init__(input_path)
        self.prio_map = {
            y:x for x,y in zip(range(1,53),string.ascii_lowercase + string.ascii_lowercase.upper())
        }

    def read_data(self):

        with open(self.input_path, 'r') as file:

            data = file.readlines()
        
        self.data = [x.rstrip('\n') for x in data][0]

    
    def handle_data(self,length: int):

        self.read_data()
        print(self.data)
        for i in range(length,len(self.data)):
            counter = {}
            stream = self.data[(i-length):i]
            print(stream)
            ct = 0
            for char in stream:
                if char in counter.keys():
                    counter[char] += 1
                    break
                else:
                    counter[char] = 1
                ct +=1
            
            if ct == length:
                self.res = i
                print(self.res)
                break


        


        

    