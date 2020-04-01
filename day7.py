# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 06:14:26 2020

@author: HP
"""

"""
Function that takes in the room number list as parameter and returns the captain's room (i.e room number with only one person).
All other room contain N persons and N > 1 (i.e contain more than 1 person)
"""
def captains_room(room_no_list):
  #room_no_list: list containing room numbers

  if(len(room_no_list) < 1):
    return -1

  #dictionary to hold room numbers as keys and the number of people in the room as values
  rooms = {}

  #iterate through the room number list, for each element in the list:
  #if it is present in the rooms dictionary as a key, then increment the value of the key by 1
  #else add the element as a new key to the dictionary and its value initialized as 1
  for i in range(len(room_no_list)):
    if(room_no_list[i] in rooms):
      rooms[room_no_list[i]] += 1
    else:
      rooms[room_no_list[i]] = 1
  
  #iterate through the dictionary and return the key(room number) whose value is 1
  for key in rooms:
    if(rooms[key] == 1):
      return key

  #if no room is found with just 1 person, then return -1  
  return -1


room = captains_room([1,2,3,6,5,4,4,2,5,3,6,1,6,5,3,2,4,1,2,5,1,4,3,6,8,4,3,1,5,6,2])
if(room != -1):
  print("captain's room number =", room)
else:
  print("captain's room not found")
