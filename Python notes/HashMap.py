string = "Scott"
hashList = []

for i in range(100000):
    hashList.append("null")

def hash(word):
    asList = list(word)
    hashVal = 0

    for letter in asList:
        if(ord(letter) % 2 == 0):
            hashVal *= ord(letter)
        else:
            hashVal += ord(letter)

        hashVal /= 13

    i = 1

    while(True):

        try:
            if(hashList[int(hashVal)] == "null"):
                hashList[int(hashVal)] = word
                break
            else:
                i += 1
        except:
            hashVal = int(hashVal/2) + i
            i += 1
            continue
        break

    return int(hashVal)

print(str(hash(string)) + ": " + hashList[hash(string)])

