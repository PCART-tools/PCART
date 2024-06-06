import tornado.options
tornado.options.define(name='hello', default=None, type=str, help='Name of the user', metavar=None, callback=None)
