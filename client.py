import socket
print('Client Server...')


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET = IPV4, SOCK_STREAM = TCP Protocol

"""
   Here client and server are in same computer, so we use gethostname() function
"""

host = socket.gethostname() #return name of the server
ip = socket.gethostbyname(host) #return the IP of the hostname

print(host, f'({ip})')
server_host = socket.gethostname() #we need to define it, since both are in same computer we call gethostname() function

name = input('Your Name: ') #asks user to input name
port = 1234 #client port number

print(f'Trying to connect to the server: {server_host}, ({port})')
s.connect((server_host, port))
print("Connected\n")

s.send(name.encode()) #send server name to client
server_name = s.recv(1024) #receive server name from server
server_name = server_name.decode()
print(f'{server_name} has joined')
print('Enter ctrl+c to leave chat room: ')

#send the content of file from client to server
f = open('raz.txt','r')
r = f.read()
s.send(r.encode())


"""
   Both are connected so unitl and unless one do not press ctrl + c it keeps running
"""

while True:
   message = s.recv(1024)
   message = message.decode()
   print(server_name, ">", message)
   message = input(str(f"{name}: "))
   s.send(message.encode())