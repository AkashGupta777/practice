
#                                        EVEN NUMBER
start,end =map(int,input("ENTER THE NUMBER FROM WHERE YOU WANT TO START AND WHERE YOU WANT TO STOP \n").split())
print( "staring from",start ,"ending with ", end)
for i in range(start ,end):
        if i%2==0:
         print(i)