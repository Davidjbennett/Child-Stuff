# K is 2^10
# M is 2^20
# G is 2^30
# T is 2^40

import random
import math
numList = [1,2,4,8,16,32,64,128,256,512]
numFollower = {'':0,'K':10,'M':20,'G':30,'T':40}
Win = False
counter = 0

while(Win == False):
    log = numList[random.randint(0,9)]
    lgKys = list(numFollower.keys())
    logLet = lgKys[random.randint(0,4)]
    print(numFollower[logLet])
    logString = str(log) + str(logLet)

    Uinput = input("log " + logString + ": ")

    userInt = int(Uinput)

    if(int(math.log2(log)) + numFollower[logLet] == userInt):
        counter += 1
        print(counter, "in a row correct")
        if(counter == 3):
            print("Flippity Flip you won!")
            Win = True
    else:
        counter = 0
        print("Wrong, try again.")