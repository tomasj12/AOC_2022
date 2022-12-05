#/usr/bin/bash
session=$1
day=$2

output_path="Event_$day/data/input.txt"

curl --cookie "session=$session" "https://adventofcode.com/2022/day/${day}/input" -o $output_path