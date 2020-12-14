import re
from time import time
from pprint import pprint

t1 = time()

with open("2020/Day_14/input") as f:
    memory = f.read().splitlines()


def set_bits(number, mask):
    number = list(number.zfill(36))
    for i, val in enumerate(mask[::-1], 1):
        if val in ["0", "1"]:
            number[-i] = val
    return "".join(number)


mem = {}

for instruction in memory:
    if instruction[:4] == "mask":
        mask = re.findall("\d.+", instruction[7:])
        mask = mask[0] if mask else "0"
        continue

    m, num = re.findall("\d+", instruction)
    mem[m] = set_bits(str(bin(int(num))[2:]), mask)

total = 0
for val in mem.values():
    total += int(val, 2)

print("Part 1:", total)

print("Time:", time() - t1)
