#!/usr/bin/env python

import subprocess
import time

while 1:
    p = subprocess.Popen(['tmux', 'list-buffers'], stdout=subprocess.PIPE)

    bufs = p.stdout.readlines()

    arr = [ x.split() for x in bufs]

    arr.reverse()

    for b in arr:
        if int(b[1]) < 3:
            subprocess.call(['tmux', 'delete-buffer', '-b', b[0][:-1]])

    time.sleep(30)
