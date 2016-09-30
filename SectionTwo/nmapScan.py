import optparse
from socket import *
from threading import *
from  nmap import *


screanLock = Semaphore(value = 1)

def nmapScan(tgtHost, tgtPort):
    nmScan = PortScanner()
    nmScan.scan(tgtHost, tgtPort)
    state = nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
    screanLock.acquire()
    print tgtHost + ' tcp:' + tgtPort + ' ' + state
    screanLock.release()

def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print '[-] Can not resolve %s : unkonwn host' % tgtHost
        return
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
#        connScan(tgtIP, int(tgtPort))#int
        t = Thread(target=nmapScan, args=(tgtIP, str(tgtPort)))
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

