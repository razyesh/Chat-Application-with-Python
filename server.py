import socket
print('Setup Server...')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET = IPV4, SOCK_STREAM = TCP Protocol

"""
	Here client and server are in same computer, so we use gethostname() function
"""
host_name = socket.gethostname() #return name of the server
ip = socket.gethostbyname(host_name) #return the IP of the hostname
port = 1234

s.bind((host_name, port)) #assign IP and Port to server socket
print(host_name, f'({ip})')

name = input('Enter server name: ') #name of server

s.listen(2) #determine how many client server can listen

print('Waiting for incoming connections...')
connection, addr = s.accept() #if any clients request server -> server accept and kept the address and connection in tuple

print(f"Received connection from {addr[0]} ( {addr[1]} )")
print(f'Connection Established. Connected From: {addr[0]}, ({addr[1]})')

#get a connection from client side
client_name = connection.recv(1024) #receive name of client for chat
client_name = client_name.decode() #need to decode as client is sending data encoding

print(client_name + ' has connected.')

print('Press ctrl+c to leave the chat room')


connection.send(name.encode()) #server name is send to client

#receive content of file and store in separate file
file_data = connection.recv(1024) 
f = open('receive.txt','a')
f.write(file_data.decode())

#if client and server made a connection
while True:
   message = input(f'{name}: ')
   connection.send(message.encode())
   message = connection.recv(1024)
   message = message.decode()
   print(client_name, ':', message)