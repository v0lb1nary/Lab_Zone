
#! MINIMO MULTIPLO COMUM

def maior_menor(i,j):
  return i if i > j else j

def MMD(n1,n2):
  """ Retorna o Minino Multiplo Comum de 2 numeros """
  
  list_MMD = ()
  while n1 > 1 or n2 > 1:
    w = maior_menor(n1,n2)
    for i in range(2,w+1):
      # print("contado:",i," x:",x," y:",y," i:",i)
      if n1 % i == 0 and n2 % i == 0:
        list_MMD += i,
        n1 = int(n1/i)
        n2 = int(n2/i)
        break

      elif n1 % i == 0 or n2 % i == 0:
        if n1 % i == 0:
          list_MMD += i,
          n1 = int(n1/i)
          break

        if n2 % i == 0:
          list_MMD += i,
          n2 = int(n2/i)
          break

      else:
        pass

      pass
    pass

  result = 1
  for i in list_MMD:
    result *= i

  return(result)

while True:
  x = int(input("N1: "))
  y = int(input("N2: "))

  print(MMD(x,y))
        