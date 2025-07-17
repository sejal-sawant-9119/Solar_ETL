def divide(a,b):
	try:
		return a/b
	except ZeroDivisionError:
		print("Oops! You can't divide by zero.")

print(divide(10,2))
print(divide(10,0))
