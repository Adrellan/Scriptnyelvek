#!/usr/bin/env python3

from cgi import print_directory
import sys

def get_movie_info():
    return ("Total recall",1990,7.6)

def main():
    title, _, _ = get_movie_info()
    print(title)

if __name__ == "__main__":
    main()