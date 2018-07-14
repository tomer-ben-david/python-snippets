#!/usr/bin/env python
"""
Very simple HTTP server in python.
Usage::
    ./dummy-web-server.py [<port>]
Send a GET request::
    curl http://localhost
Send a HEAD request::
    curl -I http://localhost
Send a POST request::
    curl -d "foo=bar&bin=baz" http://localhost
"""
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import subprocess
from urlparse import parse_qs
import json

# http://ec2-54-242-165-191.compute-1.amazonaws.com:8080/?title=skhfskjfs%20skfdhskjf%20akjfdh%20askfhakjs%20hfakjshfkjas%20f&description=asklhf%20aksjfd%20kajskjasfkjashfkaasklhf%20aksjfd%20kajskjasfkjashfkaasklhf%20aksjfd%20kajskjasfkjashfkaasklhf%20aksjfd%20kajskjasfkjashfkaasklhf%20aksjfd%20kajskjasfkjashfkaasklhf%20aksjfd%20kajskjasfkjashfkaasklhf%20aksjfd%20kajskjasfkjashfkaasklhf%20aksjfd%20kajskjasfkjashfkaasklhf%20aksjfd%20kajskjasfkjashfkaasklhf%20aksjfd%20kajskjasfkjashfkaasklhf%20aksjfd%20kajskjasfkjashfkaasklhf%20aksjfd%20kajskjasfkjashfkaasklhf%20aksjfd%20kajskjasfkjashfkaasklhf%20aksjfd%20kajskjasfkjashfkaasklhf%20aksjfd%20kajskjasfkjashfkaasklhf%20aksjfd%20kajskjasfkjashfkaasklhf%20aksjfd%20kajskjasfkjashfkaasklhf%20aksjfd%20kajskjasfkjashfkaasklhf%20aksjfd%20kajskjasfkjashfkaasklhf%20aksjfd%20kajskjasfkjashfkaasklhf%20aksjfd%20kajskjasfkjashfkaasklhf%20aksjfd%20kajskjasfkjashfkaasklhf%20aksjfd%20kajskjasfkjashfkaasklhf%20aksjfd%20kajskjasfkjashfkaasklhf%20aksjfd%20kajskjasfkjashfkaasklhf%20aksjfd%20kajskjasfkjashfkaasklhf%20aksjfd%20kajskjasfkjashfkaasklhf%20aksjfd%20kajskjasfkjashfkaasklhf%20aksjfd%20kajskjasfkjashfkaasklhf%20aksjfd%20kajskjasfkjashfkaasklhf%20aksjfd%20kajskjasfkjashfkaasklhf%20aksjfd%20kajskjasfkjashfkaasklhf%20aksjfd%20kajskjasfkjashfkaasklhf%20aksjfd%20kajskjasfkjashfkaasklhf%20aksjfd%20kajskjasfkjashfkaasklhf%20aksjfd%20kajskjasfkjashfkaasklhf%20aksjfd%20kajskjasfkjashfka%20sfkjsaf%20akhf%20akshfdkashfkjsahfdkjashfdieyiuy888888888%20%2067676akshfdkashfkjsahfdkjashfdieyiuy888888888%2067676akshfdkashfkjsahfdkjashfdieyiuy888888888%2067676akshfdkashfkjsahfdkjashfdieyiuy888888888%2067676akshfdkashfkjsahfdkjashfdieyiuy888888888%2067676akshfdkashfkjsahfdkjashfdieyiuy888888888%2067676akshfdkashfkjsahfdkjashfdieyiuy888888888%2067676

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        params = self.path[2:]
        if 'title' in params:
            print("params: " + params)
            print("url params: " + str(parse_qs(params)))
            title = str(parse_qs(params)['title'][0])
            description = str(parse_qs(params)['description'][0])

            # productner_homedir = '/home/itamar/tmp'
            productner_homedir = '/home/ubuntu/productner'
            productner_inputfilepath = productner_homedir + "/Product Dataset.csv"

            text_file = open(productner_inputfilepath, "w")
            text_file.write('id,name,description\n')
            text_file.write('000' + ',' + title + ',' + description)
            text_file.close()

            create_input_result = subprocess.check_output(["python extract.py ./models/ Product\ Dataset.csv"], cwd="/home/ubuntu/productner", shell=True)
            predict_result = subprocess.check_output(["python extract.py ./models/ Product\ Dataset.csv"], cwd="/home/ubuntu/productner", shell=True)
            self.wfile.write(json.dumps(predict_result))

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        # Doesn't do anything with posted data
        self._set_headers()
        self.wfile.write("<html><body><h1>POST!</h1></body></html>")

def run(server_class=HTTPServer, handler_class=S, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)

    # SSL
    # import ssl
    # httpd.socket = ssl.wrap_socket (httpd.socket, certfile='/home/ubuntu/keys/mypemfile.pem', server_side=True)

    print 'Starting httpd...'
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()