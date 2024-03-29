import threading
import socket


host = '127.0.0.1'
port = 2567

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen

clients = []
name = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            nicknames = name[index]
            broadcast(f'{nicknames} left the chat'.encode('ascii'))
            nicknames.remove(name)
            break

def main():
    while True:
        client, address = server.accept()
        print(f'connected with {str(address)} ')

        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nickname.append(nickname)
        clients.append(client)

        print(f'Nickname of client is {nickname}')
        broadcast(f'{nickname} joined the chat'.encode('ascii'))
        client.send('connected to the server'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

if __name__ == "__main__":
    main()