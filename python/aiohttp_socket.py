# !/usr/bin/env python
# encoding: utf-8

"""
file: aiohttp_socket.py
time: 2019/7/8 14:57
Author: twy
contact: 19983195362
des: 使用aiohttp的socket服务器，可以与WebSocket对象进行通信
"""

import aiohttp
from aiohttp import web

app = web.Application()


async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    async for msg in ws:
        if msg.type == aiohttp.WSMsgType.TEXT:
            if msg.data == 'close':
                await ws.close()
            else:
                await ws.send_str(f'{msg.data}/answer')
        elif msg.type == aiohttp.WSMsgType.ERROR:
            print(f'ws connection closed with exception {ws.exception()}')
    print('websocket connection closed')
    return ws

app.add_routes([web.get('/', websocket_handler)])
web.run_app(app)


