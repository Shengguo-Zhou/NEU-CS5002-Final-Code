# Monte Carlo by Mersenne-Twist
import random

from time import time
import numpy as np

# var
index = 624
MT = [0] * index
# MT[0] ->seed


def inter(t):
    return(0xFFFFFFFF & t)  # get the last 32 digits -> t


def twister():
    global index
    for i in range(624):
        y = inter((MT[i] & 0x80000000) + (MT[(i + 1) % 624] & 0x7fffffff))
        MT[i] = MT[(i + 397) % 624] ^ y >> 1
        if y % 2 != 0:
            MT[i] = MT[i] ^ 0x9908b0df
    index = 0


def exnum():
    global index
    if index >= 624:
        twister()
    y = MT[index]
    y = y ^ y >> 11
    y = y ^ y << 7 & 2636928640
    y = y ^ y << 15 & 4022730752
    y = y ^ y >> 18
    index = index + 1
    return inter(y)


def mainset(seed):
    MT[0] = seed  # This is the seed
    for i in range(1, 624):
        MT[i] = inter(1812433253 * (MT[i - 1] ^ MT[i - 1] >> 30) + i)
    return exnum()


def main():
    pi = 0.0            # Assign a value (0.0) to pi
    radius = 10.0       # The radius of a circle
    num_in_square = 0   # Count the number of drop points in the square
    num_in_circle = 0   # Count the number of drop points in the circle
    MSG = ("In order to get a closer theoretical value, we recommend that" +
           "you enter a number n >= 9,999\n" +
           "Please enter the number of random drop points, n = ")

    # Get user's input as the amount of random samples.
    user_in = int(input(MSG))

    for i in range(user_in):
        # Set the coordinates of the drop point as (x, y)
        # random.uniform generates a random float in the range of +/- radius.
        mi = -radius
        ma = radius
        so = mainset(int(time())) / (2**32-1)
        x = mi + int((ma - mi) * so)
        print(x)
        so = mainset(int(time())) / (2**32-1)
        y = mi + int((ma - mi) * so)
        print(y)

        # (dis) represents the distance from drop point to center of circle
        dis = (x ** 2 + y ** 2) ** 0.5

        # Let's count the number of drop points
        if dis > radius:       # Drops fall in the square but not in the circle
            num_in_square += 1
        else:     # (dis <= radius) Drops fall in the square also in the circle
            num_in_circle += 1
            num_in_square += 1

        # In case the divisor is 0, we will ignore that case.
        if num_in_square == 0:
            continue

        pi = num_in_circle / num_in_square * 4       # Caculate the pai.

    print("We used {} random drops and caculated that, \nPi = {}".
          format(user_in, pi))


if __name__ == "__main__":
    main()
