#!/usr/bin/env python3

from cgi import print_directory
import sys

def main():
    abc = [*range(97, 123,1)]

    for i in abc:
	    print(chr(i), end=' ')

if __name__ == "__main__":
    main()