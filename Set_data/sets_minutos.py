import time

def inputInt(x):
  ''' Loop para o teclado numerico '''
  E = True
  while E:
    try:
      ic = int(input(str(x)+": "))
      if x == "Hora" and ic > 24:
        raise print("Isso não é uma hora possivel")
      elif x == "Minutos" and ic > 59:
        raise print("Isso não é um minuto suportavel")
      else:
        pass
    except Exception:
      pass  
    except ValueError:
      print("Erro de valor, insira apenas números")
    except:
      print("Ocorreu um erro imprevisto")      
    else:
      E = False
  return ic;

while True:
  h = inputInt("Hora")
  m = inputInt("Minutos")

  time_invent = (1970, 1, 1, h, m, 0, 0, 1, 0)

  invent_time = time.mktime(time_invent)
  print("--- Data inventada! ---")

  seconds = invent_time #! <-- SEGUNDOS 
  x = inputInt("Duração")
  seconds_add = (x*60)

  named_tuple = time.localtime(seconds) # get struct_time
  time_start_string = time.strftime("%H:%M", named_tuple)

  named_tuple1 = time.localtime((seconds+seconds_add)) #? Mais duração
  time_end_string = time.strftime("%H:%M", named_tuple1)

  print("COMEÇOU EM:",time_start_string,"às",time_end_string,"\n"+"-"*27,"\n")

