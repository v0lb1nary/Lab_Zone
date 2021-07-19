# import time

# named_tuple = time.localtime() # get struct_time
# time_string = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)

# print(time_string)

import time

t = (2021, 12, 28, 8, 44, 4, 4, 0, 0)

invent_time = time.mktime(t)
print("Time inventado:", invent_time)

seconds = invent_time #! <-- SEGUNDOS 

# local_time = time.ctime(seconds) #todo :: Tue Dec 28 08:44:04 2021	
# print("Local time:", local_time) 

named_tuple = time.localtime(seconds) # get struct_time
time_start_string = time.strftime("%d/%m/%Y, %H:%M", named_tuple)

print("COMEÇOU EM: ",time_start_string)

x = int(input("Minutos: "))
seconds_add = (x*60)

named_tuple1 = time.localtime((seconds+seconds_add)) # get struct_time
time_end_string = time.strftime("%d/%m/%Y, %H:%M", named_tuple1)

print("TERMINOU EM: ",time_end_string)