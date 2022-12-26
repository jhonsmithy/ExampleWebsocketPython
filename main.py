# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import websockets
import asyncio
import websocket



async def produce(message:str, host: str, port: int)->None:
    async with websockets.connect(f"ws://{host}:{port}") as ws:
        await ws.send(message)
        await ws.recv()

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    websocket.enableTrace(True)
    ws = websocket.WebSocket()

    ws.connect("ws://192.168.230.103:81/")
    data=ws.recv()
    print(data)
    #ws.send('/connection|')
    #ws.send('/oiranecs| if cron35 then {vout31="cron";if vbtn45==1 then vout94="button on";}')
    ws.send('/sgnittes|')
    while True:
        data = ws.recv()
        print(data)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
