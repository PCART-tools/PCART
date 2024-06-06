import tornado.iostream
import socket
address = ('example.com', 80)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
stream = tornado.iostream.IOStream(sock)
stream.connect(address=address, server_hostname=None)
