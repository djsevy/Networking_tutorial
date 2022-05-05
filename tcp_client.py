import logging 
import socket

logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s',datefmt='%H:%M:%S', level=logging.DEBUG)

def download(server,port):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # define a TCP socket using a IPv4 that is bidirectional in it's communication.
    address = (server,port)
    logging.info(f'Connecting to our {server}:{port}')

    s.connect(address)
    logging.info('Connected')

    logging .info('Send')
    s.send(b'Hello\r\n')

    logging.info('Recv')
    data = s.recv(1024)

    logging.info('Closing')
    s.close()

    logging.info(f'Data: {data}')


def main():
    download("voidrealms.com",7346)

if __name__ == "__main__":
    main()