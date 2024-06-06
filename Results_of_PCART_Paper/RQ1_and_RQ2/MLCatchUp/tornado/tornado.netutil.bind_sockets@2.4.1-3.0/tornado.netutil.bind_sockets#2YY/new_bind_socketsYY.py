import tornado.netutil
import socket
sockets = tornado.netutil.bind_sockets(port=8888, flags=None)
