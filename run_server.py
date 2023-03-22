
import os
import sys
import subprocess

import http.server
import socketserver
import socket
import threading

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def do_GET(self, *args):
        print(f'do_GET({self}, {args})')
        return super().do_GET(*args)

def open_browser_t(to_url):
    import time
    import webbrowser
    time.sleep(0.5)
    webbrowser.open(to_url)

def main(args=sys.argv):
    our_ip_addr = socket.gethostbyname( socket.gethostname() )
    port = 8080
    server_url = f'http://{our_ip_addr}:{port}/'
    
    threading.Thread(target=open_browser_t, args=(server_url, )).start()

    with socketserver.TCPServer(('', port), Handler) as httpd:
        print(f'Serving {server_url}')
        httpd.serve_forever()



if __name__ == '__main__':
    main()

