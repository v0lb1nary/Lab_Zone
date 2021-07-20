
def Simplif(x):
   ''' Encontra os divisores de um numero ("x") '''
   listaLimpa = ()
   lista = list(range(1,x+1)) 
   for j in lista:
         listaLimpa += ((),(j,))[x%j == 0]
         pass
   return listaLimpa

def fun_MDC(lst1,lst2):
  ''' Encontra do "Maior Divisor Comum" entre duas listas '''
  lstMDC = ()
  for j in lst1:
      lstMDC += ((),(j,))[j in lst2]
      pass
  return {1: (lstMDC[-1:]), 2: lstMDC[1:]}

def Conta(FragList1, FragList2):
  ''' Calcula e escreve o resultado da Simplicação junto ao seu MDC '''
  fract = SomaFracoes(FragList1, FragList2)

  #$ FRAÇÃO
  if not fract[2] == 0: 
    MDC = (fun_MDC(Simplif(fract[1]),Simplif(fract[2])))
    print(fract[3],end=" :: ")
    print("["+str(MDC[1][0])+"]",end=" ==> ") 
    print("Result:",fract[0],"("+str(int(fract[1]/(MDC[1][0])))+"/"+str(int(fract[2]/(MDC[1][0])))+")\n") 
    #? ^ RESULTADO ^

  #$ INTEIRO
  else: 
    print(fract[3],end=" = ")
    print("Result:",fract[0],"\n") 
    #? ^ RESULTADO ^

  #// Type = int(input("Tipo da saida: "))
  
def inputInt(x):
  ''' Loop para o teclado numerico '''
  E = True
  while E:
    try:
      ic = int(input(str(x)+": "))
    except ValueError:
      print("Erro de valor, insira apenas números")
    except:
      print("Ocorreu um erro imprevisto")
    else:
      E = False
  return ic;

def SomaFracoes(FragList1, FragList2):
   nN = FragList1[0] + FragList2[0]
   n1 = FragList1[1] + FragList2[1]
   n2 = FragList1[2] #! DENOMINADORES DIFERENTES

   print("("+str(FragList1[0])+")",str(FragList1[1])+"/"+str(FragList1[2]),end=" + ")
   print("("+str(FragList2[0])+")",str(FragList2[1])+"/"+str(FragList1[2]),end=" >> ")
   print(nN,str(n1)+"/"+str(n2), end=" == ")

   return ReducaoNumerador(nN, n1, n2)

def ReducaoNumerador(nN,n1,n2):
  while n1>n2 or n1 == n2 and n1 != 0:
    if n1>n2:
      n1 -= n2
      nN += 1
      pass
    elif n1 == n2:
      n1 = 0
      n2 = 0
      nN += 1 
    
  else:
    return {0:nN, 1:n1, 2:n2, 3:"("+str(nN)+") "+str(n1)+"/"+str(n2)}

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

def Divisor(x,j):
  for i in range(1,j):
    if x*i == j:
      return (i)
      pass
    else:
      pass
  
def AdaptedeFracao(f1,f2):
  var = MMD(f1[2],f2[2])
  f1[1] *= Divisor(f1[2],var)
  f2[1] *= Divisor(f2[2],var)
  f1[2] = var



while True:
  
  f1 = []
  f2 = []

  f1 += inputInt("Isira o valor do inteiro (1°)"),
  f1 += inputInt("Isira o valor do numerador (1°)"),
  f1 += inputInt("Isira o valor denominador (1°)"),

  while f1[2] == 0:
    print("'0' não pode ser um denominador")
    f1[2] = inputInt("Isira o valor denominador (1°)")
    pass

  f2 += inputInt("Isira um valor do inteiro (2°)"),
  f2 += inputInt("Isira um valor do numerador (2°)"),
  f2 += inputInt("Isira o valor denominador (2°)"),

  while f2[2] == 0:
    print("'0' não pode ser um denominador")
    f2[2] = inputInt("Isira o valor denominador (2°)")
    pass
  
  if f1[2] != f2[2]:
    AdaptedeFracao(f1,f2)
  
  Conta(f1,f2)
