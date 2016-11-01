#!/usr/bin/env python3
# Найти произведение 5 * 6 * 7 * ... * 13.
begin_seq = 5
end_seq = 13

gen = begin_seq
for i in range(begin_seq, end_seq):
    gen += gen * i

print(gen)
#print(gen)
