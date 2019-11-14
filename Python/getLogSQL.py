import psycopg2
from getpass import getpass
import websockets
import asyncio

conSql = psycopg2.connect(user = "postgres",password = getpass('Password: '),host = "localhost",port = input('Porta: '),database = "LogTest")
cur = conSql.cursor()

print('Conectado com sucesso')

texto = ""

async def sendToJS():
    uri = "ws://localhost:5101"
    
    async with websockets.connect(uri) as websocket:
        await websocket.send(texto)
        


async def echo(websocket, path):
    async for message in websocket:
        await websocket.send(message) #Recebe a mensagem por WebSocket
        
        print('Recebido: ', message)
        texto = ""
        if str(message) == 'log':
            sql = 'select * from LogStatusLuz'
            cur.execute(sql)
            conSql.commit()
            returnCur = cur.fetchall()

            for rec in returnCur:
                texto += str(rec) + '\n'

            asyncio.get_event_loop().run_until_complete(sendToJS())
            

start_server = websockets.serve(echo, "localhost", 5100) #Endereço para iniciar server WebSocket

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()



