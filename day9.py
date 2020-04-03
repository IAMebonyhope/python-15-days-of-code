# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 07:19:24 2020

@author: HP
"""


def decryptor(text, key):
  """
  text: input text to be decrypted
  key: number of actual text away with the direction

  returns decrypted text
  """

  #array for keeping converted characters to decrease overhead of string concatenation
  decrypted_text = []

  #iterate through each character in the input text
  for ch in text:
    #checks if character is an alphabet
    #converts the character to its alphabetical index using ascii value operations i.e 'a' = 0, 'z' = 25
    #adds the key to the index and use modulus to rotate back to the alphabet array incase of overflow during operation
    #converts the index gotten from the calculation above to its actual character
    if(ch.isalpha()):
      ch_val = ord(ch.lower()) - 97
      decrypted_val = (ch_val + key) % 26
      decrypted_ch = chr(decrypted_val+97)

    if(ch.islower()):
      decrypted_text.append(decrypted_ch)
    elif(ch.isupper()):
      decrypted_text.append(decrypted_ch.upper())
    else:
      decrypted_text.append(ch)

  return "".join(decrypted_text)


print(decryptor("Rcb mjh 9 xo cqn 30 mjhb xo lxmn lqjuunwpn!!", 17))



  
