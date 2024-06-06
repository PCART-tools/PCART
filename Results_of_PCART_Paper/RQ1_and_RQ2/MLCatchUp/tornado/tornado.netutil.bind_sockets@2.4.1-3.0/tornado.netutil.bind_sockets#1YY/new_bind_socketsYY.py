import tornado.netutil
import socket
sockets = tornado.netutil.bind_sockets(8888, flags=None)
