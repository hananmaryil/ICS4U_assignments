# ------------------------------------------------------------------------------
# Name:      CS_U2_Assg3.py
# Purpose:   Multi-Dimensional Lists
# Author:    Maryil.H
# Created:   03/04/2017
# ------------------------------------------------------------------------------
import random 

#Create Matrix Function
def create_matrix():        
    while True:    
        #Get the users input "n"
        n = input("Please enter the size of your new list: ")
        #Check if the input is an integer
        if n.isdigit() == False:
                print("Please enter a valid integer")
                continue
        #Check if the input is greater than 1
        elif int(n) < 1:
            print("Please enter a valid integer")
            continue
        #Create the matrix and then go into the other functions
        else:
                n = int(n)                
                matrix = [[random.randint(0,9) for i in range(n)] for j in range(n)]        
                print(matrix)
                transpose(matrix)
                continue
        break
    return

#Transpose function
def transpose(matrix):
    while True:
        #Ask if the user wants to transpose the list
        ask = input("Would you like to tranpose this list (yes/no): ")
        #If the user says yes then transpose the list
        if ask.lower() == 'yes':
            #tranpose function
            result = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
            for r in result:
                print(r)
            is_symmetric(matrix)
            break
        #If the user says no then go back to the create matrix function
        elif ask.lower() == 'no':
            create_matrix()
        
        #If the user does not say yes or no, say it is invalid and ask again
        else:
            print("That entry is invalid")
    return
def is_symmetric(matrix):    
    while True:
        #Variable for boolean value True
        symmetric = "True. That is symmetric"
        #Tranposed list
        result = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]                           
        #Check if the tranposed list is the same as the original matrix
        if matrix != result:
            #If it is not equal, say it is not symmetric
            print("False. That is not symmetric")
        elif matrix == result:
            print(symmetric)
        #If it is equal, say it is symmetric
        return

#TEST SCRIPT
#square not symmetrical    
matrix = [[4,2],[6,8]]
print(matrix)
transposed = transpose(matrix)
print(transposed)
#square symmetrical
matrix = [[2,1],[1,2]]
print(matrix)
transposed = transpose(matrix)
print(transposed)
#not square non-symmetrical
matrix = [[1,2,3],[1,2,3]]
print(matrix)
transposed = transpose(matrix)
print(transposed)
#not square non-symmetrical
matrix = [[1,2],[3,4],[5,6]]
print(matrix)
transposed = transpose(matrix)
print(transposed)

#Call the main function for actual user friendly code
create_matrix()