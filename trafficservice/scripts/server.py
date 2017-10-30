import django
django.setup()
import socket
import requests
from threading import Thread
from SocketServer import ThreadingMixIn
from nt_db.nt_db_app.models import Junction, Junction_data

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
                while True: 
                    part = self.sock.recv(BUFFER_SIZE)
                    file_data += part
                    if len(file_data) >=133:
                        break
                print file_data
                file_data = file_data.strip()
                file_list = file_data.split('&')
                if file_data != '':
                    if file_data.startswith("NUC") and file_data.endswith("CUN"):
                        year = file_list[6] + file_list[7]
                        city_name = file_list[38] + file_list[39] + file_list[40] + file_list[41] + file_list[42]
                        junction_name = file_list[33] + file_list[34] + file_list[35] + file_list[36] + file_list[37]
                        Junction_data.objects.create(junction=Junction.objects.get(junction_name=junction_name),
                            hour=int(file_list[1]), minute=int(file_list[2]), second=int(file_list[3]), day=int(file_list[4]),
                            month=int(file_list[5]), year=int(year), phase_no=int(file_list[10]), status=str(file_list[11]),
                            mode=str(file_list[8]), normal_time=int(file_list[17]), step_elased_time=int(file_list[19]),
                            cycle_elased_time1=str(file_list[20]), cycle_elased_time2=str(file_list[21]),
                            working_on=str(file_list[22]), total_cycle_time1=str(file_list[23]), total_cycle_time2=str(file_list[24]),
                            phase1=str(file_list[25]), phase2=str(file_list[26]), phase3=str(file_list[27]), phase4=str(file_list[28]),
                            phase5=str(file_list[29]), phase6=str(file_list[30]), phase7=str(file_list[31]), phase8=str(file_list[32]))
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
