import socket
import _thread
import time
import serial

HOST = 'localhost'     # Endereco IP do Servidor
PORT = 5002            # Porta que o Servidor esta


def conectado(con, cliente):
    print('Conectado por', cliente)

    comport = serial.Serial('COM3', 9600)	#Inicia a conexao com o arduino
    
    while True:
        msg = con.recv(1024)  # Recebe a mensagem
        if int(msg) >= 2 and int(msg) <= 8:       
            time.sleep(1.8)

            luz = str(chr(int(msg)+48))
            time.sleep(0.1)
            comport.write(str.encode(luz))	#Liga a luz referente ao comodo
            comport.write(str.encode('\n'))

    print ('Finalizando conexao', cliente)
    con.close()		#Finaliza conexao 
    _thread.exit()	#Finaliza Thread

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

orig = (HOST, PORT)

tcp.bind(orig)
tcp.listen(1)

while True:
    con, cliente = tcp.accept()
    _thread.start_new_thread(conectado, tuple([con, cliente])) #Inicia a thread com a conexao

tcp.close()