import tornado.escape
value_to_unescape = 'hello world'
unescaped_value = tornado.escape.url_unescape(value_to_unescape, plus=True)
print(unescaped_value)
