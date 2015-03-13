import os,re,threading
from socket import*
import socket
from commands import*
def scanLocPort():
    print 'hello world!'
    localIP = socket.gethostbyname(socket.gethostname())
    ipList = socket.gethostbyname_ex(socket.gethostname())
    print "local ip:%s" %localIP
    print "\n"
    addlist = ipList[2]
    for j in addlist:
        print "addlist:%s" %j
    for i in ipList:
        print "extern ip:%s" %i
    #for ii in range(100,200):    
        #mySocket = socket.socket(AF_INET, SOCK_STREAM)
        #result = mySocket.connect_ex(('127.0.0.1', ii))        
        #if(result == 0):
        #print 'port %d result %s:open' %(ii,result)
        #mySocket.close()
   # targetIP = gethostbyname()
    command = 'netstat -a -n'
    str_com = os.system(command)
    print str_com
    pass
def scanWanPort():
    pass
scanLocPort()
