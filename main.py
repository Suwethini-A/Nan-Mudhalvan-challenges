#find factorial number python program

def factorial(number):
  if number == 0:
    return 1
  else:
    return number * factorial(number - 1)

number = int(input("Enter any number : "))
result = factorial(number)
print(f"\nThe Factorial of {number} is {result}")
