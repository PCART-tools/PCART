import tornado.netutil
import socket
sockets = tornado.netutil.bind_sockets(port=8888, address='0.0.0.0', family=socket.AF_UNSPEC, backlog=128, flags=None)
