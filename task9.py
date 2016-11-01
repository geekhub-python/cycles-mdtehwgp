#!/usr/bin/env python3

char = input('char: ').lower()

for i in range(ord(char)+1, ord(char)+4):
    if i > ord('z'):
        print(chr(i-26))
    else:
        print(chr(i))
