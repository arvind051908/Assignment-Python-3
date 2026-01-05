# Task 1: Calculate Factorial Using a Function 
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

num = int(input("Enter a number: "))
result = factorial(num)
print(f"The factorial of {num} is : {result}")
 