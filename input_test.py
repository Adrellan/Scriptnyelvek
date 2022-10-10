#!/usr/bin/env python3
import time

from cgi import print_directory
import sys
import matplotlib.pyplot as plt

def szamlista(max_num):
    ret_val=""

    for n in range(1,15+1):
        ret_val += str(n)

    return ret_val

def szamlista2(max_num):
    ret_val=""

    for n in range(1,15+1):
        ret_val += str(n)

    return ret_val    

def main():
    # szam = int(input("Várakozási idő: "))
    # szam+=1

    # time.sleep(szam)
    # print(szam)

    #print(szamlista)

    y = [n*n for n in range(-5,5+1)]
    plt.plot(y)
    plt.show(y)


if __name__ == "__main__":
    main()