import re
from operator import mul
from functools import reduce


def part_a():
    data = open("input.txt").read().split("\n")
    times, distances = data

    times = list(map(int, re.sub(" +", " ", times.split(":")[1]).strip().split(" ")))
    distances = list(map(int, re.sub(" +", " ", distances.split(":")[1]).strip().split(" ")))

    all_ways_to_beat = []

    for time, distance in zip(times, distances):
        ways_to_beat = 0
        for time_button_held in range(1, time + 1):
            time_left = time - time_button_held
            if time_left * time_button_held > distance:
                ways_to_beat += 1
        all_ways_to_beat.append(ways_to_beat)
    print(reduce(mul, all_ways_to_beat))


def part_b():
    data = open("input.txt").read().split("\n")
    times, distances = data
    time = int(re.sub(" ", "", times.split(":")[1]))
    distance = int(re.sub(" ", "", distances.split(":")[1]))

    ways_to_beat = 0
    for time_button_held in range(14, time + 1):
        time_left = time - time_button_held
        if time_left * time_button_held > distance:
            ways_to_beat += 1
    print(ways_to_beat)


part_a()
part_b()
