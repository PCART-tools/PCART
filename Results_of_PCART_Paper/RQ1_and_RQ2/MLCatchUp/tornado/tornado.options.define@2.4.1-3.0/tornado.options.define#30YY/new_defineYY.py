import tornado.options
tornado.options.define('hello', None, str, 'Name of the user', None, multiple=False, group=None, callback=None)
