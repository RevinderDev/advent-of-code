data = open("input.txt").read().splitlines()

directions, _, *moves = data

from dataclasses import dataclass


@dataclass
class Directions:
    left: str
    right: str


moves_map = {}
for move in moves:
    x = move.split("=")
    moves_map[x[0].strip()] = Directions(left=x[1][2:5], right=x[1][7:10])

move = moves_map["AAA"]
moves = 0
broken = False
while True:
    for direction_str in directions:
        direction = move.left if direction_str == "L" else move.right
        moves += 1
        if direction == "ZZZ":
            broken = True
            break
        move = moves_map[direction]
    if broken:
        break

print(moves)
