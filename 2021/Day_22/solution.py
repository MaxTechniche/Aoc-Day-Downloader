from time import time
import numpy as np


def parse(step, offset=0):
    o, step = step.split()
    o = True if o == 'on' else False
    x, y, z = step.split(',')
    x = x.split('..')
    y = y.split('..')
    z = z.split('..')

    x[0] = x[0][2:]
    x = [xn+offset for xn in map(int, x)]
    y[0] = y[0][2:]
    y = [yn+offset for yn in map(int, y)]
    z[0] = z[0][2:]
    z = [zn+offset for zn in map(int, z)]

    return o, x, y, z


def main():
    t1 = time()

    with open("2021/Day_22/sample_input") as f:
        steps = f.read().splitlines()

    cuboid = np.ndarray((101, 101, 101), bool)

    for step in steps:
        o, x, y, z = parse(step, 50)
        cuboid[
            x[0]:x[1]+1,
            y[0]:y[1]+1,
            z[0]:z[1]+1
        ] = o

    print(cuboid.sum())

    print("Time:", time() - t1)


main()
