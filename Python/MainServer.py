import asyncio
import websockets
import socket

async def echo(websocket, path):
    async for message in websocket:
        await websocket.send(message) #Recebe a mensagem por WebSocket
        HostDest1 = 'localhost' #pySQL
        PortDest1 = 5001 #pySQL
        HostDest2 = 'localhost' #pySerial
        PortDest2 = 5002 #pySerial

        #Dados para enviar a mensagem ao pySQL
        Dest1 = (HostDest1, PortDest1) 
        tcpDest1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpDest1.connect(Dest1)
        tcpDest1.send(message.encode()) 
        
        #Dados para enviar a mensagem ao pySerial
        Dest2 = (HostDest2, PortDest2)
        tcpDest2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpDest2.connect(Dest2)
        tcpDest2.send(message.encode())   
     
start_server = websockets.serve(echo, "localhost", 5000) #Endereço para iniciar server WebSocket

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
