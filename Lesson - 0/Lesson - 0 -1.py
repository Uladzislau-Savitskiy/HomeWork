input_number = int(input("Enter a three-digit number: "))
number1 = input_number // 100
number2 = input_number // 10 % 10
number3 = input_number % 10
sum = number1 + number2 + number3
print(f"The sum of all digits in the three-digit number {input_number} is equal to:  {sum}")

