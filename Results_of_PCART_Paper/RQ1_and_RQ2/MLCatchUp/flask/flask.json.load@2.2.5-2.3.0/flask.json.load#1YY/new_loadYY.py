import flask
file_path = '/home/zhang/test.json'
with open(file_path, 'r', encoding='utf-8') as text_file:
    flask.json.load(text_file)
