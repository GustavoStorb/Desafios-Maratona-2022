def maximoSubVetor(lista , size):
     
    max_total = lista[0]
    max_atual = lista[0]
     
    for i in range(1 , size):
        max_atual = max(lista[i], max_atual + lista[i])
        max_total = max(max_total,max_atual)
         
    return max_total

lista = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]
print("Maximo :" , maximoSubVetor(lista,len(lista)))
