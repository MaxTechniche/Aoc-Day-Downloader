from time import time
import re
from pprint import pprint
import math

t1 = time()


def intify(val):
    if val[1] == "x":
        return val
    return val[0], int(val[1])


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


bods = {}


def get_dist(left_bus, right_busses=None):
    print()
    print(left_bus, right_busses)
    # print(bods)
    if not right_busses:
        print("[] caught")
        return lcm(left_bus[0], left_bus[1])
    if right_busses[0] not in bods:
        bods[right_busses[0]] = get_dist(right_busses[0], right_busses[1:])

    print(bods)

    departure_distance = right_busses[0][0] - left_bus[0]
    id = right_busses[0][1] - left_bus[1]
    return lcm(bods[right_busses[0]], lcm(departure_distance, id))


with open("2020/Day_13/input") as f:
    file = f.readlines()
    early_time = int(file[0])
    busses = list(enumerate(map(int, re.findall("(\d+)", file[1]))))
    busses_p2 = list(map(intify, enumerate(file[1].split(","))))
    busses_p2 = [x for x in busses_p2 if x[1] != "x"]

print(early_time)
print(busses)

print()

busses = [(bus, bus - (early_time % bus)) for i, bus in busses]
busses.sort(key=lambda x: (x[1], -x[0]))

print(busses)
# next_bust = busses[]
print(busses[0][0] * busses[0][1])


print(busses_p2)
print(get_dist(busses_p2[0], busses_p2[1:]))

print("Time:", time() - t1)


100000000000000
320985598345147335600
73757063715720