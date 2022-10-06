#!/usr/bin/env python3

def mely_magas(word):
    s = set()
    magas_hangok={'e', 'é', 'i', 'í', 'ö', 'ő', 'ü', 'ű'}
    mely_hangok={'a', 'á', 'o', 'ó', 'u', 'ú'}
    hangrendek=['magas', 'mély', 'vegyes', 'semmilyen']
    s.update(word)

    if(len(set(magas_hangok) & set(s)) > 0 and len(set(mely_hangok) & set(s)) > 0):
        return hangrendek[2]
    elif(len(set(magas_hangok) & set(s)) > 0 and len(set(mely_hangok) & set(s)) == 0):
        return hangrendek[0]
    elif(len(set(magas_hangok) & set(s)) == 0 and len(set(mely_hangok) & set(s)) > 0):
        return hangrendek[1]
    else:
        return hangrendek[3]


def main():
    words = ["ablak", "erkély", "kisvasút", "magas", "mély", "pfff"]

    for i in words:
        print(i,'->',mely_magas(list(i)))

if __name__ == "__main__":
    main()