import socket

localIP     = "localhost"
localPort   = 20001
bufferSize  = 1024

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening")

while True:
    message,address = UDPServerSocket.recvfrom(1024)
    UDPServerSocket.sendto(b'asf',address)
    print("Message from Client:{}".format(message))
    #print("Client IP Address:{}".format(address))
