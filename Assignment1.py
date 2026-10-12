n=0
# n=int(input("1 for CHECK BALANCE  ,2 for DEPOSIT MONEY  , 3 for WITHDRAW MONEY   , 4.EXIT:"))
bal=10000
while n!=4:
    n=int(input("1 for CHECK BALANCE  ,2 for DEPOSIT MONEY  , 3 for WITHDRAW MONEY   , 4.EXIT:"))
    if n==1:
        print("CURRENT BALANCE:",bal)
    elif n==2:
        depo=int(input("enter the amount to deposit:"))
        bal+=depo
        print("amount deposited sucessfull")
        print("total available balance is:",bal)
    elif n==3:

        withdraw=int(input("enter the amount to withdraw:"))
        if withdraw<=bal and withdraw%100==0:
            bal-=withdraw
            print("Transaction sucessfull")
        else:
            print("insufficiant balance or invalid amount")
    else:
        exit

#         1. Create and Write a File
# Create a file named student.txt and write the following information:
# Name: Akhil
# Age: 25
# Course: bca

# Use open() and the write() method.
# 2. Read a File
# Create a file called welcome.txt containing:
# Welcome to Python Programming

# Write a program to read and display its contents.
# 3. Read Line by Line
# Create a file names.txt containing 5 student names.
# Write a program to read and display each name line by line.
# 4. Count Lines
# Create a file data.txt containing multiple lines.
# Write a program to count the number of lines in the file.
# Example output:
# Number of lines: 5

# 5. Count Words
# Read a file and count the total number of words.
# Example:
# sample.txt
# Python is easy to learn
# Python is powerful

# Output:
# Total words: 7

# 6. Count Characters
# Write a program to count the total number of characters in a file.
# 7. Append Data
# Create students.txt and write three student names.
# Then ask the user for another name and append it to the file.
# 8. Display File Contents
# Ask the user to enter a filename.
# Enter filename: notes.txt

# Display the contents of that file.
# 9. Check Whether File Exists
# Write a program that checks whether student.txt exists.
# Output:
# File exists

# or
# File does not exist

# 10. Copy File Contents
# Read the contents of source.txt and copy them into destination.txt.