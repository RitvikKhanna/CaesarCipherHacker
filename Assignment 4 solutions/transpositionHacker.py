
import math, detectEnglish


def main():
    message = 'Cenoonommstmme oo snnio. s s c'
    decryptions = hackTransposition(message)
    print(decryptions)


def decryptMessage(key, message):
    numOfColumns = math.ceil(len(message) / key)
    numOfRows = key
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

    plaintext = [''] * numOfColumns

    col = 0
    row = 0

    for symbol in message:
        plaintext[col] += symbol
        col += 1 

        if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            col = 0
            row += 1

    return ''.join(plaintext)


def hackTransposition(message):
    decryptions = {}
    
    for key in range(1, len(message)):
        translated = decryptMessage(key, message)
        if detectEnglish.isEnglish(translated):
            decryptions[key] = translated
    return decryptions

if __name__ == '__main__':
    main()