with open("input.txt") as f:
    lines_ = f.read().splitlines()


def search_for_symbol(x_end, y_end, number_length, lines) -> bool:
    points_to_check = []
    if x_end - 1 >= 0:
        points_to_check.extend([(x_end - 1, y_end + 1 - i) for i in range(number_length + 2) if y_end + 1 - i >= 0])
    if x_end + 1 < len(lines):
        points_to_check.extend([(x_end + 1, y_end + 1 - i) for i in range(number_length + 2) if y_end + 1 - i >= 0])
    if y_end + 1 < len(lines[x_end]):
        points_to_check.append((x_end, y_end + 1))
    if y_end - number_length >= 0:
        points_to_check.append((x_end, y_end - number_length))
    for x, y in points_to_check:
        if lines[x][y] in "!#$%&'()*+,-/:;<=>?@[]^_`{|}~":
            return True
    return False


def part_a(lines_):
    engine_sum = 0
    for x in range(len(lines_)):
        digits_ = []
        for y in range(len(lines_[x])):
            char_: str = lines_[x][y]
            if char_.isdigit():
                digits_.append(char_)
                continue
            if not (char_.isdigit()) and digits_:
                number = int("".join(digits_))
                if search_for_symbol(x, y - 1, len(digits_), lines_):
                    engine_sum += number
                    print(f"Found {number=} at ({x}, {y-1})")

                digits_.clear()
    return engine_sum
