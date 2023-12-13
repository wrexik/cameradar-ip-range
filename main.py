#Libraries
import random
import time as t
import sys
import os
import netaddr
from alive_progress import alive_bar

import subprocess

#Definitions / Functions
osn = os.name

#Functions
def clear():
    if(osn == 'posix'):
        os.system('clear')
    else:
        os.system('cls')

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

def get_len(list):
    count = 0
    for element in list:
        count += 1
    return count

def get_list(ip_from, ip_to):
    ip_list = list(netaddr.iter_iprange(ip_from, ip_to))
    ip_count = len(ip_list)
    return ip_list, ip_count

def run_container(target_ip):
    docker_command = ["docker", "run", "-d", "-t", "ullaakut/cameradar", "-t", target_ip, "-p", "554,5554,8554,8080"]
    global found_in_ip
    found_in_ip = 0
    try:
        # Run Docker container in detached mode and capture the container ID
        container_id = subprocess.check_output(docker_command, text=True).strip()

        # Show the output from Docker container in real-time
        docker_command = ["docker", "logs", "--follow", container_id]
        docker_process = subprocess.Popen(docker_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        print(" ")
        print(f"Output for {target_ip} (updating in real-time):")
        print(" ")

        # Loop to print output while the container is running
        for line in docker_process.stdout:
            print(line, end='')
            
            if not line.find("no stream found"):
                print("OK - Streams found")
                found_in_ip = +1

        docker_process.stdout.close()

        print(f"Successful scan for {target_ip}")

    except subprocess.CalledProcessError as e:
        print(f"Failed for {target_ip}")
        print(e.stderr)

    finally:
        # Remove the Docker container after checking
        subprocess.run(["docker", "rm", container_id])

def check_ip(ip_from, ip_list, ip_count):
    with alive_bar(ip_count, title="IP's Checked", bar="bubbles", monitor="Time elapsed", calibrate=5e40) as bar:
        for ip_address in ip_list:
            # Format the IP address for the Docker command
            target_ip = str(ip_address)

            print(f"Checking {target_ip}...")
            run_container(target_ip)

            t.sleep(0.5)
            bar()

# Code
ip_range = set_ips()

while True:
    decide = input("Is this right? [Y/N] ")

    if decide.lower() == "y":
        resume = True
        break
    else:
        print(" Gosh, well well...")
        set_ips()

if resume:
    clear()
    print("OK - Resuming")

ip_list, ip_count = get_list(ip_from, ip_to)

print("OK - IP addresses to be checked: {}".format(len(ip_list)))

print("OK - Started checking")

print("")

check_ip(ip_from, ip_list, ip_count)

print("Succesfully found: {}".format(found_in_ip))

