# pylint: disable-all
# pylint: skip-file
"""
simple FTP Handler
"""
import ftplib
import os

import urllib3


class FTPHandler:
    """
    simple FTP Handler
    """

    def __int__(self, server: str, port: str, protocol: str, user: str, pwd: str) -> None:
        """
        Konstruktor
        @param server:
        @param port:
        @param protocol:
        @param user:
        @param pwd:
        @return:
        """
        self.server = server
        self.protocoll = protocol
        self.user = user
        self.pwd = pwd
        self.port = port

    def download(self, file: str) -> None:
        """
        Download an File from a FTP Server
        @param file:
        @return:
        """
        server = ftplib.FTP()
        server.connect(self.server, int(self.port))
        server.login(self.user, self.pwd)
        server.retrbinary("RETR " + file, open(file, 'wb').write)
