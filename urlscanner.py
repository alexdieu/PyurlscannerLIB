import socket

def urlscan(MYURL):
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((f'{MYURL}', 80))
    cmd = f'GET http://{MYURL} HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(),end='')

    mysock.close()