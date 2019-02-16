# Auto-Key cipher, modified from the following:
# Caesar Cipher
# http://inventwithpython.com/hacking (BSD Licensed)

def decrypt(keyword,message):
  # every possible symbol that can be encrypted
  LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  
  message = message.upper()
  keyword = keyword.upper()
  k = 0 # index for keeping track of position in the key

  # stores the encrypted/decrypted form of the message
  translated = ''

  # run the encryption/decryption code on each symbol in the message string
  for symbol in message:
    if symbol in LETTERS:
      # get the encrypted (or decrypted) number for this symbol
      num = LETTERS.find(symbol) # get the number of the symbol
      key = LETTERS.find(keyword[k]) # get the number of the corresponding key symbol
      num = num - key

      # handle the wrap-around if num is larger than the length of
      # LETTERS or less than 0
      if num >= len(LETTERS):
        num = num - len(LETTERS)
      elif num < 0:
        num = num + len(LETTERS)

      # add encrypted/decrypted number's symbol at the end of translated
      translated = translated + LETTERS[num]
    
      # add this plaintext symbol to the the key, so it can be used to encipher
      keyword = keyword + LETTERS[num]     
      k += 1 # go to the next character in the key

    else:
      # just add the symbol without encrypting/decrypting
      translated = translated + symbol
  
  return translated


def encrypt(keyword,message):
  # every possible symbol that can be encrypted
  LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  
  message = message.upper()
  keyword = keyword.upper()
  k = 0 # index for keeping track of position in the key

  # stores the encrypted/decrypted form of the message
  translated = ''

  # run the encryption/decryption code on each symbol in the message string
  for symbol in message:
    if symbol in LETTERS:
      # get the encrypted (or decrypted) number for this symbol
      num = LETTERS.find(symbol) # get the number of the symbol
      key = LETTERS.find(keyword[k]) # get the number of the corresponding key symbol
      num = num + key

      # handle the wrap-around if num is larger than the length of
      # LETTERS or less than 0
      if num >= len(LETTERS):
        num = num - len(LETTERS)
      elif num < 0:
        num = num + len(LETTERS)

      # add encrypted/decrypted number's symbol at the end of translated
      translated = translated + LETTERS[num]
      
      # add this plaintext symbol to the the key, so it can be used to encipher
      keyword = keyword + symbol
      k += 1 # go to the next character in the key

    else:
      # just add the symbol without encrypting/decrypting
      translated = translated + symbol
  
  return translated