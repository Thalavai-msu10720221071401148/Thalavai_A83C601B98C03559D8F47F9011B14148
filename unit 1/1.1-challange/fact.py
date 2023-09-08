"""1.1-Implement a recursive function to calculte the 
factorial of a given number"""

def fact(n):
	if n==0:
		return 1
	else:
		return n*fact(n-1)
n=int(input("Enter the number:"))
result=fact(n)
print("The factorial of {} is {} :".format(n,result))		


		