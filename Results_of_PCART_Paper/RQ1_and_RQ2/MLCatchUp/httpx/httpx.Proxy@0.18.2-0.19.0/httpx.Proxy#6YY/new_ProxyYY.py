import httpx
proxy_url = 'http://localhost:8080'
proxy_headers = {'Custom-Header': 'Value'}
proxy = httpx.Proxy(headers=proxy_headers, url=proxy_url)
