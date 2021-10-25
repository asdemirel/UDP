from ctypes import windll
from os import execv
import socket

HOST = "localhost"
PORT = 12345

try:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print('[INFO] SOCKET OLUŞTURULDU')
    s.bind((HOST,PORT))
    print("[INFO] {} nolu port aktif edildi.".format(PORT))

    s.listen(5)
    print('[INFO] Port Dinleniyor...')
    port, address = s.accept()
    print('[INFO] porta gelen bağlantı {} '.format(address))

    while True:
        port.send(b'Client Servera baglandin')
        receive_data = port.recv(1024)
        print(receive_data.decode("utf-8"))
except socket.error as errormesage:
    print('[INFO] HATA: ', errormesage)
  


   

