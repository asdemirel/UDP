import socket
import time
import json
import datetime

settings= json.load(open('settings.json'))

logFolder = open('log.txt','a+')
logFolder.write(str(datetime.datetime.now())+'\n')
logFolder.close()

HOST = settings['HOST']
PORT = settings['PORT']

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
counter = 0

while True:
    try:
        print(counter)
        mesaj = str(counter)
        time.sleep(1)
        UDPClientSocket.sendto(mesaj.encode('utf-8'),(HOST,PORT))
    
        msgFromServer,address = UDPClientSocket.recvfrom(1024)

        msgLog = open('servermessageLog.txt','a+')
        #msgLog.write(msgFromServer.decode('utf-8') + '     '+ str(address) +'\n')
        msgLog.write(str(msgFromServer) + '     '+ str(address) +'\n')
        msgLog.close()


        print("Address {} - Message from Server  -> {} <-".format(address, msgFromServer))
        counter +=1
    except Exception as errorMessage:
        logFolder = open('log.txt','a+')
        print('[INFO] HATA:',errorMessage)
        if str(errorMessage) !=  open('log.txt','r').readlines()[-1][:-1]:
            logFolder.write(str(errorMessage)+'\n')
            logFolder.close()
        