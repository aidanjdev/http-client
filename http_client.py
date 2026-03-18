#!/usr/bin/env python3

import argparse
import socket

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

HTTP_VERSION = "HTTP1.1"

parser = argparse.ArgumentParser(
    description='A simple web client'
)

parser.add_argument('url')
parser.add_argument('-m', '--request-method', default='GET', choices=REQUEST_METHODS)
parser.add_argument('-p', '--port', default=80)
args = parser.parse_args()

host =  
request_line = f"{args.request_method} {args.request_target} {HTTP_VERSION}\r\n"   # This is the start-line

http_request = {
    'start_line': request_line,
    'host': host,
    'empty_line': '\r\n'
}


print(request_line)
