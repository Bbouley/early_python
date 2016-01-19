def while_loop():
  n = 1
  while(n < 5):
    print 'n = ' + str(n)
    n = n + 1
  print('loop is done')

# while_loop()

def for_loop():
  for i in range(1, 5):
    print 'i = ' + str(i)
  print('loop is done')

# for_loop()

def loops_in_loops():
  for n in range(0,5):
    for j in ['a', 'b', 'c']:
      print 'n = ' + str(n) + ' j = ' + j
  print('loop is done')

# loops_in_loops()

def review_1():
  for n in range(2, 11):
    print n

# review_1()

def review_2():
  n = 2
  while(n<11):
    print n
    n = n+1

# review_2()

def doubles(num):
  for n in range(0,3):
    num = num * 2
    print (num)

doubles(2)

