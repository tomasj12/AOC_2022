import typing as t
from abc import ABC, abstractmethod

class Downloader(ABC):

    def __init__(self,input_path: t.Literal[str]):

        self.input_path = input_path
    
    @abstractmethod
    def read_data(self):
        pass
    
    # Is done by each event separately
    @abstractmethod
    def handle_data(self):
        pass

    def __str__(self):

        str_ = self.input_path.split('/')
        day_ = str_[0].split('_')[1]

        return f"The data for the day {day_}!"

def get_middle_word(word: str) -> str:
    
    k = len(word)
    return k // 2