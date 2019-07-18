#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import os
import logging
import logging.config

class Device:
	def __init__(self, ip):
		self.ip = ip
		self.total_ping_count = 0
		self.total_ping_failed_count = 0



def main():
	logging.config.fileConfig("logger.conf")
	logger = logging.getLogger("example01")

	cur_asctime = time.asctime( time.localtime(time.time()))
	logger.debug('begin ping process')

	device_list = [Device("192.168.20.102"),
				   Device("192.168.20.103"),
				   Device("192.168.20.105"),
				   Device("192.168.20.106")]
	try:
		while True:
			for device in device_list:
				logger.debug('begin ping:' + device.ip)
				device.total_ping_count = device.total_ping_count + 1
				ping_result = os.system('ping ' + device.ip + ' -c 1 -W 2 > /dev/null')
				if ping_result != 0:
					cur_asctime = time.asctime( time.localtime(time.time()))
					logger.warning('ping:' + device.ip + ' failed')
					device.total_ping_failed_count = total_ping_failed_count + 1
			time.sleep(5)
	except KeyboardInterrupt as e:
		for device in device_list:
			print('ping:' + device.ip + ' ' + str(device.total_ping_count) + ' times, ' + 'failed ' + str(device.total_ping_failed_count) + ' times')
			#logger.info('ping:' + device.ip + ' ' + str(device.total_ping_count) + ' times, ' + 'failed ' + str(device.total_ping_failed_count) + ' times')
	else:
		pass
	finally:
		pass

if __name__ == '__main__':
	main()		