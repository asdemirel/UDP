import socket
import time
import json
import datetime
import threading 

class UDPclient():
    def __init__(self):
        settings= json.load(open('settings.json'))
        self.logFolder = open('log.txt','a+')
        self.logFolder.write(str(datetime.datetime.now())+'\n')
        self.logFolder.close()
        self.HOST = settings['HOST']
        self.PORT = settings['PORT']
        self.UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.UDPClientSocket.sendto(b'START',(self.HOST,self.PORT))
        time.sleep(1)
        self.counter = 0
        self.msgFromServer = None
        self.address = None

    def getMessage(self):
        while True:
            try:
                self.msgFromServer,self.address = self.UDPClientSocket.recvfrom(1024)  # veri gelene kadar kod burada takılır.
                msgLog = open('servermessageLog.txt','a+') 
                msgLog.write(str(self.msgFromServer) + '     '+ str(self.address) +'\n') #msgLog.write(msgFromServer.decode('utf-8') + '     '+ str(address) +'\n')
                msgLog.close()
                print("Address {} - Message from Server  -> {} <-".format(self.address, self.msgFromServer))
            except:
                pass

    def sendMessage(self):
        while True:
            try:
                mesaj = str(self.counter)
                time.sleep(1)
                self.UDPClientSocket.sendto(mesaj.encode('utf-8'),(self.HOST,self.PORT))    # Thread olayını bu şekilde yaptığımızda çalışmasını istediğimiz fonk run olmalı.
                print(self.counter)
                self.counter +=1

            except Exception as errorMessage:
                logFolder = open('log.txt','a+')
                print('[INFO] HATA:',errorMessage)
                if str(errorMessage) !=  open('log.txt','r').readlines()[-1][:-1]:
                    logFolder.write(str(errorMessage)+'\n')
                    logFolder.close()

    def run(self):
        threading.Thread(target=self.sendMessage).start()
        threading.Thread(target=self.getMessage).start()

if __name__ == "__main__":
    com = UDPclient()
    com.run()