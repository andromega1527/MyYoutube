# -*- coding: utf-8 -*-
import os
# import socket

class Server:
    def __init__(self):
        self._host = '192.168.0.100'
        self._port = 8000
        self._username = 'andromega'
        self._password = 'mario1527'
        self._direc = './youtube/static/videos/'

    def connect(self, user_id):
        sla = os.system('sudo mount -t cifs //{}/myoutube/{}/videos {} -o username={},password={},dir_mode=0777,file_mode=0777'.format(self._host, user_id, self._direc, self._username, self._password))
        print('\n\nConexão bem sucedida\n\n') if sla == 0 else print('\n\nNão foi possivel se conectar ao servidor\n\n')

    def close_connection(self):
        sla = os.system('sudo umount {}'.format(self._direc))
        print('\n\nConexão fechada\n\n') if sla == 0 else print('\n\nNão foi possivel fechar a conexão\n\n')

    def restart_connection(self, user_id):
        self.close_connection()
        self.connect(user_id)

    def send_file(self, video_code, user_id, extension, file):
        filename = video_code + extension
        file.save(os.path.join(self._direc, filename))
        self.restart_connection(user_id)

    def delete_file(self, link_video):
        remove_video = os.system('rm {}'.format(link_video))
        print('\n\nArquivo removido com sucesso!!\n\n') if remove_video == 0 else print('\n\nErro na remoção do arquivo\n\n')