#------Start-----------
# This program prints Hello, world!
print('Hello, world!')
#------End-------------

#------Start-----------
#This program adds two numbers
num1 = 1
num2 = 7
# Add two numbers
sum = num1 + num2
# Display the sum
print(sum)
#------End-------------

#------Start-----------
#This program is to find the square
num	= 2
sq = num*num
print(“Square is: ”, sq)
#------End-------------

#------Start-----------
#This program is to find the square root
num	=  16
sq_rt = num**(1/2)
print(“Square root is: ”,sq_rt)
#------End-------------

#------Start-----------
#This program is to find the square root of a user-entered number
# To take the input from the user
num = float(input('Enter a number: '))
num_sqrt = num ** 0.5
print(“The sqrt is: ”, num_sqrt)
# If you need precision after decimal points, then use the statement below.
#print('The square root of %0.3f is %0.3f'%(num ,num_sqrt))
#------End-------------

#------Start-----------
#This program is to find the area of a square/rectangle with user-entered values
l = float(input('Enter a length: '))
h= float(input('Enter a height: '))
area = l*h
print('The area of the rectangle with length and heightis:: %0.5f' %area)
#------End-------------

#------Start-----------
#This program is to find if the entered number is odd or even
# A number is even if division by 2 gives a remainder of 0.
# If the remainder is 1, it is an odd number.

num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))
#------End-------------
