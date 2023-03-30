def countBackwards(step = 1, beg = 100, end = 0):
    Counting = beg
    print("I am counting backwards.")
    while(Counting >= end):
        print(Counting)
        Counting -= step

def countToNum(step, beg = 0, end = 100):
    count = beg
    print("I am counting fowards.")
    while(count <= end):
        print(count)
        count += step

def main():
    countToNum(5, 80, 100)
    print("~~~~~~~~~~")
    countBackwards(10, 80, 10)
    print("~~~~~~~~~~")
    

main()