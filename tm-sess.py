#!/usr/bin/env python3.3

import subprocess
import os
import re
import codecs

#tmux lsp -as | grep $TMUX_PANE

tm_cmd = ['tmux', 'lsp', '-as']

def main():
    s_proc = subprocess.Popen(tm_cmd, stdout=subprocess.PIPE)
    tm_s_lines = s_proc.stdout.readlines()

    pane = os.environ['TMUX_PANE']
    iPane = int(pane[1:])

    mre = re.compile('%(\d+)')
    for aLine in tm_s_lines:
        aLine = codecs.decode(aLine).strip()
        m = mre.search(aLine)
        if m:
            for am in m.groups():
                if int(am) == iPane:
                    print(aLine.split(':')[0])
                    return

    print('')

if __name__ == '__main__':
    main()
