#Libraries
import random
import time as t
import sys
import os

#Definitions / Functions
osn = os.name

#Functions
def clear():
    if(osn == 'posix'):
        os.system('clear')
    else:
        os.system('cls')

#Code

while True:
    try: 
        text = str("Input the first IP address, after each number pres enter: ")
        feild_1 = int(input(text))
        clear()
        break
    except:
        print("Thats not a number try again")

while True:
    try: 
        text = "Input the first IP address: {}.".format(feild_1)
        feild_2 = int(input(text))
        clear()
        break
    except:
        print("Thats not a number try again")

while True:
    try: 
        text = "Input the first IP address: {}.{}.".format(feild_1, feild_2)
        feild_3 = int(input(text))
        clear()
        break
    except:
        print("Thats not a number try again")


while True:
    try: 
        text = "Input the first IP address: {}.{}.{}.".format(feild_1, feild_2, feild_3)
        feild_4 = int(input(text))
        clear()
        break
    except:
        print("Thats not a number try again")



    


