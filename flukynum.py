import random
import time
t = 0
l = 0
start = time.time()
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
   
end = time.time()
timer = end - start
print("It took " + str(round(timer, 2)) + " seconds")
print("Total loops: " + "7")

   