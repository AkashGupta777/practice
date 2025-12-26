#Write a program to find the largest of three numbers.

number1,number2,number3=list(map (int,input( "ENTER THE NUMBER THAT YOU WANT =").split()))
if (number1>number2 and number1 >number3):
   print("number1 is largest",number1)
elif number2 > number3 :  
   print("number2 is greater",number2)
else:
   print("number3 is greater",number3)
