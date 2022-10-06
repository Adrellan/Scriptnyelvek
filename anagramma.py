#!/usr/bin/env python3

def anagramma(str1,str2):
    """
    Az alábbi függvény vár két string paramétert,
    majd a szóban/mondatban lévő betűket sorbarendezve szóköz eltávolítással, eldönti,
    hogy a 'str2' kirakható e az 'str1' betűiből
    
    Válaszként egy igaz/hamis értéket kapunk vissza 
    """
    return sorted(str1.lower())==sorted(str2.lower())

def main():
    print(anagramma("liba".replace(" ",""),"Bali".replace(" ","")))

if __name__ == "__main__":
    main()