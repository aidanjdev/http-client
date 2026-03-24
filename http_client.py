#!/usr/bin/env python3

import argparse
import socket
from urllib.parse import urlsplit

REQUEST_METHODS = [
    'GET',
    'HEAD',
    'POST',
    'PUT',
    'DELETE',
    'CONNECT',
    'OPTIONS',
    'TRACE'
]

HTTP_VERSION = "HTTP/1.1"
CRLF = "\r\n"

def send_request(request, socket):
    bytes_sent = 0
    encoded_request = request.encode()
    while bytes_sent < len(request):
        sent = socket.send(encoded_request[bytes_sent:])
        if sent == 0:
            raise RuntimeError("Error: Socket connection broken during request.")
        bytes_sent = bytes_sent + sent

def format_request(http_request):
    formatted_request = ''
    for line in http_request:
        formatted_request += line + CRLF
    return formatted_request

def receive_response(socket):
    headers = b''
    while b'\r\n\r\n' not in headers:
        current_line = socket.recv(1024)
        if len(current_line) == 0:
            raise RuntimeError("Error: Socket connection broken during response.")
        headers += current_line
    parsed_headers, sep, _ = headers.partition(b'\r\n\r\n')
    print(parsed_headers.decode() + sep.decode())

parser = argparse.ArgumentParser(
    description='A simple web client'
)

parser.add_argument('url')
parser.add_argument('-m', '--request-method', default='GET', choices=REQUEST_METHODS)
parser.add_argument('-p', '--port', default=80)
args = parser.parse_args()

parsed_url = urlsplit(args.url)
protocol = parsed_url.scheme
target_host = parsed_url.netloc
requested_resource = parsed_url.path

request_line = f"{args.request_method} {requested_resource} {HTTP_VERSION}"   # This is the start-line
host = f"Host: {target_host}"
empty_line = ''

http_request = [
    request_line,
    host,
    empty_line
]

request = format_request(http_request)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((target_host, args.port))
send_request(request, s)
receive_response(s)
