import socket
import threading
import sys 

port = 5500
FORMAT = 'utf-8'
IP = socket.gethostbyname(socket.gethostname())
ADDR = (IP,port)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def writing():
	connected = True
	while connected:
		client_msg = input(">")
		client.send(client_msg.encode(FORMAT))
		if client_msg == "END":
			connected = False

def reading():
	connected = True
	while connected:
		msg = client.recv(2048).decode(FORMAT)
		if msg == "":
			connected = False
		print(f"[SERVER]: {msg}")


def start():
	client.connect(ADDR)
	name = input("Enter your name....")
	client.send(name.encode(FORMAT))
	print(f"[{name}] connected....on {IP}")
	thread1 = threading.Thread(target = reading)
	thread1.start()
	thread2 = threading.Thread(target =writing)
	thread2.start()

start()