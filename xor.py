#!/usr/bin/env python3

from cgi import print_directory
import sys

def boolfgv(a,b):
    return bool(a) != bool(b)

def main():
    print(boolfgv('Értelmetlen','Feladat'))
if __name__ == "__main__":
    main()