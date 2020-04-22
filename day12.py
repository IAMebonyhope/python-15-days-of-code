# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 13:18:49 2020

@author: HP
"""
points = {'a': 1, 'e': 1, 'i': 1, 'l': 1, 'n': 1,'o': 1,'r': 1,'s': 1,'t': 1,'u': 1,'d': 2,'g': 2,'b': 3,'c': 3,'m': 3,'p': 3,'f': 4,'h': 4,'v': 4,'w': 4,'y': 4,'k': 5,'j': 8,'x': 8,'q': 10,'z': 10}

def word_score(word):
    
    score = 0
    for ch in word:
        if ch.isalpha():
            score += points[ch.lower()]
    
    return score



print(word_score("quixotic"))
print(word_score("maximize"))
print(word_score("jezebel"))
print(word_score("quizzify"))
print(word_score("fortune"))
    