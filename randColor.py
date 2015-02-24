#!/usr/bin/env python

import random

bg = random.randint(0,7)
fg = random.randint(0,7)

if bg == fg:
    fg += 1

PROMPT = 'set prompt="%%{\033[2;4%d;3%dm%%}%%B%%m%%b%%{\033[0m%%}\[%%U$WHERE%%u\:%%~\] "' % (bg,fg,)
PROMPT2 = '2;4%d;3%d' % (bg,fg,)

print PROMPT
print PROMPT2
