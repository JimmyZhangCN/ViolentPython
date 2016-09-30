import optparse
import socket
from socket import *
from threading import *


screanLock = Semaphore(value = 1)
def connScan(tgtHost, tgtPort):
#    print '[s] scaning %s:%d' %(tgtHost, tgtPort)
    try :
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        connSkt.send("ViolentPython\r\n")
        results = connSkt.recv(100)
        screanLock.acquire()
        print '[+] %d/tcp open ' % tgtPort
        print '[+] ' + str(results)
    except:
        screanLock.acquire()
        print '[-] %d/tcp closed'
    finally:
        screanLock.release()
        connSkt.close()

def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print '[-] Can not resolve %s : unkonwn host' % tgtHost
        return
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
#        connScan(tgtIP, int(tgtPort))#int
        t = Thread(target=connScan, args=(tgtIP, int(tgtPort)))
        t.start()    
    return


def main():
#
#    parser = optparse.OptionParser('Usage -H target host -P ports')
#    parser.add_option('-H', dest='tgtHost', type='string', help='Host')
#    parser.add_option('-P', dest='tgtPorts', type='string', help='Ports')
#    (options, args) = parser.parse_args()
#    if (options.tgtHost == None) | (options.tgtPorts == None):
#        print parser.usage
#        exit(-1)
#    else:
#        tgtHost  = options.tgtHost
#        tgtPorts  = str(options.tgtPorts).split(',')
 
    tgtHost = '171.221.207.58'
    tgtPorts= range(1, 60000)   
    portScan(tgtHost, tgtPorts)



if __name__ == "__main__":
    main() 

