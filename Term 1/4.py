a = int(input('Enter the First Side of a Triangle: '))
b = int(input('Enter the Second Side of a Triangle: '))
c = int(input('Enter the Third Side of a Triangle: '))
if a == b == c:
	print("Equilateral triangle")
elif a==b or b==c or c==a:
	print("isosceles triangle")
else:
	print("Scalene triangle")

