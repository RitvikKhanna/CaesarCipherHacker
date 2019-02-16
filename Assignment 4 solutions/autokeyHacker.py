# Bisan Hasasneh and Ritvik Khanna  CMPUT299 Win2018
# Q2 Assignment 4 - Fully Automated Autokey Cipher Breaker
# This code requires the detectEnglish.py module from Hacking Secret Ciphers with Python
# by Al Sweigart
# http://inventwithpython.com/hacking (BSD Licensed)

import detectEnglish, autokeyCipher

def main():
    # for testing purposes
    
    decryptions = dictAttack('XUKIRTXRH JKKF P LLLBB HM TZPZYXSS')
    print(decryptions)
    
    return

def dictAttack(ciphertext):
    # this functions attempts to break the cipher by using every word in a 
    # dictionary as the key for the autokey cipher.
    # returns a dictionary containing decipherments that appear to be English
    words = detectEnglish.loadDictionary()
    decryptions = {}
    
    # test all english words as keys
    for key in words:
        translation = autokeyCipher.decrypt(key, ciphertext)
        # add to dictionary if the translation appears to be English
        if detectEnglish.isEnglish(translation):
            decryptions[key] = translation
        
    return decryptions
    
    
# if the program is run instead of being imported as a module call main()
if __name__ == '__main__':
    main()