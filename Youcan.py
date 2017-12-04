#
import random

print("Let's Play Guessing Number Game")
a=int(raw_input("Select your range's Start Number:"))
b=int(raw_input("Select your range's Last Number:"))
#p#rint(a)
#print(b)

x = random.randint(a,b)
#print(x)
#y=range(a,b)
#print(y)
atp=3	
while atp>0:
    y=int(raw_input("Guess and Enter any Number in your selected range:"))
    atp-=1 
    if y!=x:
        print ("Sorry Try again, you have %d chance left" %(atp))
    else : #y==x:
        print("congratulation you got it")    
        atp=0        
    #else:
  	    #print("Game Over")
    
print"Game Over"
	#print ("Sorry Try again you have %d left" % (atp))
	#y=int(raw_input("Enter Number:"))

#if y == x: 
	#print"congratulation"
	
#else:
	#print('Game Over')



#(y!=x):
#	print ('Sorry Game Over')

	#	print(atp-1)






