# A branching program to see if an int is even or odd
x = int(input("Enter a number: "))
if x%2 == 0:
  print("x is even")
else:
  print("x is odd")
print("Done with conditional") 

# A nested conditional program to see if an int is divisible by 2 and 3
if x%2 == 0:
	if x%3 == 0:
		print("x is divisible by 2 and 3")
	else:
		print("x is divisible by 2 and not 3")
elif x%3 == 0:
	print("x is divisible by 3 and not 2")
else:
	print("x not divisible by 2 and 3")
print("Done with nested conditional")



  
  
 
