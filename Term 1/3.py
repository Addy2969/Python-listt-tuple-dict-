a = int(input('Enter the First Side of a Triangle: '))
b = int(input('Enter the Second Side of a Triangle: '))
c = int(input('Enter the Third Side of a Triangle: '))
if a+b>=c and b+c>=a and c+a>=b:
    print("This is a Valid Triangle")
else:
    print("This is an Invalid Triangle")
