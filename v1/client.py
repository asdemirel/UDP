import socket

HOST = "localhost"
PORT = 12345

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    s.connect((HOST,PORT))
    print('[INFO] SERVER BAGLANTISI SAGLANDI')
    receive_data = s.recv(1024)
    print(repr(receive_data))
    while True:
        mesaj = input()
        s.sendall(mesaj.encode('utf-8'))

except socket.error as errormesage:
    print('[INFO] Server ile bağlantı kurulamadı. -->',errormesage)
