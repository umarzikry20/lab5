import socket
import sys

if(len(sys.argv) >1):
	serverIP = sys.argv[1]
else:
	print("\n\n Run like \n phython3 5.4.client.py 192.168.56.107 \n\n")
	exit(1)

s = socket.socket()

PORT = 9898

s.connect((ServerIP, PORT))

print("Which file you want to sent?")
filename = input("Enter filename:")
print("Filename: " + filename)

file = open(filename,"rb")
SendData = file.read(1024)

while SendData:
	print("\n\n-----Below message is received from server----- \n\n", s.recv(1024).decode("utf-8"))
	s.send(SendData)
	SendData = file.read(1024)

s.close()
