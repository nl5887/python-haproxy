# -*- coding: utf-8 -*-

import logging
import socket
import select
import sys
import socket
import string

from time import time
from traceback import format_exc
 
logger = logging.getLogger(__name__)
 
class TimeoutException(Exception): 
	pass 

class HAProxyStats(object):
	""" Used for communicating with HAProxy through its local UNIX socket interface.
	"""
	def __init__(self, socket_name=None):
		self.socket_name = socket_name
 
	def execute(self, command, timeout=200):
		""" Executes a HAProxy command by sending a message to a HAProxy's local
		UNIX socket and waiting up to 'timeout' milliseconds for the response.
		"""
		
		buffer = ""
 
		client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
		client.connect(self.socket_name)

		client.send(command + "\n")

		running = True
		while(running):
			r, w, e = select.select([client,],[],[], timeout)

			if not (r or w or e):
				raise TimeoutException()
	
			for s in r:
				if (s is client):
					buffer = buffer + client.recv(16384)
					running = (len(buffer)==0)
										
		client.close()

		return (buffer.decode('utf-8').split('\n'))

