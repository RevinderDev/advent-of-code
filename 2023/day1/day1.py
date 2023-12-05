import re


def part_a(data: list[str]) -> list[int]:
    numbers = []
    for line in data:
        digits = re.findall(r"(\d)", line)
        numbers.append(int(digits[0] + digits[-1]))
    return numbers


def part_b(data: list[str]) -> list[int]:
    numbers = []
    for line in data:
        for i, number in enumerate(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
            line = line.replace(number, number + str(i + 1) + number)
        digits = re.findall(r"(\d)", line)
        numbers.append(int(digits[0] + digits[-1]))
    return numbers


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        input_ = f.read().splitlines()
    print(f"A: {sum(part_a(input_))}")
    print(f"B: {sum(part_b(input_))}")
