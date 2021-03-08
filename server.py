import socket
import threading


port = 5500
IP = socket.gethostbyname(socket.gethostname())
ADDR = (IP,port)
FORMAT = 'utf-8'

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def writing(conn, addr):
	connected = True
	while connected:
		server_msg = input(">")
		conn.send(server_msg.encode(FORMAT))
		if server_msg == "END":
			connected = False
	conn.close()

def reading(conn, addr, name):
	print(f"[NEW CONNECTION] formed with {name}")
	connected = True
	while connected:
		msg = conn.recv(2048).decode(FORMAT)
		if msg == "END":
			connected = False
		print(f"[{name}]: {msg}")
	conn.close()


def start():
	server.listen()
	print(f"[SERVER] Ready to listen....on {IP}")
	while True:
		conn, addr = server.accept()
		name = conn.recv(2048).decode(FORMAT)
		thread1 = threading.Thread(target =reading,args = (conn, addr,name))
		thread1.start()
		thread2 = threading.Thread(target =writing,args= (conn, addr))
		thread2.start()
		print(f"[ACTIVE CONNECTIONS] {(threading.activeCount() - 1)/2}")
	pass
start()

