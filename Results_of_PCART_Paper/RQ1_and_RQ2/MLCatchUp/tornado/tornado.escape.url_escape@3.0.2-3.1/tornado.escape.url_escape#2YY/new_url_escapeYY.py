import tornado.escape
value_to_escape = 'hello world'
escaped_value = tornado.escape.url_escape(value=value_to_escape, plus=True)
print(escaped_value)
