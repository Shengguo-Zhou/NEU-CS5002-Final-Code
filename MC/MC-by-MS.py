# Monte Carlo by Middle-Square
import random

from time import time


def rander(i, seed, n, radius):
    if n == 1:
        return 0
    seed = int(seed) * i
    length = len(str(seed))
    seed = int(seed**2 / pow(10, (length / 2))) % int(pow(10.0, length))
    while(seed > radius or seed < -radius):
        seed = seed / 10
        seed = -seed
    return seed


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
        seed = time()
        x = rander(i, seed, 100, radius)
        print(x)
        y = rander(rander(i, seed, 100, radius), seed, 100, radius)
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
