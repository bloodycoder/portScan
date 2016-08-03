import sys 
import socket 
import pdb
from threading import Thread

class Portscan:
	def __init__(self,host,portRange):
		self.opened_ports = []
		self.start_port = portRange[0]
		self.end_port = portRange[1]
		self.ip_toget = socket.gethostbyname(host)
		self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.sock.settimeout(10)
	def start(self):
		threadPool = []
		for port in range(self.start_port,self.end_port+1):
			new_thread = Thread(target = self.scanone,args =(port,))
			threadPool.append(new_thread)
		for thread in threadPool:
			thread.start()
		for thread in threadPool:
			thread.join()
		for port in self.opened_ports:
			print port
		return 
	def scanone(self,port):
		result = self.sock.connect_ex((self.ip_toget,port))
		if(result == 0):
			self.opened_ports.append(port)

if __name__ == '__main__':
	host = sys.argv[1]
	portstrs = sys.argv[2]
	portstrs = portstrs.split('-')
	start_port = int(portstrs[0])
	end_port = int(portstrs[1])
	portscan = Portscan(host,(start_port,end_port))
	portscan.start()