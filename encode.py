import sys
import re

ciphertext = sys.argv[1]
keytext = sys.argv[2]

def encode(cipher, key):
    cipher = ''.join(cipher.split()).upper().replace("j", "i")
    doubleletters = True
    while(doubleletters):
        x = False
        for i in range(0, len(cipher) - 1):
            if cipher[i] == cipher[i + 1]:
                x = True
                cipher = cipher[:i + 1] + "x" + cipher[i + 1:]
        doubleletters = x
    if len(cipher) % 2 == 1:
        cipher += "x"
    encoded = ""
    for i in range(0, len(cipher)/2):
        a = cipher[i * 2]
        b = cipher[(i * 2) + 1]
        aind = getIndex(a, key)
        bind = getIndex(b, key)
        if (aind[0] == bind[0]):
            encoded += letterByIndex([(aind[0] + 1) % 5, aind[1]], key)
            encoded += letterByIndex([(bind[0] + 1) % 5, bind[1]], key)
        elif (aind[1] == bind[1]):
            encoded += letterByIndex([aind[0], (aind[1] + 1) % 5], key)
            encoded += letterByIndex([bind[0], (bind[1] + 1) % 5], key)
        else:
            encoded += letterByIndex([bind[0], aind[1]], key)
            encoded += letterByIndex([aind[0], bind[1]], key)
    print(encoded)

def getIndex(letter, key):
    index = key.find(letter)
    x = index % 5
    y = (index - x) / 5
    return [x, y]

def letterByIndex(index, key):
    i = index[0] + (5 * index[1])
    return key[i]


encode(ciphertext, keytext)
