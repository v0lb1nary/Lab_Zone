
# CRIADA
def max_linhas_colunas(matriz, i, j):
    if i >= len(matriz) or j >= len(matriz[i]):
        return False
    else:
        return True

# Função 5 (10 pontos): get_pos_vertical()
def get_pos_vertical(matriz, tam):
    possbl = ()
    for i in range(0,len(matriz)):
        for j in range(0, len(matriz[i])):      
            for h in range(0, tam):
                if h != tam-1:
                    if tem_agua(matriz, (i+h), j):
                        pass
                    else:
                        break
                else:
                    if tem_agua(matriz, (i+h), j):
                        possbl += (i,j),
                    else:
                        pass

    return possbl

# Função 4 (10 pontos): get_pos_horizontal()
def get_pos_horizontal(matriz, tam):
    possbl = ()
    for i in range(0,len(matriz)):
        for j in range(0, len(matriz[i])):      
            for h in range(0, tam):
                if h != tam-1:
                    if tem_agua(matriz, i, (j+h)):
                        pass
                    else:
                        break
                else:
                    if tem_agua(matriz, i, (j+h)):
                        possbl += (i,j),

    return possbl

# Função 3 (8 pontos): tem_navio()
def tem_navio(matriz, i, j):
    if max_linhas_colunas(matriz, i, j):
        if matriz[i][j] != "N":
            return False
        else:
            return True
    else:
        return False

# Função 2 (8 pontos): tem_agua()
def tem_agua(matriz, i, j):
    if max_linhas_colunas(matriz, i, j):
        if matriz[i][j] != 0:
            return False
        else:
            return True
    else:
        return False

# Função 1 (10 pontos): cria_tabuleiro()
def cria_tabuleiro(char):
    return ((char,)*10,)*10
 
 
# print_matriz()
def print_matriz(matriz):
    for i in range(0,len(matriz)):
        for j in range(0, len(matriz[i])):
            print(matriz[i][j], end=" ")
        print()

#tabi = cria_tabuleiro(0)

fake_tab = [[0, 0, 'N', 0, 0, 0, 0],
            [0, 0, 'N', 0, 0, 'N', 0],
            [0, 0, 'N', 0, 0, 0, 0],
            [0, 0, 'N', 0, 'N', 'N', 0],
            [0, 0, 0, 0, 0, 0, 0]]

print(len(fake_tab), len(fake_tab[0]))

print_matriz(fake_tab)
print("Horizontal: ",get_pos_horizontal(fake_tab, 3))
print("Vertical: ",get_pos_vertical(fake_tab, 3))





