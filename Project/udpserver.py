import socket

# Variáveis

serverIP = "127.0.0.1" # Este IP muda para cada computador
localPort = 8184
bufferSize = 1024
msgFromServer = "Hello from UDP Server"
bytesToSend = str.encode(msgFromServer)

# Criando um Datagram Socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Definindo (bind) com o ip e porta
UDPServerSocket.bind((serverIP,localPort))

# Mensagem mostrando que está ativo
print("UDP Server UP and LISTEN!")

# Esperando por qualquer Datagram para o Servidor
while(True):

    # Recebendo mensagem do Cliente
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]

    # Apresentação da Mensagem
    print("Mensagem do Cliente: {}".format(message))
    print("IP do Cliente: {}".format(address))

    # Enviando resposta ao Cliente
    UDPServerSocket.sendto(bytesToSend,address)