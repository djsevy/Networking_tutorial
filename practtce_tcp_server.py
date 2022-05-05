import logging


import logging
import select
import socket
import multiprocessing

logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s',datefmt='%H:%M:%S', level=logging.DEBUG)


def chatserver(ip, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logging.info(f'Binding to {ip}: {port}')
    server.bind((ip,port))
    server.setblocking(False)
    server.listen(100)
    logging.info(f'listening on {ip}: {port}')

    readers = [server]
    while True:
        readable, writable, errored = select.select(readers, [], [], 0.5)

        for s in readable:
            

            try:
                if s == server:
                    client, address = s.accept()
                    client.setblocking(False)
                    readers.append(client)
                    logging.info(f'connection: {address}')
                    
                else:
                    data = s.recv(1024)
                    if data:
                        logging.info(f'Echo {data}')
                        s.send(data)
                    else:
                        logging.info(f'Remove {s}')
            except Exception as ex:
                logging.warning(ex.args)
            finally:
                pass

def main():
    svr = multiprocessing.Process(target=chatserver, args=['localhost', 2045], daemon=True, name='server')
    
    while True:
        command = input('\n\nEnter a command (start, stop)\n\n')
        if command == 'start':
            logging.info('\nstarting the server')
            svr.start()
        if command == 'stop':
            logging.info('Stopping')
            svr.terminate
            svr.join()
            svr.close()
            logging.info('Server stopped')
            break
    

if __name__ == "__main__":
    main()