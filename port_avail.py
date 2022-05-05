import logging
import socket

logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s',datefmt='%H:%M:%S', level=logging.DEBUG)

def check_port(ip,port,timeout):
    ret = False
    logging.info(f'checking {ip}: {port}')

    try:
        s= socket.socket(socket.AF_INET,socket.SOCKET_STREAM)
        s.settimeout(timeout)
        con = s.connect_ex(ip,port)
        logging.debug(f'Connection {ip}: {port} = {con}')
        s.close

        if con == 0:
            ret = False
            logging.debugging(f'In use {ip}:{port}')
        else:
            ret = True
            logging.debugging(f'Usable {ip}:{port}')

    except Exception as ex:
        ret = False
        logging.debug(f' Error {ip}: {port} = {ex.msg}')
        pass
    finally:
        logging.debug(f'returning {ip}: {port} = {ret}')
        return ret

def check_range(ip,scope):
    ret = {}
    for p in scope:
        r = check_port(ip,p,1.0)
        ret[p] = r
    return ret


def main():
    p = check_port('localhost',2594,2.0)
    logging.info(f'port 2594 usable: {p}')

    ports = check_range('localhost',range(2300,2350))
    for k,v in ports.items():
        logging.info(f'port:{k} usable {v}')

if __name__ == "__main__":
    main()