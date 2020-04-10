# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 03:53:03 2020

@author: HP
"""

def sieve_of_eratos(n):

  #initializing the list with True for all numbers before n. The index of the arr tells us the number while the value of the index indicates if it is prime or not. initially we assume all numbers are prime
  numbers = [True for i in range(n)]

  #crossing out possible multiples from 2 to sqrt(n), because multiples after the sqrt must have been crossed out during earlier operation, as they are squares of initial multiples
  # Loop's ending condition is (i * i) < n instead of i < sqrt(n) to avoid repeatedly calling an expensive function sqrt().
  i = 2
  while((i*i) < n):
    #if i is still indicating been a prime(i.e it has not been crossed out), we have to cross out all its multiples
    if (numbers[i] == True):
        for j in range((i * i), n, i):
            #instead of deleting multiples, which will be expensive and increase time complexity, we change the status
            numbers[j] = False;
    i += 1

  #iterate through the numbers arr and collect all numbers i.e indices whose status of been a prime still remains true
  primes = []

  for k in range(2, n):
    if (numbers[k] == True):
          primes.append(k)

  return primes;

print(sieve_of_eratos(100))