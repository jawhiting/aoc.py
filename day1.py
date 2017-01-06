def add(a, b):
    return a[0] + b[0], a[1] + b[1]


directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def right(curr_dir):
    curr_pos = directions.index(curr_dir)
    next_pos = (curr_pos + 1) % len(directions)
    return directions[next_pos]


def left(curr_dir):
    curr_pos = directions.index(curr_dir)
    next_pos = (curr_pos - 1)
    if next_pos < 0:
        next_pos = len(directions) - 1
    return directions[next_pos]


def distance(point):
    return abs(point[0]) + abs(point[1])


def travelled_distance(input):
    visited = set()
    curr = 0, 0
    inc = 0, 1

    for move in input.split(sep=", "):
        dir = move[0]
        amt = int(move[1:])
        if dir == "R":
            inc = right(inc)
        else:
            inc = left(inc)
        for i in range(amt):
            curr = add(curr, inc)
            if curr in visited:
                print("Revisited {}".format(curr))
            else:
                visited.add(curr)
    return distance(curr)


input = "R1, R3, L2, L5, L2, L1, R3, L4, R2, L2, L4, R2, L1, R1, L2, R3, L1, L4, R2, L5, R3, R4, L1, R2, L1, R3, L4, R5, L4, L5, R5, L3, R2, L3, L3, R1, R3, L4, R2, R5, L4, R1, L1, L1, R5, L2, R1, L2, R188, L5, L3, R5, R1, L2, L4, R3, R5, L3, R3, R45, L4, R4, R72, R2, R3, L1, R1, L1, L1, R192, L1, L1, L1, L4, R1, L2, L5, L3, R5, L3, R3, L4, L3, R1, R4, L2, R2, R3, L5, R3, L1, R1, R4, L2, L3, R1, R3, L4, L3, L4, L2, L2, R1, R3, L5, L1, R4, R2, L4, L1, R3, R3, R1, L5, L2, R4, R4, R2, R1, R5, R5, L4, L1, R5, R3, R4, R5, R3, L1, L2, L4, R1, R4, R5, L2, L3, R4, L4, R2, L2, L4, L2, R5, R1, R4, R3, R5, L4, L4, L5, L5, R3, R4, L1, L3, R2, L2, R1, L3, L5, R5, R5, R3, L4, L2, R4, R5, R1, R4, L3"

print("Distance is {}".format(travelled_distance(input)))
