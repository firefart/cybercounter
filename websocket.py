#!/usr/bin/env python3

import asyncio
import websockets
import time

counter = 0

async def count(websocket, path):
  global counter
  while True:
    i = input("Press enter for cyber")
    counter += 1
    await websocket.send(str(counter))

start_server = websockets.serve(count, "0.0.0.0", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
