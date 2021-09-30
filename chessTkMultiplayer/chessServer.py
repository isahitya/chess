import socket

s=socket.socket()

port=12345

s.bind(('',port))

s.listen(2)

bottomPlayerSocket,bottomPlayerAddr=s.accept()
data=bottomPlayerSocket.recv(1024)
print(data)
bottomPlayerSocket.sendall("bottom".encode())
topPlayerSocket,topPlayerAddr=s.accept()
data=topPlayerSocket.recv(1024)
print(data)
topPlayerSocket.sendall("top".encode())

chance="bottom"
bottomPlayerSocket.sendall(chance.encode())
topPlayerSocket.sendall(chance.encode())


while True:
	if chance=="bottom":
		move=bottomPlayerSocket.recv(1024)
		move=move.decode()
		if move=="nothing":
			print(move)
			topPlayerSocket.sendall("nothing".encode())
		elif (move.split(':'))[0]=="move":
			print("Sending move :"+move)
			topPlayerSocket.sendall(move.encode())
			chance="top"
	else:
		move=topPlayerSocket.recv(1024)
		move=move.decode()
		if move=='nothing':
			print(move)
			bottomPlayerSocket.sendall("nothing".encode())
		elif (move.split(':'))[0]=="move":
			print("Sending move :"+move)
			bottomPlayerSocket.sendall(move.encode())
			chance="bottom"
