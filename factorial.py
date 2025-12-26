# Write a program to calculate the factorial of a number.

number =int(input("enter the number"))
fact=1
for i in range (1,number+1):
 fact= fact * i 
print("the factorial is",fact)
