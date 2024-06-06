from redis import Redis
client = Redis(host='localhost', port=6379, db=0)
result = client.zrank('my_sorted_set', 'element', withscore=False)
