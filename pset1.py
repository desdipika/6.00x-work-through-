# Problem 1
#0.0/10.0 points (graded)

#Assume s is a string of lower case characters.

#Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
#For example, if s = 'azcbobobegghakl', your program should print: Number of vowels: 5

vowcount = s.count('a')+s.count('e')+s.count('i')+s.count('o')+s.count('u')
print("Number of vowels: "+str(vowcount))

