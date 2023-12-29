word = 'cat'
chars = 'atach'

H = {}
for c in chars:
  if c in H:
    H[c] -= 1
  else:
    H[c] = 1
  print(c, H)