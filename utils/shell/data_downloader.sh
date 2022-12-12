#/usr/bin/bash
day=$1

output_path="Event_$day/data/input.txt"

curl --cookie "session=53616c7465645f5f9a675ab25a03c67b8039cdda4f589c06515d9c2f62f4f99e4211c4f1ae89ba1f2f9b61d250a1fdf41977035f81cbd486d99a094a69bc023c" "https://adventofcode.com/2022/day/${day}/input" -o $output_path