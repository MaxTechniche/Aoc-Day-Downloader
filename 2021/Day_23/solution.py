from time import time, sleep
from pprint import pprint


INPUT_LINES = """#############
#...........#
###B#C#C#B###
  #D#D#A#A#
  #########"""

PART_2_INPUT_LINES = """#############
#...........#
###B#C#C#B###
  #D#C#B#A#
  #D#B#A#C#
  #D#D#A#A#
  #########"""

SAMPLE_LINES = """#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########"""

PART_2_SAMPLE_LINES = """#############
#...........#
###B#C#B#D###
  #D#C#B#A#
  #D#B#A#C#
  #A#D#C#A#
  #########"""

LINES = [list(line) for line in PART_2_INPUT_LINES.splitlines()]

SUCCESSES = []
LOWEST_COST = float('inf')
COSTS = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000
}
AM_ROOMS = {
    'A': 3,
    'B': 5,
    'C': 7,
    'D': 9
}
ILLEGAL_SPOTS = set([(1, 3), (1, 5), (1, 7), (1, 9)])
BOARD_POSITIONS = set()

SETS = {}


for x in range(len(LINES)):
    for y in range(len(LINES[x])):
        if LINES[x][y] in '.ABCD':
            BOARD_POSITIONS.add((x, y))


def display(ams):
    layout = """#############
#...........#
###.#.#.#.###
  #.#.#.#.#
  #########"""
    if len(ams) > 8:
        layout = """#############
#...........#
###.#.#.#.###
  #.#.#.#.#
  #.#.#.#.#
  #.#.#.#.#
  #########"""
    layout = [list(line) for line in layout.splitlines()]
    for am in ams:
        layout[am[0]][am[1]] = ams[am]

    for row in layout:
        print(''.join(row))


def store(ams):
    layout = """#############
#...........#
###.#.#.#.###
  #.#.#.#.#
  #########"""
    if len(ams) > 8:
        layout = """#############
#...........#
###.#.#.#.###
  #.#.#.#.#
  #.#.#.#.#
  #.#.#.#.#
  #########"""
    layout = [list(line) for line in layout.splitlines()]
    for am in ams:
        layout[am[0]][am[1]] = ams[am]

    grid = ''.join(layout[0])
    for row in layout[1:]:
        grid += '\n' + ''.join(row)

    return grid


def path_is_clear(cp, np, ams):
    row = 0
    column = 1
    if cp[row] > 1:
        for x in range(1, cp[row]):
            if (x, cp[column]) in ams:
                return False

    if np[row] > 1:
        for x in range(1, np[row]+1):
            if (x, np[column]) == cp:
                continue
            if (x, np[column]) in ams:
                return False

    if np[column] < cp[column]:
        for y in range(np[column], cp[column]):
            if (1, y) in ams:
                return False

    elif cp[column] < np[column]:
        for y in range(cp[column]+1, np[column]+1):
            if (1, y) in ams:
                return False

    return True


def legal_position(cp, np, ams):
    row = 0
    column = 1
    if np == cp:
        return False
    # Can only move into a room of its type
    if np[row] != 1 and np[column] != AM_ROOMS[ams[cp]]:
        return False
    # Cannot block a room
    if tuple(np) in ILLEGAL_SPOTS:
        return False
    # Can only move into or out of a room
    if cp[row] == np[row] == 1 or cp[column] == np[column]:
        return False
    # Cannot block a different letter when entering its room
    for x in range(np[row], len(LINES)):
        if (x, np[column]) in ams:
            if ams[(x, np[column])] in [ams[cp], '#']:
                continue
            return False
    return True


def in_own_room(am, ams):
    if am[1] == AM_ROOMS[ams[am]]:
        return True

    return False


def locked_in(cp, ams):
    if not in_own_room(cp, ams):
        return False

    for x in range(cp[0], len(LINES)):
        if (x, cp[1]) in ams and ams[(x, cp[1])] not in [ams[cp], '#']:
            return False

    return True


def move(am, np, ams):
    cost = 0
    if np[0] != 1:
        cost += abs(np[0] - 1)
    if am[0] != 1:
        cost += abs(am[0] - 1)
    cost += abs(am[1] - np[1])
    return cost * COSTS[ams[np]]


def all_in(ams):
    # for letter, room in zip(list('ABCD'), AM_ROOMS.values()):
    for pos, letter in ams.items():
        if AM_ROOMS[letter] != pos[1]:
            return False

    return True


def solve(ams, cost, move_set, cost_set, memo):
    if store(ams) in memo:
        if cost >= memo[store(ams)]:
            return

    memo[store(ams)] = cost
    global LOWEST_COST
    # display(ams)
    # sleep(.25)
    # print('')
    # if cost > LOWEST_COST:
    #     return
    if all_in(ams):
        print(LOWEST_COST, len(SUCCESSES))
        if SUCCESSES:
            if cost < LOWEST_COST:

                SETS[cost] = (move_set, cost_set)
                # for m, c in zip(move_set, cost_set):
                #     print(c)
                #     print(*m, sep='\n')
                #     print()
                # display(ams)
                print(cost, len(SUCCESSES))
                LOWEST_COST = cost
        SUCCESSES.append(cost)
        return
    for cp in list(ams):
        if locked_in(cp, ams):
            continue
        for position in BOARD_POSITIONS:
            if path_is_clear(cp, position, ams) \
                    and legal_position(cp, position, ams):
                old_pos = cp
                letter = ams[cp]
                del ams[old_pos]
                ams[position] = letter
                move_set.append(store(ams))
                cost_set.append(move(cp, position, ams))
                solve(ams, cost+move(cp, position, ams),
                      move_set, cost_set, memo)
                del ams[position]
                ams[old_pos] = letter
                move_set.pop()
                cost_set.pop()


def main():
    t1 = time()

    ams = {}
    layout = LINES
    for i, v in enumerate(layout):
        for j, k in enumerate(v):
            if k in 'ABCD':
                ams[(i, j)] = k

    memo = {}

    solve(ams, 0, [], [], memo)
    print(sorted(SUCCESSES))
    # display(layout)

    print("Time:", time() - t1)


main()
