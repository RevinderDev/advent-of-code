histories = open("input.txt").readlines()


def do_magic_a(history):
    history = list(map(int, history.split(" ")))
    histories = [history]
    while True:
        followup_history = []
        for i in range(len(history) - 1):
            diff = history[i + 1] - history[i]
            followup_history.append(diff)
        history = followup_history
        histories.append(followup_history)
        if followup_history.count(0) == len(followup_history):
            break
    for i in reversed(range(len(histories))):
        A = histories[i][-1] + histories[i - 1][-1]
        histories[i - 1].append(A)
    return histories[0][-1]


result = 0
for history in histories:
    result += do_magic_a(history)

print(f"Part A = {result}")


def do_magic_b(history):
    history = list(map(int, history.split(" ")))
    histories = [history]
    while True:
        followup_history = []
        for i in range(len(history) - 1):
            diff = history[i + 1] - history[i]
            followup_history.append(diff)
        history = followup_history
        histories.append(followup_history)
        if followup_history.count(0) == len(followup_history):
            break
    for i in reversed(range(1, len(histories))):
        A = histories[i - 1][0] - histories[i][0]
        histories[i - 1].insert(0, A)
    return histories[0][0]


result = 0
for history in histories:
    result += do_magic_b(history)

print(f"Part B = {result}")
