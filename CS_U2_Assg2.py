# ------------------------------------------------------------------------------
# Name:      CS_U2_Assg2.py
# Purpose:   List Checker
# Author:    Maryil.H
# Created:   27/03/2017
# ------------------------------------------------------------------------------

#Remove Redundants function
def remove_redundants(og_list): 
 items = input("Please enter an item: ")
 if items not in og_list:
  og_list.append(items)
  print(og_list)
 elif items in og_list:
  print(og_list)
 return

#Has duplicates function
def has_duplicates(og_list):
 items = input("Please enter an item: ")
 if items not in og_list:
  og_list.append(items)
  print("true")
 elif items in og_list:
  print("false")
 return

#The list
og_list = []
#While loop to cycle through items that are added to the list
while True:
 #user input of an item
 items = input("Please enter an item: ")
 #if the item is already there print false and print the clean list
 if items in og_list:  
  print("false", og_list)
  continue
 #if the item is unique add it to the list and print the list
 if items not in og_list:
  og_list.append(items)
 print("true", og_list)



