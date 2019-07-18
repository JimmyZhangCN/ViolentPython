#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import os
import sys

def retBanner(ip, port):
	try:
		socket.setdefaulttimeout(1)
		s = socket.socket()
		s.connect((ip, port))
		banner = s.recv(1024) 
		return banner
	except Exception as e:
		print(e)
		return

def checkVulns(banner, filename):
	f =  open(filename, 'r')
	for line in f.readlines():
		if line.strip('\n') in banner:
			print(line  + 'is vulnerable.')
	return

def main():
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		if not os.path.isfile(filename):
			print('[-]' + filename + 'does not exist')
			exit(0)
		if not os.access(filename, os.R_OK):
			print('[-]' + filename + 'access denied')
			exit(0)
	else:
		print('[-] Usage: ' + str(sys.argv[0]) + 'Vuln filename')
		exit(0)

	f = open('search_result.txt', 'w+')
	portList = [21, 22, 25, 80, 110]
	for x in range(57, 255):
		ip = '171.221.207.' + str(x)
		for port in portList:	
			banner = retBanner(ip, port)
			if banner:
				result = '[+]' + ip + ':' + str(port) + ' ' + str(banner).strip('\r\n')
				f.write(result)
				f.flush()
				#result.encode('utf-8')   #编码为UTF-8
				checkVulns(str(banner), filename)

if __name__ == '__main__':
	main()		