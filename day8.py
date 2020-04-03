# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 07:17:15 2020

@author: HP
"""


def create_dictionary(secret_word):

  secret_word_dictionary = {}

  for i in range(len(secret_word)):
    if(secret_word[i] in secret_word_dictionary):
      lst = secret_word_dictionary[secret_word[i]]
      lst.append(i)
    else:
      secret_word_dictionary[secret_word[i]] = [i] 
  
  return secret_word_dictionary


def hangman(secret_word, trials):

  input_word_arr = ['_' for i in range(len(secret_word))]
  secret_word_dictionary = create_dictionary(secret_word)

  count = 0
  correct_guesses = 0

  print("".join(input_word_arr))

  while(count < trials):
    print("\n")
    print("You have ", (trials - count), " trials left")
    input_letter = input("Guess a letter: ")

    if input_letter in secret_word_dictionary:
      indices = secret_word_dictionary[input_letter]
      for index in indices:
        if input_word_arr[index] == '_':
          input_word_arr[index] = input_letter
          correct_guesses += 1
          break          

    print("".join(input_word_arr))

    if(correct_guesses == (len(input_word_arr))):
      break

    count += 1


  print("\n")
  print("Correct Word: ", secret_word)
  if(correct_guesses == (len(input_word_arr))):  
    return "You Won"
  
  return "You Lose"


print(hangman("poor", 5))