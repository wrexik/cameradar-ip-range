#Libraries
import random
import time as t
import sys
import os
import netaddr
from alive_progress import alive_bar

#Definitions / Functions
osn = os.name

#Functions
def clear():
    if(osn == 'posix'):
        os.system('clear')
    else:
        os.system('cls')

#Code
def set_ips():
    while True:
        try: 
            text = str("Input the first IP address (FROM), after each number pres enter: ")
            feild_1 = int(input(text))
            clear()
            break
        except:
            clear()
            print("Thats not a number try again")

    while True:
        try: 
            text = "Input the first IP address: {}.".format(feild_1)
            feild_2 = int(input(text))
            clear()
            break
        except:
            clear()
            print("Thats not a number try again")

    while True:
        try: 
            text = "Input the first IP address: {}.{}.".format(feild_1, feild_2)
            feild_3 = int(input(text))
            clear()
            break
        except:
            clear()
            print("Thats not a number try again")

    while True:
        try: 
            text = "Input the first IP address: {}.{}.{}.".format(feild_1, feild_2, feild_3)
            feild_4 = int(input(text))
            clear()
            break
        except:
            clear()
            print("Thats not a number try again")


    ip = str(feild_1) + "." + str(feild_2) + "." + str(feild_3) + "." + str(feild_4)

    print("Selected IP (FROM) {}, now enter the second ip (TO)".format(ip))

    while True:
        try: 
            text = str("Input the second IP address (TO), after each number pres enter: ")
            feild_1_1 = int(input(text))
            clear()
            break
        except:
            clear()
            print("Thats not a number try again")

    while True:
        try: 
            text = "Input the second IP address: {}.".format(feild_1_1)
            feild_1_2 = int(input(text))
            clear()
            break
        except:
            clear()
            print("Thats not a number try again")

    while True:
        try: 
            text = "Input the second IP address: {}.{}.".format(feild_1_1, feild_1_2)
            feild_1_3 = int(input(text))
            clear()
            break
        except:
            clear()
            print("Thats not a number try again")

    while True:
        try: 
            text = "Input the second IP address: {}.{}.{}.".format(feild_1_1, feild_1_2, feild_1_3)
            feild_1_4 = int(input(text))
            clear()
            break
        except:
            clear()
            print("Thats not a number try again")

    global ip_from
    global ip_to

    ip_from = str(feild_1) + "." + str(feild_2) + "." + str(feild_3) + "." + str(feild_4)
    ip_to = str(feild_1_1) + "." + str(feild_1_2) + "." + str(feild_1_3) + "." + str(feild_1_4)

    print("Selected IP (FROM) {}".format(ip_from))
    print("Selected IP (TO) {}".format(ip_to))

def get_list():
    global list
    global ip_count

    list = list(netaddr.iter_iprange(ip_from, ip_to))

    ip_count = range(len(list))

    return ip_count


range = set_ips()


while True:

    deside = input("Is this right? [Y/N] ")

    if deside == "y" or deside == "Y":
        resume = True
        break

    else:
        print(" Gosh, well well...")
        set_ips()

if resume == True:
    print("OK - Resuming")

get_list()

print("OK - IP addresses to be checked: {}".format(len(list)))

print(type(len(list)))

print("OK - Started checking")

def check_ip():
    for total in ip_count:
        with alive_bar(total) as bar:
            for _ in range(ip_count):


                t.sleep(1)
                bar()


check_ip()







    

