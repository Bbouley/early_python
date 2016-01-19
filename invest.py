def invest(amount, rate, time):
  print 'principal amount: $' + str(amount)
  print 'annual rate of return: ' + str(rate)
  for i in range(0, time):
    amount = amount + (amount * rate)
    print 'year ' + str(i+1) + ': $' + str(amount)

invest(100, .05, 8)
