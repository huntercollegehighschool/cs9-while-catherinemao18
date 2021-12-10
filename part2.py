'''
***PART 2***

Write a program that prompts the user to enter a number. The program then prints "Hunter" the number of times the user entered. Use a while loop.

Example of what should appear when the program runs:

Times to print: 3
Hunter
Hunter
Hunter

'''
hunter = int(input("Times to print: "))
tracker = 0 #keeps track of number of times hunter has been printed

while tracker < hunter:
  tracker = tracker + 1
  print("Hunter")