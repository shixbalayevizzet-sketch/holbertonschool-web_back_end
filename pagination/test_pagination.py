#!/usr/bin/env python3
# Əgər faylınızın adı 1-simple_pagination.py-dırsa:
from 1-simple_pagination import Server
server = Server()
# 1-ci səhifə, 5 sətir istəyirik
print(server.get_page(1, 5))
