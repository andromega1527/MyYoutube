import os

class Server:
    def __init__(self):
        self._username = 'andromega'
        self._password = 'mario1527'
        self._direc = './youtube/static/videos/'
        self._user = 'user'

    def connect(self):
        # umount pasta
        # mount -t //ip_do_servidor_samba/nome_do_compartilhamento /mnt/ -o username=nome_do_usuario,password=senha_do_usuario
        sla = os.system('sudo mount -t cifs //192.168.0.100/myoutube/videos {} -o username={},password={}'.format(self._direc, self._username, self._password))
        print('conexão bem sucedida') if sla == 0 else print('não foi possivel se conectar ao servidor')

    def closeConnection(self):
        sla = os.system('sudo umount {}'.format(self._direc))
        print('conexão fechada') if sla == 0 else print('não foi possivel fechar a conexão')

# import socket
# from paramiko import SSHClient
# import paramiko
# import requests

# class SSH:
#     def __init__(self):
#         self.ssh = SSHClient()
#         self.ssh.load_system_host_keys()
#         self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#         self.ssh.connect(hostname='192.168.0.100', port=22, username='andromega', password='mario1527')
#         # self.ssh._host_keys.load('//home')

#     def exec_cmd(self, cmd):
#         stdin, stdout, stderr = self.ssh.exec_command(cmd)
#         if stderr.channel.recv_exit_status() != 0:
#             print(stderr.read())
#         else:
#             print(stdout.read())

# if __name__ == '__main__':
#     ssh = SSH()
#     ssh.exec_cmd('ls')

# def connection(self):
    #     HOST = '192.168.0.100'
    #     PORT = 8000
    #     tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #     dest = (HOST, PORT)
    #     tcp.connect(dest)

    #     print('Para sair use Ctrl+X\n')
    #     msg = input()
    #     while msg != '\x18':
    #         tcp.send(msg)
    #         msg = input()

    #     tcp.close()