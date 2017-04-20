# ------------------------------------------------------------------------------
# Name:      CS_U2_Assg4.py
# Purpose:   File IO
# Author:    Maryil.H
# Created:   10/04/2017
# ------------------------------------------------------------------------------

#Count the number of times a word appears in the movie file
def count(userWord):           
        #open the movie file
        with open("movieReviews.txt","r") as movies:
                #count the frequency
                number = movies.read().count(userWord)
                #print the word and frequency
                print("Your word, {0} appears {1} times".format(userWord,number))
                                        
#Find the average rating of the word
def average(userWord):
        #initialize an empty list to store the ratings of a word
        ratingList = []
        with open("movieReviews.txt","r") as movies:    
                for line in movies:                        
                        #if the word is in the line place the rating in the list
                        if userWord in line:
                                rating = line[:1]
                                ratingList.append(rating)
                                ratingList = list(map(int,ratingList))
                #return a negative value if the word doesn't exist
                if len(ratingList) == 0:
                        print("There are no occurrences of {} in movies".format(userWord))
                        return -1
                #find the average of the ratings in the ratingList
                else:
                        average = float(sum(ratingList))/float(len(ratingList))                
        #Return the average rating of the word
        return average

#Option to allow the user to enter a personal file or continue with the movie file                
def enter_userInput(userWord):
        if userWord == 'other':
                userFile = input("Enter the name of the file with words you want to score: ")
                userInput(userFile)
        else:
                count(userWord)
                print("The average score for reviews containing the word {0} is {1}".format(userWord,average(userWord)))                
                
#Find which word has the maximum and which has the minimum ratings in the user's file
def userInput(userFile):
        #initialize the dictionary, max and min averages, and actual words
        word_ratings = {}
        max_average = 0
        min_average = 32767
        max_key = ""
        min_key = ""        
        #open the user inputted file
        with open(userFile,"r") as toRate:                
                for word in toRate:
                        #continue if word exists
                        word_average = average(word[:-1])
                        if word_average > 0:
                                #enter the return of the average function into the dictionary with its corresponding word
                                word_ratings[word[:-1]] = average(word[:-1])
                                #calculate the maximum word in the file
                                if word_ratings[word[:-1]] > max_average:
                                        max_average = word_ratings[word[:-1]]
                                        max_key = word[:-1]
                                #calculate the minimum word in the file
                                if word_ratings[word[:-1]] < min_average:
                                        min_average = word_ratings[word[:-1]]
                                        min_key = word[:-1]
        print("The most positive word, with a score of {0} is {1}".format(max_average,max_key))
        print("The most negative word, with a score of {0} is {1}".format(min_average,min_key))
        return
#Function for when the program runs
def main():
        #get the user input
        userWord = input("Please enter a word to search the movie file or type 'other' to scan your own: ")
        #run the user input through the function to check if the user wants to input their own file
        enter_userInput(userWord)
        #put a question within a loop to ask if the user wants to continue with the searching
        while input("Go Again? (yes/no)") == 'yes':
                userWord = input("Please enter a word to search the movie file or type 'other' to scan your own: ")
                enter_userInput(userWord)        

#Run the python program
if __name__ == "__main__":
        main()
        
                