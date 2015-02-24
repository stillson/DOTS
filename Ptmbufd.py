#!/usr/bin/env python

import SocketServer
import subprocess

class MyTCPHandler(SocketServer.StreamRequestHandler):
    def handle(self):
        self.data = self.rfile.readlines()
        self.tmux_buffer = ''.join(self.data)
        print self.tmux_buffer
        subprocess.call(['tmux', 'set-buffer', self.tmux_buffer])

if __name__ == "__main__":
    HOST, PORT = "", 7531

    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()

"""
#!/bin/sh

cat $* | nc localhost 7531

#tmb: aliased to tmux load-buffer
"""
