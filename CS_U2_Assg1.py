#ICS4U Unit 2 Assignment 1: Date Validation
#By: Hanan Maryil
#------------------------------------------

#Fill this while loop with restrictions to the user's date entry
while True:
 #get the user's input
 user_input = input("Please enter your Date of Birth in the format MM/DD/YYYY(include the slashes) or type 'quit' to end: ")
 if user_input.lower() == 'quit':
  print("Au Revoir!")
  break
 #set month, day, and year as individual string variables
 month = user_input[0:2]
 day = user_input[3:5]
 year = user_input[6:10]
 #variables for months with 30 days and 31 days respectively
 month_30 = set(['09','04','06','11'])
 month_31 = set(['01','03','05','07','08','10','12']) 
 #make sure that the length of the date is correct, purely by number of characters
 if len(user_input)!=10:
  print("Seriously? Why are you trying to break my program? That is invalid!")
  continue 
 #check it the characters inputted are integers (digits)
 if month.isdigit()==False or day.isdigit()==False or year.isdigit()==False:
  print("That's an invalid date, mon amie!")
  continue
 #If they are digits, then convert them to integers
 else:
  month = int(user_input[0:2])
  day = int(user_input[3:5])
  year = int(user_input[6:10])  
 #Check it the user has inputted slashes in the appropriate places
 if ('/' not in user_input[2]) or ('/' not in user_input[5]):
  print("*fail* Umm...so you forgot the slash(es)...Your date is invalid")
  continue
 #check if the month is valid
 if month > 12 or month == 0:
  print("Do you know how many months are in a year? Your date is invalid")
  continue
 #check if the day and year is valid
 if day >= 32 or day == 00 or year > 2017:
  print("How were you born then? IMPOSSIBLE! Date is invalid")
  continue
 #convert the month back to a string
 else:
  month = user_input[0:2]
 #If it is a 30-day month, check if the number of days exceed the limit, 30
 if month in month_30:
  if day > 30:
   print("There aren't that many days in that month. Date is invalid.")   
  continue
 #If the month is February:
 if month == '02':
  #If the year is a leap year:
  if year % 400 == 0 or year % 4 == 0:
   if day > 29:
    print("I don't think so! That date is invalid.")
    continue
  #If the year is not a leap year:
  if year % 100 == 0:
   if day > 28:
    print("For real? That date is invalid.")
    continue
  else:
   continue
  
 #Reply if everything is good and valid
 else:
  print("Valid! That's a great birthday :)")
  continue
   
 

 