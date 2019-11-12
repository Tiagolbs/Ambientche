import socket
import _thread
import time
import psycopg2
from datetime import datetime
from getpass import getpass

HOST = '192.168.9.19'              # Endereco IP do Servidor
PORT = 5001            # Porta que o Servidor esta

conSql = psycopg2.connect(user = input('User postgres: '),password = getpass('Senha: '),host = input('Host: '),port = input('Porta: '),database = input('Database: '))

cur = conSql.cursor()

print('Conectado com sucesso')

StatusLuz = [False, False, False, False, False, False, False]

def conectado(con, cliente):
    print ('Conectado por', cliente)

    while True:
        msg = con.recv(1024)
        if int(msg) >= 2 and int(msg) <= 8:
            sql = "INSERT INTO LogTest1 (dt_string, comodo, status) VALUES (%s, %s, %s)"
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            StatusLuz[int(msg)-2] = not StatusLuz[int(msg)-2]
            val = (dt_string, int(msg), StatusLuz[int(msg)-2])
            cur.execute(sql, val)
            conSql.commit()
            print('Inserido:', dt_string, int(msg), StatusLuz[int(msg)-2])

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
