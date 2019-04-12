import socket


def Main():
    HOST = '127.0.0.1'
    PORT = 5080

    s= socket.socket()
    s.connect((HOST, PORT))

    message = input(" -> ")
    while message != 'q':
        s.send(b'message')
        data = s.recv(1024)
        print("Received from Server: " + str(data))
        message = input(" -> ")
        s.close()


if __name__ == '__main__':
    Main()
