import math
figure = input('Enter the figure whose area you want to find: ')
circul = 'circle'
triangle = 'triangle'
rectangle = 'rectangle'
if figure.lower() == circul:
  num = int(input('Enter the radius of the circle: '))
  print('The area of a circle is: ', (3.14 * num ** 2))
elif figure.lower() == triangle:
  num1 = int(input('Enter the length of line a of the triangle: '))
  num2 = int(input('Enter the length of line b of the triangle: '))
  num3 = int(input('Enter the angle between the sides: '))
  print('The area of a triangle is: ', (0.5 * num1 * num2 * math.sin(math.radians(num3))))
elif figure.lower() == rectangle:
  num1 = int(input('Enter the length of line a of the rectangle: '))
  num2 = int(input('Enter the length of line b of the rectangle: '))
  print('The area of a rectangle is: ', (num2 * num1))
else:
  print("Error. Incorrect input.")
  