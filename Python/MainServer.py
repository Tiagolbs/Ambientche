import socket
import _thread

HOST = 'localhost'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta


def conectado(con, cliente):
    print('Conectado por', cliente)


    while True:
        msg = con.recv(1024)
        HostDest1 = 'localhost' #pySQL
        PortDest1 = 5001 #pySQL
        HostDest2 = 'localhost' #pySerial
        PortDest2 = 5002 #pySerial

        #pySQL
        Dest1 = (HostDest1, PortDest1) 
        tcpDest1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpDest1.connect(Dest1)
        tcpDest1.send(msg) 
        
        #pySerial
        Dest2 = (HostDest2, PortDest2)
        tcpDest2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcpDest2.connect(Dest2)
        tcpDest2.send(msg)   

    print(cliente, msg)

    tcp.close()
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
