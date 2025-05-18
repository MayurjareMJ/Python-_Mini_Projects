# Simple calulator in python

# Three steps to build calculator program

# 1.Fuction for program
# 2. User input
# 3. Print result

# Function to add two number
print(25*"=")
print("Welcome to calculator")
print(25*"=")
def add(num1,num2):
    return num1+num2

# Function to substract two number
def sub(num1,num2):
    return num1-num2

# Functoin to multiplication of two number
def mult(num1,num2):
    return num1*num2

# Functoin to Division of two number
def div(num1,num2):
    return num1/num2

# Functoin to Average of two number
def avg(num1,num2):
    return (num1+num2)/2

#User Input
select=int(input("Enter the operation want to perform.\n"\
                 "_________________________________________\n"
                 "1.Addation\n"
                 "2.Substraction\n"
                 "3.Multiplication\n"
                 "4.Division\n"
                 "5.Average\n"
                 "Please Enter : "))
num1=int(input("Enter the first number : "))
num2=int(input("Enter the second number : "))

if select==1:
    print(num1,"+",num2,"=",add(num1,num2))

elif select==2:
    print(num1,"-",num2,"=",sub(num1,num2))

elif select==3:
    print(num1,"*",num2,"=",mult(num1,num2))

elif select==4:
    print(num1,"+",num2,"=",div(num1,num2))

elif select==5:
    print(num1,"+",num2,"=",avg(num1,num2))
else:
    print("Please Entre valid operator from 1,2,3,4,5")
