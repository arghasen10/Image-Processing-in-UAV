import os
import socket
import subprocess
import time,csv

class Client():
    def __int__(self):
        self.host='192.168.0.14'
        self.port=9999
        self.s = None

    def socket_create(self):
        try:
            self.s = socket.socket()
            print('Socket Created')
        except socket.error as e:
            print('Socket creation error: '+ str(e))


    def socket_connect(self):
        try:
            self.s.connect(('192.168.0.14',9999))
            print('Socket connected')
        except socket.error as e:
            print('Socket connection error: '+ str(e))
            return

    def create_file(self):
        filename = str(self.s.recv(1024), 'utf-8')
        print('File created:{}'.format(filename))

        header = ['Date','Time', 'PM1', 'PM2_5', 'PM10', 'N02', 'CO2', 'CO', 'Humidity', 'Temperature']
        with open(filename, 'w') as file:
            writer = csv.writer(file)
            writer.writerow(header)

        return filename


    def recv_data(self, filename):
        file = open(filename , 'a', newline='')
        print('file opened')
        writer = csv.writer(file)
        count=0
        while True:
            print('receiving data...')
            data = str(self.s.recv(1024), 'utf-8')
            print(data)
            if not data:
                break
            # write data to a file
            data = data.split(',')
            print(data)
            writer.writerow(data)
            count+=1
            if count>=100:
                response = input('Do you want to continue data collection?(Yes/No):')
                self.s.send(str.encode(response))
        file.close()


def main():
    client=Client()
    client.socket_create()
    while True:
        try:
            client.socket_connect()
        except Exception as e:
            print('Error on socket connections: '+str(e))
        else:
            break

    filename = client.create_file()
    client.recv_data(filename)

    client.s.close()

if __name__=='__main__':
        main()
