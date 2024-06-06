import tornado.options
tornado.options.define('hello', None, type=str, help='Name of the user', metavar=None, multiple=False, group=None, callback=None)
