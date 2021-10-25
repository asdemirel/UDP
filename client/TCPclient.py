import socket
import time

HOST = "localhost"
PORT = 12345
counter = 0

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def reconnectServer(s):
    try:
        s.close()
        print("Reconnect to the server!")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST,PORT))
       
    except:
        print('SERVER AÇIK DEĞİL')
    
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:

    s.connect((HOST,PORT))
    print('[INFO] SERVER BAGLANTISI SAGLANDI') 

    while True:
        try:
            mesaj = str(counter)
            s.sendall(mesaj.encode('utf-8'))
            time.sleep(2)
            counter +=1
        except Exception:
                print("[INFO] HATA !!! ")
                reconnectServer(s)
                continue