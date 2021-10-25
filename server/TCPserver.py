import socket

HOST = "localhost"
PORT = 12345

def create_server(s):
    s.close()
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print('[INFO] SOCKET OLUŞTURULDU')
    s.bind((HOST,PORT))
    s.listen(5)
    print('[INFO] Port Dinleniyor...')
    port, address = s.accept()
    print('[INFO] porta gelen bağlantı {} '.format(address))
    return port

while True:
    
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        port = create_server(s)
        port.send(b'Client Servera baglandin')
        receive_data = port.recv(1024)
        print(receive_data.decode("utf-8"))
        port.sendall(receive_data)

    except Exception:
        pass