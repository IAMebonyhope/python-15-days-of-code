# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 21:22:55 2020

@author: HP
"""

def is_Nigerian1(number):
    
    start = 0

    if(len(number) != 11) and (len(number) != 13) and (len(number) != 14):
        return False

    if(len(number) == 11) and (number[0] != '0'):
        return False
    
    if(len(number) == 14) and (number[0] != '+'):
        return False
    
    if(len(number) == 14):
        start = 1
    
    if(len(number) == 13) or (len(number) == 14):
        if(number[start] != '2') and (number[start+1] != '3') and (number[start+2] != '4'):
            return False
   
    for i in range(start, len(number)):
        if not (number[i].isdigit()):
            return False
    
    return True

import re

def is_Nigerian2(number):

    if(len(number) != 11) and (len(number) != 13) and (len(number) != 14):
        return False

    if(len(number) == 11) and not (re.match(r'[0]\d{10}$', number)):
        return False
    
    if(len(number) == 13) and not (re.match(r'[2][3][4]\d{10}$', number)):
        return False
    
    if(len(number) == 14) and  not (re.match(r'[+][2][3][4]\d{10}$', number)):
        return False
  
    return True

print(is_Nigerian2("090568704001"))
    
    
        
    
    
    