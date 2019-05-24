import socket
import csv

# Create a socket(allows two computers to connect)
def socket_create():
    try:
        global host
        global port
        global s
        host = ''
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print('Socket Creation Error: '+ str(msg))

# Bind socket to port and wait for connection from client
def socket_bind():
    try:
        global host
        global port
        global s

        s.bind((host,port))
        s.listen(5)
    except socket.error as msg:
        print('Socket Binding error: '+str(msg)+ '\nRetrying...')


# Accept multiple clients and save to list
def accept_connections():
    conn, address = s.accept()
    conn.setblocking(1)
    return conn  

def send_data(conn,data):
        conn.send(bytes(data, 'UTF-8'))
        print('Data sent')
    
