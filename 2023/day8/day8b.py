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

ghosts = [moves_map[key] for key in moves_map if key.endswith("A")]
moves = 0
broken = False
while True:
    for direction_str in directions:
        new_ghosts_spots = []
        current_ghost_spots = []
        for ghost in ghosts:
            direction = ghost.left if direction_str == "L" else ghost.right
            moves += 1
            current_ghost_spots.append(direction)
            new_ghosts_spots.append(moves_map[direction])
        for current_ghost_spots in current_ghost_spots:
            if not current_ghost_spots.endswith("Z"):
                break
        else:
            broken = True
            break
        ghosts = new_ghosts_spots
    if broken:
        break

print(moves // len(ghosts))
