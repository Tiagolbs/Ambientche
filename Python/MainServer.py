import asyncio
import websockets
import socket

async def echo(websocket, path):
    async for message in websocket:
        await websocket.send(message) #Recebe a mensagem por WebSocket
        HostDest1 = '192.168.9.21' #pySQL
        PortDest1 = 5001 #pySQL
        HostDest2 = '192.168.9.17' #pySQL
        PortDest2 = 5001 #pySQL
        HostDest3 = '192.168.9.9' #pySQL
        PortDest3 = 5001 #pySQL
        HostDestSerial = '192.168.9.19' #pySerial
        PortDestSerial = 5002 #pySerial

        #Dados para enviar a mensagem ao pySQL
        tcpDest1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        Dest1 = (HostDest1, PortDest1) 
        tcpDest1.connect(Dest1)
        tcpDest1.send(message.encode()) 

        tcpDest2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        Dest2 = (HostDest2, PortDest2) 
        tcpDest2.connect(Dest2)
        tcpDest2.send(message.encode()) 

        tcpDest3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        Dest3 = (HostDest3, PortDest3) 
        tcpDest3.connect(Dest3)
        tcpDest3.send(message.encode()) 
        
        #Dados para enviar a mensagem ao pySerial
        DestSerial = (HostDestSerial, PortDestSerial)
        tcpDestSerial = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpDestSerial.connect(DestSerial)
        tcpDestSerial.send(message.encode())   
     
start_server = websockets.serve(echo, "192.168.9.20", 5000) #Endereço para iniciar server WebSocket

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
