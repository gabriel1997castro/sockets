import socket

L = int(input())

for i in range(L):
    IP = input()
    hostName = socket.gethostbyaddr(IP)
    print(hostName[0])