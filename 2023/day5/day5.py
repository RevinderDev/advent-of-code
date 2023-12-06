def part_a():
    seeds, *blocks = open("input.txt").read().split("\n\n")
    seeds = list(map(int, seeds.split(":")[1].split()))
    for block in blocks:
        ranges = [list(map(int, line.split())) for line in block.splitlines(1)[1:]]
        new = []
        for seed in seeds:
            for destination, source, step in ranges:
                if seed in range(source, source + step):
                    new.append(destination + (seed - source))
                    break
            else:
                new.append(seed)
        seeds = new
    print(min(seeds))


part_a()

from functools import reduce


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


