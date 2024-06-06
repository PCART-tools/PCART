import aiohttp
import asyncio

def main(loop):
    connector = aiohttp.TCPConnector()
    cookies = {'test': 'cookie_value'}
    headers = {'Content-Type': 'application/json'}
    auth = aiohttp.BasicAuth('username', 'password')
    session = aiohttp.ClientSession(request_class=aiohttp.client_reqrep.ClientRequest, ws_response_class=aiohttp.websocket_client.ClientWebSocketResponse, response_class=aiohttp.client_reqrep.ClientResponse, loop=None, connector=connector, cookies=cookies, headers=headers, auth=auth, skip_auto_headers=None)
    response = loop.run_until_complete(session.get('http://httpbin.org/headers'))
    data = loop.run_until_complete(response.text())
    print(data)
    session.close()
loop = asyncio.get_event_loop()
main(loop)
