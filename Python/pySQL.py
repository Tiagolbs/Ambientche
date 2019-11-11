import socket
import _thread
import time
import psycopg2
from datetime import datetime

HOST = ''              # Endereco IP do Servidor
PORT = 5001            # Porta que o Servidor esta

conSql = psycopg2.connect(user = "postgres",password = "password",host = "localhost",port = "5433",database = "LogTest")

cur = conSql.cursor()

def conectado(con, cliente):
    print ('Conectado por', cliente)

    while True:
        msg = con.recv(1024)
        if int(msg) >= 2 and int(msg) <= 8:
            sql = "INSERT INTO LogTest1 (dt_string, comodo) VALUES (%s, %s)"
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            val = (dt_string, int(msg))
            cur.execute(sql, val)
            conSql.commit()

    con.close()
    _thread.exit()

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

orig = (HOST, PORT)

tcp.bind(orig)
tcp.listen(1)

while True:
    con, cliente = tcp.accept()
    _thread.start_new_thread(conectado, tuple([con, cliente]))

tcp.close()