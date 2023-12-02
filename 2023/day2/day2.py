from functools import reduce

MAXES = {"red": 12, "green": 13, "blue": 14}


def part_a(lines: str) -> int:
    def is_game_possible(game: str) -> bool:
        for round in game.split(";"):
            for cubes in round.split(","):
                number, color = cubes.strip().split(" ")
                if int(number) > MAXES.get(color):
                    return False
        return True

    game_id_sum = 0
    for line in lines:
        game_number, game = line.split(": ")
        game_number = int(game_number.split("Game ")[1])
        if is_game_possible(game):
            game_id_sum += game_number
    return game_id_sum


def part_b(lines: str) -> int:
    def find_power(game: str) -> int:
        minimals = {"red": 0, "green": 0, "blue": 0}
        for round in game.split(";"):
            for cubes in round.split(","):
                number, color = cubes.strip().split(" ")
                minimals[color] = max(int(number), minimals.get(color))
        return reduce(lambda x, y: x * y, minimals.values())

    power_sum = 0
    for line in lines:
        game_number, game = line.split(": ")
        game_number = int(game_number.split("Game ")[1])
        power_sum += find_power(game)
    return power_sum


if __name__ == "__main__":
    with open("input.txt") as f:
        lines_ = f.read().splitlines()
    print(f"A = {part_a(lines_)}")
    print(f"B = {part_b(lines_)}")
