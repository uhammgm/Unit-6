E1 = 0
E2 = 0 
keeper = 0
KF1 = 0 #keeper found elephant 1
KF2 = 0 #keeper found elephant 2 
KFB = 0 #keeper found both
t = 0
import random 
response = "Y"
while response == "Y":
    while t <= 100000:
        E1 = random.randint(1,6)
        E2 = random.randint(1,6)
        keeper = random.randint(1,6)
        if E2 == keeper and E1 == keeper:
            KFB += 1
        elif E1 == keeper:
            KF1 += 1
        elif E2 == keeper: 
            KF2 += 1
        t += 1
    
    KF1 = round(KF1/1000, 2)
    KF2 = round(KF2/1000, 2)
    KFB = round(KFB/1000, 2)


    print(KF1)
    print(KF2)
    print(KFB)

    print("~~~~~REPORT~~~~~")
    print("There is at least one elephant in the pen " + str(round(KF1 + KF2 + KFB, 2)) + " percent of the time.")
    print("Both elephants are in the pen the keeper checks " + str(KFB) + " percent of the time.")
    print("Based on this, the zookeeper is incorrect.")
    response = input("Run the simulation again? Y or N ")



