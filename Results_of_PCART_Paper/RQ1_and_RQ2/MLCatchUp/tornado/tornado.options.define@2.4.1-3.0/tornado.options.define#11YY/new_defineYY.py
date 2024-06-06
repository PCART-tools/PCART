import tornado.options
tornado.options.define('hello', None, str, help='Name of the user', callback=None)
