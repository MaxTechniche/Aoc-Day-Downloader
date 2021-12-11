import time
from pprint import pprint

t1 = time.time()

with open("2020/Day_01/input") as f:
    nums = list(map(int, f.readlines()))

n = len(nums)

for i in range(n):
    for j in range(i + 1, n):
        if nums[i] + nums[j] == 2020:
            print("Part 1:", nums[i] * nums[j])
        elif nums[i] + nums[j] < 2020:
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 2020:
                    print("Part 2:", nums[i] * nums[j] * nums[k])

print("Time:", time.time() - t1)  # .02
