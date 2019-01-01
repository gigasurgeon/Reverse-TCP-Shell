# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 02:12:15 2018

@author: CAPTAIN
"""

import socket

def create_socket():
    global HOST,PORT,s
    HOST=''
    PORT=10009
    
    try:
        s=socket.socket()
        print("Socket Created")
    
    except:
        print("Error while creating socket.....\n "+str(socket.error))
        

def bind_socket():
    global HOST, PORT, s
    
    try:
        s.bind((HOST, PORT))
        print("Socket Bound")
    
    except:
        print("Error while binding socket......\n"+str(socket.error))
        

def listen_socket():
    global HOST, PORT, s
    
    try:
        s.listen(5)
        print("Listening for connections")
        
    except:
        print("Error while listening socket.....\n"+str(socket.error))
    
    
def accept_socket():
    
    global HOST, PORT, s, conn
    
    try:
        conn, address = s.accept()
        print("Connection Established:" + str(address[0])+str(address[1]),sep="  ")
        send_commands()
        
    except:
        print("Error while accepting connection......\n"+str(socket.error))
        
        
        
def send_commands():
    
    global conn
    
    while True:
        command= input("command: ")
        
        if command=='quit':
            print("Quitting")
            close_socket()
            
        elif len(command)>0:
            conn.send(str.encode(command))
            resp= conn.recv(5000000)
            resp=resp.decode("utf-8")
            print(resp)
        
    
          

def close_socket():
    global s, conn
    
    conn.close()
    s.close()
    
    print("Connection Terminated\n")
    sys.exit()

        




create_socket()
bind_socket()
listen_socket()
accept_socket()
close_socket()