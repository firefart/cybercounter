#!/usr/bin/env python3

import asyncio
import websockets
import time
from aioconsole import ainput

counter = 0

async def input_loop():
  global counter
  while True:
    _ = await ainput("Press enter to cyber >>> ")
    counter += 1

async def count(websocket, path):
  print("New Client Connected")
  global counter
  # send inital value on new connection
  await websocket.send(str(counter))
  last_count = counter
  while True:
    if last_count != counter:
      await websocket.send(str(counter))
      last_count = counter
    await asyncio.sleep(0.1)

loop = asyncio.get_event_loop()
server = websockets.serve(count, "127.0.0.1", 8765)
loop.run_until_complete(asyncio.gather(server, input_loop()))
loop.run_forever()
