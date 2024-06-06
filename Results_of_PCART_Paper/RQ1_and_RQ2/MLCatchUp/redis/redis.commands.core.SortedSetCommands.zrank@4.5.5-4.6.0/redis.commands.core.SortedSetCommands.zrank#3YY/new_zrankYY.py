from redis import Redis
client = Redis(host='localhost', port=6379, db=0)
result = client.zrank(name='my_sorted_set', value='element', withscore=False)
