# -*- coding: utf-8 -*-
"""
Created on Fri May 12 12:47:56 2017

@author: v-bensc
taken from https://forum.tek.com/viewtopic.php?t=137002
"""

import socket
import time

class Socket_Instrument(object):
    ''' socket replacement for visa.instrument class'''
    def __init__(self, IPaddress, PortNumber = 4000):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((IPaddress, PortNumber))
        self.s.setblocking(False)

    def write(self, cmd):
        self.s.send(cmd + '\n')

    def ask(self, cmd, buffer = 2048, timeout = 5):
        self.s.send(cmd + '\n')
        response = ''
        while True:
            char = ""
            try:
                char = self.s.recv(1)
            except:
                time.sleep(0.001)
                if response.rstrip() != "":
                    break
            if char:
                response += char
        return response.rstrip()

    def query(self, cmd, buffer = 2048, timeout = 5):
        self.s.send(cmd + '\n')
        response = ''
        while True:
            char = ""
            try:
                char = self.s.recv(1)
            except:
                time.sleep(0.001)
                if response.rstrip() != "":
                    break
            if char:
                response += char
        return response.rstrip()

    def read(self):
        response = ''
        while True:
            char = ""
            try:
                char = self.s.recv(1)
            except:
                time.sleep(0.001)
                if response.rstrip() != "":
                    break
            if char:
                response += char
        return response.rstrip()

    def close(self):
        self.s.close()
        


