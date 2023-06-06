#!/usr/bin/python3
# 100-print_tebahpla.py

g = 0
for n in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(n - g)), end="")
    g = 32 if g == 0 else 0
