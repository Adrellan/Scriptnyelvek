#!/usr/bin/env python3

from cgi import print_directory
import sys

def main():
    print("A lang_info tömböt írjuk ki soronként tördelve, fix keretek között megadva\n")
    lang_info =  [('Fortran', 1954, 0.435), ('Cobol', 1959, 0.391),
              ('C', 1972, 16.076), ('C++', 1980, 9.014), 
              ('Python', 1991, 6.482), 
              ('Java', 1995, 17.99), ('C#', 2001, 6.687)]

    print ("{0:<12} {1:^16} {2:>16}".format("Language", 
                                       "Year Developed", 
                                       "TIOBE rating"))
    print ("-"*46)
    for element in lang_info:
        print ("{0:12} {1:^16} {2:16}".format(element[0], element[1], element[2]))

    print()

    print("A 'num_format' segítségével egyszerűen lehet vesszővel ellátni kis,- és nagy számokat bárhol\n")
    num_format = "{:,}".format
    print(num_format(10000000000))
    print(num_format(1005409))
    print(num_format(155248))

    """
    s1 = "cats"
    s2 = "dogs"
    s3 = "%s and %s living together" % (s1, s2)
    print(s3)
    s4 = "{} and {} living together ".format(s1, s2)
    print(s4)

    print("{0:d} - {0:x} - {0:o} - {0:b} ".format(21))
    #21 - 15 - 25 - 10101

    ## defining formats
    email_f = "Your email address was {email}".format

    ## use elsewhere
    print(email_f(email="bob@example.com"))
    """

if __name__ == "__main__":
    main()