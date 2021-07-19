#! Multiplic
# while True:
#     n = int(input("Valor: "))
#     M = int(input("Multiplicador: "))
#     r = 0
#     l = 1
#     for j in (list(reversed(str(M)))):
#         m = (n*int(j))*l
#         r += m
#         print(m)
#         l *= 10

#     print("-------\n"+str(r))
#     print("\n")
#     pass

# Resto
def new_func():
    M = int(input("Divisor: "))
    return M

def new_func1():
    oo = int(input("Vezes: "))
    return oo

while True:

    M = new_func()
    #// oo = new_func1()
    
    for j in range(0,1):

        n = int(input("Valor: "))

        print()
        print("Divisão:",int(n/M),"...",(n%M))
        # print("Resto:",)

        print("-------\n")
        pass
