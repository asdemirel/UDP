import socket
import json
import threading 

class UDPserver():
    def __init__(self):
        self.settings = json.load(open(r'C:\Users\ahmet\Desktop\ICM-github\src\setting.json'))
        self.HOST = self.settings['HOST']
        self.PORT = self.settings['PORT']
        self.LOGO_NAME = self.settings['logo_name']
        self.sendCorrect = False
        self.binding()
  
    def binding(self):
        self.connectUDP = False
        self.ServerSocket = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
        self.ServerSocket.bind((self.HOST,self.PORT))
        threading.Thread(target=self.firstContact,name='firstContact Thread').start()

    def firstContact(self):
        print('[INFO] UDP LISTENING...') 
        _,self.address = self.ServerSocket.recvfrom(1024)                               #KOD BURADA BAĞLANTI GELMESİNİ BEKLER.
        print('[INFO] {} ADRESS DEVICE CONNECTED'.format(self.address))                 # BAĞLANAN CİHAZIN ADRESİ
        self.connectUDP = True                                                          # GUI EXTENSION FOR LED PIRPIR.
        
    def sendMessage(self,message:str):
        busyState = 0
        while (busyState < 3):
            try:
                if self.connectUDP:
                    self.ServerSocket.settimeout(5.0)
                    self.ServerSocket.sendto(message.encode('utf-8'),self.address)
                    msj,_ = self.ServerSocket.recvfrom(1024)                                # CEVAP DÖNENE KADAR BURADA TAKILACAK.
                    self.ServerSocket.settimeout(None)
                    if msj.decode('utf-8') != (message + str('e')):
                        self.ServerSocket.sendto(message.encode('utf-8'),self.address)
                        self.sendCorrect = False
                        print('[INFO] SEND MESSAGE :',self.sendCorrect)
                    else:
                        self.sendCorrect = True
                        print('[INFO] SEND MESSAGE :',self.sendCorrect)
                        break
            except socket.timeout as error:
                print('RUN SETTİMEOUT')
                continue
            except ConnectionResetError:
                self.ServerSocket.close()
                self.binding()
            except Exception as error:
                print(str(error))
                logFolder = open('COM_UDP_LOG.txt','a+')
                logFolder.write(self.LOGO_NAME+"\n")
                print('[INFO]!!! COMMUNICATION ERROR :',error)
                if str(error) !=  open('COM_UDP_LOG.txt','r').readlines()[-1][:-1]:   # DOSYA ZATEN AÇIK BİR DAHA OKUMAK İÇİN AÇMAYA GEREK YOK.DÜZELT.
                    logFolder.write(str(error)+'\n')
                    logFolder.close() 
            finally:
                busyState +=1 
                 
if __name__ == "__main__":
    UDP = UDPserver()
    while True:
        message = str(12)
        if UDP.connectUDP: 
            UDP.sendMessage(message)
      
            
        
    
