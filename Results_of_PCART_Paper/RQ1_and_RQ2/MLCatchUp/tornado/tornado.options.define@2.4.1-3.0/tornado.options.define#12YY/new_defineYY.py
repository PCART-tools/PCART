import tornado.options
tornado.options.define('hello', None, type=str, help='Name of the user', callback=None)
