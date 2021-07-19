
#! MINIMO MULTIPLO COMUM

def maior_menor(i,j):
  return i if i > j else j

x = 4
y = 10
lol = ()

while x > 1 or y > 1:
  w = maior_menor(x,y)
  for i in range(2,w+1):
    # print("contado:",i," x:",x," y:",y," i:",i)
    if x % i == 0 and y % i == 0:
      lol += i,
      x = int(x/i)
      y = int(y/i)
      break

    elif x % i == 0 or y % i == 0:
      if x % i == 0:
        lol += i,
        x = int(x/i)
        break

      if y % i == 0:
        lol += i,
        y = int(y/i)
        break

    else:
      pass

    pass
  pass

print(lol)

result = 1
for i in lol:
  result *= i

print(result)
      