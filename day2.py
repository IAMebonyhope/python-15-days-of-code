# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 06:16:15 2020

@author: HP
"""
import random

def password_generator(length):
    
    characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";  
    password = "";
    
    if(length >= 8):
        for i in range(length):
            password += random.choice(characters)

    return password;


pswd = password_generator(6)
if(pswd == ""):
    print("weak password")
print(pswd)
    

    