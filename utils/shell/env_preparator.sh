#!/usr/bin/bash

day=$1
path=~/Personal_projects/AOC_2022/Event_$day

mkdir Event_$day && mkdir Event_$day/data && touch $path/solution.py && touch $path/utils_event_$day.py

sh /home/tomas/Personal_projects/AOC_2022/utils/shell/data_downloader.sh $day