import time

numbers = {}

t1 = time.time()

with open('2020/Day_01/input') as i:
    for num in i.read().split('\n'):
        num = int(num) if num else 0
        if 2020 - num in numbers:
            print(numbers[2020 - num] * num)
            break
        numbers[num] = num

t2 = time.time()
print('Time:', t2-t1)
