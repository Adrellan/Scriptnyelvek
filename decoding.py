#!/usr/bin/env python3
"""
a-z 97-122
A-Z 65-90
K → M, O → Q, E → G
key = 2
"""

TEXT = """"
Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb
"""

#text is a string, key is an inetger
def decoding(text, key):
    new_text = ""
    for c in text:
        if(ord(c)>=65 and ord(c)<97):
            value=(ord(c)+key)%91
            if(value<65): value=value+65
            new_text+=(chr(value))
        elif (ord(c)>=97 and ord(c)<=122):
            value=(ord(c)+key)%123
            if(value<97): value=value+97
            new_text+=(chr(value))
        else:
            new_text+=(c)

    return new_text

def main():
    print(decoding(TEXT,2))

if __name__ == "__main__":
    main()