import random

t = 0
while t <= 7:
    for n in range(1, 10000):
        FT = 0
        for factor in range(1, n):
            if n % factor == 0:
                random.seed(factor)
                FT += random.randint(1, n)
        if n == FT:
            print(str(n) + " is a flucky number.")
        t += 1

   