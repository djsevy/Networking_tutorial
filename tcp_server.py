import logging
import socket
logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s',datefmt='%H:%M:%S', level=logging.DEBUG)

def server(ip,port):
    s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    address = (ip,port)

    logging.info(f'Bind: {ip}: {port}')
    s.bind(address)

    logging.info('Listening')
    s.listen(1)

    con, addr = s.accept()
    logging.info(f'Connected: {addr}')

    while True:
        data = con.recv(1024)
        if len(data) == 0:
            logging.info('Exiting')
            con.close()
            break
        logging.info(f'Data: {data}')

    logging.info('Closing the server')
    s.close()

def main():
    server("localhost",2607)

if __name__ == "__main__":
    main()