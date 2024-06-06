import tornado.ioloop
from tornado.tcpserver import TCPServer
import socket
server = TCPServer()
server.bind(0, '', socket.AF_UNSPEC, reuse_port=False)
