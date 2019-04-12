import socket


def Main():
    HOST = '127.0.0.1'
    PORT = 5080

    s = socket.socket()
    s.bind((HOST, PORT))
    s.listen(1) # listen for one connection at a time.
    conn, addr = s.accept()
    print("Connection from:" + str(addr))
    while True:
        data = conn.recv(1024) # buffer of 1024b.
        if not data:
            break
        print("From Connected user: " + str(data))
        data = str(data).upper()
        print("Sending: " + str(data))
        conn.send(data)
        conn.close()


if __name__ == '__main__':
    Main()




