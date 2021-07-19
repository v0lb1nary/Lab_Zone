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
  return {1: lstMDC[-1:], 2: lstMDC[1:]}

def Conta(n1,n2):
  ''' Calcula e escreve o resultado da Simplicação junto ao seu MDC '''
  MDC = (fun_MDC(Simplif(n1),Simplif(n2)))
  print(int(n1/(MDC[1][0])),"/",int(n2/(MDC[1][0])),end=" --> ")
  #// Type = int(input("Tipo da saida: "))
  print(list(MDC[1]),"\n") #? <-- RESULTADO 

def inputInt(x):
  ''' Loop para o teclado numerico '''
  E = True
  while E:
    try:
      i = int(input(x))
    except ValueError:
      print("Erro de valor, insira apenas números")
    except:
      print("Ocorreu um erro imprevisto")
    else:
      E = False
  return i;

while True:
  nC = inputInt("Isira o numerador: ")
  nB = inputInt("Insira o denominador: ")

  Conta(nC,nB)