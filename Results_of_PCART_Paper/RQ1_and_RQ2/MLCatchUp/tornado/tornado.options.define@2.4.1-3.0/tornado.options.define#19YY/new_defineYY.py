import tornado.options
tornado.options.define('hello', default=None, type=str, help='Name of the user', metavar=None, callback=None)
