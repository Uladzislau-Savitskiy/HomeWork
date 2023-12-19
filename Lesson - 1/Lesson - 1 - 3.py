data = input()
data = data.replace(" ", "")
data = data.lower()
if data[::-1] == data:
  print("palindrome")
else:
  print("not a palindrome")