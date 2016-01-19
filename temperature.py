def cels_to_fahr (cels):
  return str((cels * 9/5) + 32) + ' degrees F'

def fahr_to_cels (fahr):
  return str((fahr-32)*5/9) + ' degrees C'

print(cels_to_fahr(37))

print(fahr_to_cels(72))
