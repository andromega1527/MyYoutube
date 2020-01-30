import socket
import paramiko

class ServerConection:
    def connection(self):
        HOST = '192.168.0.100'
        PORT = 8000
        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        dest = (HOST, PORT)
        tcp.connect(dest)

        print('Para sair use Ctrl+X\n')
        msg = input()
        while msg != '\x18':
            tcp.send(msg)
            msg = input()

        tcp.close()

    def connectionSSH(self):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname='192.168.0.100', port=22, username='andromega', password='mario1527')

ServerConection().connectionSSH()