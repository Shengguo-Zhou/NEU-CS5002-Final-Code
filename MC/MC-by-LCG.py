# Monte Carlo by LCG
import random

from time import time


def LCG(i, seed, mi, ma, n):
    m = 2**32
    a = 1103515245
    c = 12345
    rdls = []
    if n == 1:
        return 0
    else:
        seed = ((a + i) * seed + c) % m
        rdls.append(int((ma-mi)*seed/float(m-1)) + mi)
        LCG(i, seed, mi, ma, n-1)
    return rdls[0]


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
    # Start a timer
    from time import time
    time_begin = time()
    for i in range(user_in):
        # Set the coordinates of the drop point as (x, y)
        # random.uniform generates a random float in the range of +/- radius.
        mi = -radius
        ma = radius
        seed = time()
        x = LCG(i, seed, mi, ma, 2)
        print(x)

        seed = time()
        y = LCG(LCG(i, seed, mi, ma, 2), seed, mi, ma, 2)
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
        # End the timer
    
    time_end = time()
    time_used = time_end - time_begin
    print("Time duration (seconds):", time_used)
    print("We used {} random drops and caculated that, \nPi = {}".
          format(user_in, pi))


if __name__ == "__main__":
    main()
