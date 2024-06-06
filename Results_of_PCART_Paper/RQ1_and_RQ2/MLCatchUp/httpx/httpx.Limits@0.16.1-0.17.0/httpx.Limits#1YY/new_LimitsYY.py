import httpx
max_connections = 10
max_keepalive = 5
limits = httpx.Limits(keepalive_expiry=5.0)
