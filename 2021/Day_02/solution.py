from time import time

t1 = time()

with open("2021/Day_02/input") as f:
    lines = [x.split(" ") for x in f.read().splitlines()]
    
hor = 0
ver = 0

for direction, unit in lines:
    if direction == "forward":
        hor += int(unit)
    elif direction == "down":
        ver += int(unit)
    elif direction == "up":
        ver -= int(unit)
        
print("Horizontal:", hor)
print("Vertical:", ver)
print(hor*ver)

    
print("Time:", time() - t1)

# Part 2
t1 = time()

with open("2021/Day_02/input") as f:
    lines = [x.split(" ") for x in f.read().splitlines()]

hor = 0
ver = 0
aim = 0

for direction, unit in lines:
    if direction == "forward":
        hor += int(unit)
        ver += int(unit) * aim
    elif direction == "down":
        aim += int(unit)
    elif direction == "up":
        aim -= int(unit)

print("Horizontal:", hor)
print("Vertical:", ver)
print(hor*ver)


print("Time:", time() - t1)
