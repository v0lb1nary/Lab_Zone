
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
   
  #f2 += inputInt("Isira um valor denominador (2°)"), #! DENOMINADORES DIFERENTES
  
    Conta(f1,f2)