import socket
from threading import Thread
from SocketServer import ThreadingMixIn

TCP_IP = socket.gethostname()
TCP_PORT = 2020
BUFFER_SIZE = 1024

class ClientThread(Thread):

    def __init__(self,ip,port,sock):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.sock = sock
        print " New thread started for "+ip+":"+str(port)

    def run(self):
        
        while True:
            file_data = ''
            try:
                data1 = self.sock.recv(1024)
                file_data = file_data + str(data1)
                data2 = self.sock.recv(1024)
                file_data = file_data + str(data2)
                file_data = file_data.strip()
                file_list = file_data.split('&')
                print file_list
                if file_data != '':
                    if file_data.startswith("NUC") and file_data.endswith("CUN"):
                        print "KK file"
                    else:
                        print "wrong file"
                else:
                    print "No data"
            except:
                continue

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind((TCP_IP, TCP_PORT))
threads = []

while True:
    tcpsock.listen(5)
    print "Waiting for incoming connections..."
    (conn, (ip,port)) = tcpsock.accept()
    print 'Got connection from ', (ip,port)
    newthread = ClientThread(ip,port,conn)
    newthread.start()
    threads.append(newthread)

for t in threads:
    t.join()