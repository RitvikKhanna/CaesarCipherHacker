# Bisan Hasasneh and Ritvik Khanna  CMPUT299 Win2018
# Q1 Assignment 4 - Fully Automated Caesar Cipher Breaker
# This code requires the detectEnglish.py module from Hacking Secret Ciphers with Python
# Some code taken from caesarHacker.py from Hacking Secret Ciphers with Python
# by Al Sweigart
# http://inventwithpython.com/hacking (BSD Licensed)

import detectEnglish

def main():
    # for testing purposes
    messages = ['GUVF VF ZL FRPERG ZRFFNTR.', 'NKXK OY G YGSVRK OTVAZ LUX EUAX VXUMXGS', 'ESP ZYWJ HZCO DAPWWPO TYNZCCPNEWJ TY L RZZO OTNETZYLCJ TD TYNZCCPNEWJ', 'BCCB']
    for message in messages:
        decryptions = autoBruteForce(message)
        print(decryptions)
    return

def autoBruteForce(message):
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # decryptions is a dict of translations that appear to be English
    decryptions = {}
    
    # loop through every possible key
    for key in range(len(LETTERS)):
        translated = ''
        # from the original Caesar program - decrypt using this key
        for symbol in message:
            if symbol in LETTERS:
                num = LETTERS.find(symbol)
                num = num - key
                
                # handle wrap around
                if num < 0:
                    num = num + len(LETTERS)
                
                # add decrypted symbol to translated
                translated = translated + LETTERS[num]
                
            else:
                # symbol not in LETTERS - append as is to translated
                translated = translated + symbol
        
        # check if this decryption is English
        if detectEnglish.isEnglish(translated):
            # add this translation with its key to the decryptions dict
            decryptions[key] = translated
    
    # print(decryptions)
    return decryptions

# if the program is run instead of being imported as a module call main()
if __name__ == '__main__':
    main()