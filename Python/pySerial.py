import time
import serial
 
# Iniciando conexao serial
comport = serial.Serial('COM3', 9600)
 
time.sleep(1.8) 
javaParam = '2' #Parametro recebido do Java, ainda não implementado
light = str(chr(javaParam+48))
comport.write(str.encode(light))
comport.write(str.encode('\n'))
	
# Fechando conexao serial
comport.close()