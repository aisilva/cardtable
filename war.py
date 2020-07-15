#!/usr/bin/env python3

# https://realpython.com/python-sockets/
import sys
import socket

"""
black_spade = "\u2664"
red_heart = "\u2665"
red_diamond = "\u2666"
black_club = "\u2667"
"""


spade = "\u2660"
heart = "\u2665"
diamond = "\u2666"
club = "\u2663"


def main():
    
    print(spade,heart,diamond,club)
    PORT1 = 6969 #port that client connects to and host listens to
    PORT2 = 7000 #these just have to be >1023 to be 'non-privileged'

    DATA_AMT = 1024
    assert len(sys.argv) >= 2
    
    if sys.argv[1] == 'host':
        #python3 war.py host
        assert len(sys.argv) == 2
        HOST = "127.0.0.1"
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT1))
            #s.bind((HOST, PORT2))
            s.listen()
            s.setblocking(False)
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                while True:
                    data = conn.recv(DATA_AMT)
                    if not data:
                        break
                    print('Host received', data)
                    conn.sendall(data)
    
    elif sys.argv[1] == 'client1' or sys.argv[1] == 'client2':
        #python3 war.py client 127.0.0.1
        assert len(sys.argv) == 3
        HOST = sys.argv[2]
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if sys.argv[1] == 'client1':
                s.connect((HOST, PORT1))
            elif sys.argv[1] == 'client2':
                s.connect((HOST, PORT2))


            while True:
                to_send = bytes(input(">"), 'utf-8')
                if to_send == b'QUIT':
                    break
                #s.sendall(b'Hello, world')
                s.sendall(to_send)
             
                data = s.recv(DATA_AMT)

                print('Host received', repr(data))
    
    
        
    else:
        print('first arg must be "host", "client1", or "client2"')
        #print('first arg but be "host" or "client"')
                        



if __name__ == "__main__":
    main()





