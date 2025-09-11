import redis
from redis.exceptions import RedisError

def main():
    # Redis connection configuration
    REDIS_HOST = 'localhost'
    REDIS_PORT = 6379
    REDIS_DB = 0

    try:
        # Using context manager for automatic connection handling
        with redis.Redis(
            host=REDIS_HOST,
            port=REDIS_PORT,
            db=REDIS_DB,
            decode_responses=True  # Automatically decode responses to strings
        ) as r:
            try:
                # Test connection
                print(f"PING response: {r.ping()}")

                # String operations
                r.set("weather", "sunny", ex=3600)  # Set with 1 hour expiration
                print(f"Current weather: {r.get('weather')}")

                # Hash operations
                user_id = "user:100"
                r.hset(user_id, mapping={"name": "Alice", "age": "25"})
                print(f"User data: {r.hgetall(user_id)}")

                # List operations
                r.lpush("recent_visitors", "Alice", "Bob", "Charlie")
                print(f"Recent visitors: {r.lrange('recent_visitors', 0, -1)}")

                # Set operations
                r.sadd("unique_visitors", "Alice", "Bob", "Alice", "Dave")
                print(f"Unique visitors: {r.smembers('unique_visitors')}")

                # Sorted Set operations
                r.zadd("player_scores", {"Alice": 100, "Bob": 85, "Charlie": 95})
                print(f"Top players: {r.zrevrange('player_scores', 0, 1, withscores=True)}")

                # Transaction (pipeline)
                with r.pipeline() as pipe:
                    pipe.incr("page_views")
                    pipe.get("weather")
                    pipe.hgetall(user_id)
                    result = pipe.execute()
                    print(f"Transaction results - Page views: {result[0]}, Weather: {result[1]}, User: {result[2]}")

                # Pub/Sub example
                pubsub = r.pubsub()
                pubsub.subscribe("news")
                r.publish("news", "Breaking news: Redis is awesome!")
                message = pubsub.get_message(timeout=1)
                if message:
                    print(f"Received message: {message}")

            except RedisError as e:
                print(f"Redis operation failed: {e}")

    except RedisError as e:
        print(f"Failed to connect to Redis: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
