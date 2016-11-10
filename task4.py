#!/usr/bin/env python3
for i in range(11, 100000, 11):
    if(i % 2 == 1 and i % 3 == 1 and i % 4 == 1 and i % 5 == 1 and i % 6 == 1
				 and i % 7 == 1 and i % 8 == 1 and i % 9 == 1 and i % 10 == 1 and i % 11 == 0):
	    print(i)
