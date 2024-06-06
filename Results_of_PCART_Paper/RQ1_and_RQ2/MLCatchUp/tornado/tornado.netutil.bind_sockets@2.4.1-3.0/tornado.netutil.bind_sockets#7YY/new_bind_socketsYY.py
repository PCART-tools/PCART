import tornado.netutil
import socket
sockets = tornado.netutil.bind_sockets(8888, '0.0.0.0', family=socket.AF_UNSPEC, flags=None)
