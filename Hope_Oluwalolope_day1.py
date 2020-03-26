# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 04:25:45 2020

@author: HP
"""
def eval_guess(input_number, target_number):
    if(input_number == target_number):
        return "equal"
    elif(input_number < target_number):
        return "too low"
    else:
        return "too high"
    
    
def guess_game(no_of_guesses, target_number):
    
    print("Guess a number between 0 and 100\n")
    
    i = 0
    
    while(i < no_of_guesses):
        print("You have ", (no_of_guesses - i), "chances left")
        try:
           input_number = int(input("Guess a number: "))       
        except ValueError:
           print("Not an integer! Try again.")
           continue
        else:
           result = eval_guess(input_number, target_number)
           if(result == "equal"):
               print("You guessed right \n")
               break
           else:
               print(result + "\n")
           i += 1
           
    diff = abs(target_number - input_number)
    print("the difference between your final guess and actual number is: ", diff)


guess_game(3, 70)
           
         
