#!/usr/bin/env python3

from cgi import print_directory
import string
import sys

def main():
# 1. feladat
# ['auto', 'villamos', 'metro'] → ['AUTO!', 'VILLAMOS!', 'METRO!']

    stringlist = ["szilva", "körte", "cseresznye"]
    print('#1',list(map(lambda x: x.upper(), stringlist)))

# 2. feladat
# ['aladar', 'bela', 'cecil'] → ['Aladar', 'Bela', 'Cecil']

    print('#2',list(map(lambda x: x.capitalize(), stringlist)))

# 3. feladat
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], azaz inicializáljunk egy 10-elemű listát csupa 0-val.

    list_of_zeros = [0] * 10
    print('#3',list_of_zeros)

# 4. feladat
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] → [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

    default = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    modified = list(map(lambda x: x*10,default))
    print('#4',modified)

# 5. feladat
# ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'] → [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] (az első listában sztringek vannak)

    defaultstr = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    modifiedstr = list(map(lambda x: int(x),defaultstr))
    print('#5',modifiedstr)

# 6. feladat
# "1234567" → [1, 2, 3, 4, 5, 6, 7], vagyis van számunk sztring formátumban, s egy listába be akarjuk tenni a számjegyeit (számokként)

    num = 1234567
    list_of_num = [int(d) for d in str(num)]
    print('#6',list_of_num)

# 7. feladat
# 'The quick brown fox jumps over the lazy dog' → [3, 5, 5, 3, 5, 4, 3, 4, 3], vagyis állapítsuk meg az egyes szavak hosszát

    original_str = 'The quick brown fox jumps over the lazy dog'
    original_list = list(original_str.split())
    num_words_list = []
    for i in original_list:
        num_words_list.append((len(i)))
    print('#7',num_words_list)

# 8. feladat
# "python is an awesome language" → ['p', 'i', 'a', 'a', 'l'], vagyis egy sztring szavainak a kezdőbetűit gyűjtsük össze egy listában

    original_str = 'python is an awesome language'
    original_list = list(original_str.split())
    list_of_first_letters = list(map(lambda x: x[0],original_list))
    print('#8',list_of_first_letters)

# 9. feladat
# 'The quick brown fox jumps over the lazy dog' → [('The', 3), ('quick', 5), ('brown', 5), ('fox', 3), ('jumps', 5), ('over', 4), ('the', 3), ('lazy', 4), ('dog', 3)], vagyis a listában tuple-öket helyezzünk el a következő szerkezettel: (szó, szóhossz).

    original_str = 'The quick brown fox jumps over the lazy dog'
    original_list = list(original_str.split())
    num_words_list = []
    for i in original_list:
        num_words_list.append((len(i)))
    st_tuple = list(zip(original_list,num_words_list))
    print('#9',st_tuple)

# 10. feladat
# [0, 2, 4, 6, 8], vagyis állítsuk elő egy listában a 10-nél kisebb páros számokat

    even_list = [ x for x in range(1, 10) if x % 2 == 0]
    print('#10',even_list)

# 11. feladat
# Vegyük a 20-nál kisebb számokat s állítsuk elő ezeknek a négyzetét. Ezen négyzetszámok közül csak a párosakat hagyjuk meg ([0, 4, 16, 36, 64, 100, 144, 196, 256, 324]).

    even_list_pow2 = [ x**2 for x in range(0, 20) if x**2 %2 ==0]
    print('#11',even_list_pow2)

# 12. feladat
# Vegyük a 20-nál kisebb számokat s állítsuk elő ezeknek a négyzetét. Ezen négyzetszámok közül csak azokat hagyjuk meg, melyeknek az utolsó számjegye "4" ([4, 64, 144, 324]).

    lastfour = [ x**2 for x in range(0, 20) if x**2 %10 == 4]
    print('#12',lastfour)

# 13. feladat
# Gyűjtsük össze az angol ábécé nagybetűit egy listában (használjuk a chr függvényt), majd fűzzük össze az elemeket egyetlen sztringgé: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.

    alphabet_string = string.ascii_uppercase
    alphabet_list = list(alphabet_string)
    print('#13',''.join(alphabet_list))

# 14. feladat
# [' apple ', ' banana ', ' kiwi'] → ['apple', 'banana', 'kiwi'], vagyis a listában lévő szavak elejéről és végéről távolítsuk el a whitespace karaktereket

    stringlist = [' apple ', ' banana ', ' kiwi']
    modified_stringlist = [ x.strip() for x in stringlist]
    print('#14',modified_stringlist)

# 15. feladat
# [1, 0, 1, 1, 0, 1, 0, 0] → "10110100", vagyis a listában lévő számjegyeket fűzzük össze egy sztringgé

    intlist = [1, 0, 1, 1, 0, 1, 0, 0]
    str_intlist = [str(x) for x in intlist]
    print('#15',''.join(str_intlist))

if __name__ == "__main__":
    main()