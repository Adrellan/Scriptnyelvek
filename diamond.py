#!/usr/bin/env python3
from cgi import print_directory
from string import whitespace
import sys

def diamond(height):
    star='*'
    minus_star=2
    line = 0
    while(line < height):
        line+=1
        stars_at_line = (2*line-1)*star
        if(len(stars_at_line) > height):
            stars_at_line = (height-minus_star)*star
            minus_star+=2 
        print(stars_at_line.center(height,' '))

def main():
    diamond(7)

if __name__ == "__main__":
    main()