import typing as t
import sys
sys.path.append("/home/tomas/Personal_projects/AOC_2022/utils")
from python.utils import Downloader


class EventOneReader(Downloader):

    def __init__(self, input_path):
        super().__init__(input_path)
    
    def read_data(self):

        with open(self.input_path, 'r') as file:

            data = file.readlines()
        
        self.data = [int(x.rstrip('\n')) if x != '\n' else ' ' for x in data ]
    
    def handle_data(self):

        self.read_data()
        final_list = []
        aux_list = []
        for l in self.data:
            if l != ' ':
                aux_list.append(l)
            else:
                final_list.append(aux_list)
                aux_list = []
        
        sum_list = [sum(x) for x in final_list]
        sum_list.sort()
        return sum_list[::-1]


        

    