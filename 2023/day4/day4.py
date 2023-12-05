import re
from collections import defaultdict


with open("input.txt") as f:
    lines_ = f.read().splitlines()


def part_a():
    points = 0

    for line in lines_:
        game = line.split(":")[1]
        winning_numbers, chosen_numbers = game.split("|")
        winning_numbers = set(map(int, re.sub(" +", " ", winning_numbers).strip().split(" ")))
        chosen_numbers = set(map(int, re.sub(" +", " ", chosen_numbers).strip().split(" ")))
        initial_points = 0
        for chosen_number in chosen_numbers:
            if chosen_number in winning_numbers:
                initial_points = 1 if initial_points == 0 else initial_points * 2
        points += initial_points

    print(f"Part a: {points}")


part_a()


def part_b():
    dict_ = defaultdict(int)

    for i in range(len(lines_)):
        line = lines_[i]
        game = line.split(":")[1]
        winning_numbers, chosen_numbers = game.split("|")
        winning_numbers = set(map(int, re.sub(" +", " ", winning_numbers).strip().split(" ")))
        chosen_numbers = set(map(int, re.sub(" +", " ", chosen_numbers).strip().split(" ")))
        initial_points = 0
        dict_[i + 1] += 1
        for chosen_number in chosen_numbers:
            if chosen_number in winning_numbers:
                initial_points += 1
        for value in range(initial_points):
            if i + 1 in dict_:
                adder = dict_[i + 1]
            else:
                adder = 1
            dict_[value + i + 2] += adder
    print(f"Part b: {sum(dict_.values())}")


part_b()
