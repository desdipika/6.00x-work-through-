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

# A conditional to compare ints and print the least
y = int(input("Enter another number: "))
z = int(input("Enter one more: "))
if x<y and x<z:
	print("x is the least")
elif y<z:
	print("y is the least")
else:
	print("z is the least")
# A conditional to compare ints and print the greatest
if x>y and x>z:
	print("x is the greatest")
elif y>z:
	print("y is the greatest")
else:
	print("z is the greatest")
print("Done with comparison")


  
  
 
