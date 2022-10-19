#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from http import server
from http.server import SimpleHTTPRequestHandler
import socket
import ssl
import sys


if sys.argv[1:]:
        port = int(sys.argv[1])
else :
        port = 8000

server_address = ("127.0.0.1", port)

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
#context.load_cert_chain("xxx.pem","xxx.key")#自己新增

httpd = server.HTTPServer(server_address,SimpleHTTPRequestHandler)
httpd.socket = context.wrap_socket(httpd.socket, server_side = True)
httpd.serve_forever()

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mylinebot.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
