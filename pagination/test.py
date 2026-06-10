#!/usr/bin/env python3

Server = __import__('1-simple_pagination').Server

server = Server()

print(server.get_page(1, 10))
print(server.get_page(2, 10))
print(server.get_page(1000, 10))
