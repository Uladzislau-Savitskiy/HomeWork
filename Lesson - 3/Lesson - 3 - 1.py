number_input = int(input())
def number_factorial(number):
  factorial = 1
  for i in range(1, number + 1):
    factorial *= i
  return factorial
print(number_factorial(number_input))
