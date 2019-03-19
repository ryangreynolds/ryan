import socket
import time

def send(message, ip = "127.0.0.1"):
	port = 5005
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	
	sock.sendto(message.encode(), (ip, port))
	#sock.sendall(message, (ip, port))

msg=''
while msg != "quit":
	msg = input("Command: ")
	send (msg)
	#send('a,b,c')

