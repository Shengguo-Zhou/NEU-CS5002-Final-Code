# Linear Congruential Generator - Improve

from time import time


m = 2**32
a = 1103515245
c = 12345
rdls = []


def LCG(seed, mi, ma, n):
    if n == 1:
        return 0
    else:
        seed = (a * seed + c) % m
        rdls.append(int((ma-mi)*seed/float(m-1)) + mi)
        LCG(seed, mi, ma, n - 1)


def main():
    br = input("Please input the range of the random number\
 (Seperate with ','): ")
    co = eval(input("Please input the number of random number\
 you want to generate: "))
    mi = eval(br.split(',')[0])
    ma = eval(br.split(',')[1])
    seed = time()
    LCG(seed, mi, ma, co + 1)
    print("The random number is ", rdls)


main()
