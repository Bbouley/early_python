def square(number):
  sqr_num = number ** 2
  return sqr_num

input_num = 5
output_num = square(input_num)

print(output_num)


def return_difference(num1, num2):
  if num1 > num2:
    return num1 - num2
  else:
    return num2-num1

print(return_difference(3,5))

def cube(num):
  return num * num * num

print(cube(3))

def multiply(num1, num2):
  return num1 * num2

print(multiply(2,4))
