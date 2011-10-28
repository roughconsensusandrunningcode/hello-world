#! /usr/bin/env python
import sys

if __name__ == '__main__':
    count = 1
    if len(sys.argv) == 2:
        count = int(sys.argv[1])
    for i in xrange (count):
        sys.stdout.write ("Hello World\n")

