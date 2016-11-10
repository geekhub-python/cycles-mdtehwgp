#!/usr/bin/env python3
import string
from random import *
characters = string.ascii_letters + string.digits
passwd_len = randint(6, 20+1)
password = ''.join(choice(characters) for x in range(passwd_len))
lpass = list(password)


for i in range(passwd_len):
    if lpass[i].isdigit() and lpass[i+1].isdigit():
        lpass.insert(i, '_')
    else:
        lpass.insert(randint(6, passwd_len), '_')
    break

print(''.join(lpass))
