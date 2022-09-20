#!/usr/bin/env python3

from cgi import print_directory
import sys

def main():

    #sztring metódus (csak az első szekció kell, a 'Sztring metódus' rész)
    #Név bekérve, metódus kiválasztva
    name = input("Név: ")
    print(f"Szia {name.capitalize()}!\n")

    #palindróm (triviális és rekurzív módszerrel)
    #Triviális
    print("Trivális:")
    print(name+"-Palindróm\n") if name.lower()==name[::-1].lower() else print(name+"-Nem palindróm\n")

    #Iteratív
    print("Iteratív:")
    j=len(name)-1
    for c in name:
        if(c.lower()!=name[j].lower()):
            print(name+"-Nem palindróm\n")
            break
        elif(c.lower()==name[len(name)-1].lower()):
            print(name+"-Palindróm\n")
            break
        else:
            j-=1  

    #Rekurzív
    print("Rekurzív:")      
    def palindrome_check(s):
        return len(s) < 2 or s[0] == s[-1] and palindrome_check(s[1:-1])
    
    print(name+"-Palindróm\n") if palindrome_check(name.lower()) == True else print(name+"-Nem palindróm\n")

if __name__ == "__main__":
    main()