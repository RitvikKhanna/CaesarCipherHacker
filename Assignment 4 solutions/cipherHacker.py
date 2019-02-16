# this program attempts to decipher a ciphertext of an unknown cipher.
# it tries to translate the autokey cipher, the caesar cipher, and the
# transposition cipher.

import sys, autokeyHacker, caesarHackerAuto, transpositionHacker

def main():
    # get the file of ciphertexts
    ciphertextsFile = open('ciphers.txt')
    ciphertexts = []
    for ciphertext in ciphertextsFile.read().split('\n'):
        ciphertexts.append(ciphertext)
    ciphertextsFile.close()
    
    # open the output file
    output = open('a4.txt', 'w')
    
    for i in range(10):
        # for all 10 ciphertexts in the file
        ciphertext = ciphertexts[i]
        print("Trying Caesar's Cipher...")
        mode = 'caesar'
        decryptions = testCaesar(ciphertext)
        if decryptions == None:
            print("Failed. Trying Autokey...")
            mode = 'autokey'
            decryptions = testAutokey(ciphertext)
            if decryptions == None:
                print("Failed. Trying Transposition Cipher...")
                mode = 'transposition'
                decryptions = testTransposition(ciphertext)
                if decryptions == None:
                    print("Failed. Unknown cipher. Quitting...")
                    sys.quit()
        print('Decryptions for', ciphertext, 'with %s cipher:'%(mode))
        print(decryptions)
        if len(decryptions) > 1:
            print("*********NOTE: Multiple decryptions**********")
        else:
            for key in decryptions:
                # write to the output file
                output.write(decryptions[key])
                output.write('\n')
                
    output.close()
        
    
def testAutokey(message):
    decryptions = autokeyHacker.dictAttack(message)
    if len(decryptions) == 0:
        return None
    
    return decryptions

def testCaesar(message):
    decryptions = caesarHackerAuto.autoBruteForce(message)
    if len(decryptions) == 0:
        return None
    
    return decryptions

def testTransposition(message):
    decryptions = transpositionHacker.hackTransposition(message)
    if len(decryptions) == 0:
        return None
    
    return decryptions

if __name__ == '__main__':
    main()