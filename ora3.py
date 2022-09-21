#!/usr/bin/env python3

from cgi import print_directory
import sys

def szorzat(li):
    a=1
    for x in li:
        a=a*x

    return a

def main():
    li = []
    li.append(420)
    li.append(69)
    li.append(666)
    li.append(777)

    li2 = ["abc", "xyz", "jkl"]

    li.extend(li2)

    print(f"{li=}")
    print(f"{li2=}")

    indexof_xyz = li2.index("xyz")
    print(indexof_xyz)

    li3 = [2,3,4]
    print(szorzat(li3))


if __name__ == "__main__":
    main()