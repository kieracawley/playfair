import sys

ciphertext = sys.argv[2]
keytext = sys.argv[3]

def encode(cipher, key):
    cipher = ''.join(cipher.split()).upper().replace("J", "I")
    encoded = ""
    doubleLetterCount = 0
    for i in range(0, len(cipher) - 1):
        if cipher[i] == cipher[i + 1]:
            if (i + doubleLetterCount) % 2 == 0:
                doubleLetterCount += 1
    if (len(cipher) + doubleLetterCount) % 2 == 1:
        cipher += "X"
    dl = 0
    for i in range(0, (len(cipher) / 2) + doubleLetterCount):
        if (i * 2) + 1 - dl < len(cipher):
            a = cipher[(i * 2) - dl]
            b = cipher[(i * 2) + 1 - dl]
            aind = getIndex(a, key)
            bind = getIndex(b, key)
            if (a == b):
                dl += 1
                xind = getIndex("X", key)
                encoded += letterByIndex([xind[0], aind[1]], key)
                encoded += letterByIndex([aind[0], xind[1]], key)
            elif (aind[0] == bind[0]):
                encoded += letterByIndex([(aind[0] + 1) % 5, aind[1]], key)
                encoded += letterByIndex([(bind[0] + 1) % 5, bind[1]], key)
            elif (aind[1] == bind[1]):
                encoded += letterByIndex([aind[0], (aind[1] + 1) % 5], key)
                encoded += letterByIndex([bind[0], (bind[1] + 1) % 5], key)
            else:
                encoded += letterByIndex([bind[0], aind[1]], key)
                encoded += letterByIndex([aind[0], bind[1]], key)
    print(encoded)

def decode(cipher, key):
    decoded = ""
    for i in range(0, (len(cipher) / 2)):
        a = cipher[(i * 2)]
        b = cipher[(i * 2) + 1]
        aind = getIndex(a, key)
        bind = getIndex(b, key)
        if (aind[0] == bind[0]):
            decoded += letterByIndex([(aind[0] - 1) % 5, aind[1]], key)
            decoded += letterByIndex([(bind[0] - 1) % 5, bind[1]], key)
        elif (aind[1] == bind[1]):
            decoded += letterByIndex([aind[0], (aind[1] - 1) % 5], key)
            decoded += letterByIndex([bind[0], (bind[1] - 1) % 5], key)
        else:
            decoded += letterByIndex([bind[0], aind[1]], key)
            decoded += letterByIndex([aind[0], bind[1]], key)
    print(decoded)


def getIndex(letter, key):
    index = key.find(letter)
    x = index % 5
    y = (index - x) / 5
    return [x, y]

def letterByIndex(index, key):
    i = index[0] + (5 * index[1])
    return key[i]

if sys.argv[1] == "encode":
    encode(ciphertext, keytext)
if sys.argv[1] == "decode":
    decode(ciphertext, keytext)
