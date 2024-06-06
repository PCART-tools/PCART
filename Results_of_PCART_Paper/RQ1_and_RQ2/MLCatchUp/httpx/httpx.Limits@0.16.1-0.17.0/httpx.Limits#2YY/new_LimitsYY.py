import httpx
max_connections = 10
max_keepalive = 5
limits = httpx.Limits(max_connections=max_connections, keepalive_expiry=5.0)
