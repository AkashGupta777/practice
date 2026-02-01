a=float(input("ENTER THE NUMBER  A:\n "))
b=float(input("ENTER THE NUMBER  B:\n "))

print("sorry there is limited operator")
print ("enter + for addition ")
print ("enter - for subtraction ")
print ("enter * for multiplication  ")
print ("enter / for division \n")

op=input("enter the operater:")

match op:
    case "+":
        print("RESULT=",a+b)
    case "-":
        print("RESULT=",a-b)
    case "*":
           print("RESULT=",a*b)
    case "/":
            print("RESULT=",a/b)
        
    case "%":
           print("RESULT=",a%b)
    case _ :
            print("THIS IS NOT A VALIDE ")