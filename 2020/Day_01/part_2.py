from itertools import combinations
import time

t1 = time.time()

with open('2020/Day_01/input') as i:
    numbers = [int(n) for n in i.read().split('\n') if n]
    perms = combinations(numbers, 3)
    for perm in perms:
        if sum(perm) == 2020:
            print(perm[0] * perm[1] * perm[2])
            break

print('Time:', time.time()-t1)
