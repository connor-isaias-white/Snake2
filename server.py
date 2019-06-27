import socket
from _thread import *
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = ''
port = 5555

server_ip = socket.gethostbyname(server)

try:
    s.bind((server, port))

except socket.error as e:
    print(str(e))

s.listen(2)
print("Waiting for a connection")

currentId = "0"
pos = {"0": "nocon", "1": "nocon"}


def threaded_client(conn):
    global currentId, pos
    conn.send(str.encode(currentId))
    currentId = "1"
    reply = ''
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode('utf-8')
            if not data:
                conn.send(str.encode("Goodbye"))
                break
            else:
                print("Recieved: " + reply)
                arr = reply.split(":")
                id = arr[0]
                pos[id] = reply.split(":")[1]
                if id == '0':
                    nid = "1"
                if id == '1':
                    nid = '0'
                if reply.split(":")[1] != "waiting":
                    reply = pos[nid]

                else:
                    print(pos)
                    if pos['0'] == "waiting" and pos['1'] == "waiting":
                        pos[id] = "ready"
                        reply = 'True'
                    elif pos[nid] == 'ready':
                        pos['0'] = "10,0"
                        pos['1'] = "-10,0"
                        reply = 'True'
                    else:
                        reply = 'False'
                print("Sending: " + reply)
            conn.sendall(str.encode(reply))
        except Exception as e:
            print(e)
            break

    print("Connection Closed")
    conn.close()


while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (conn,))
