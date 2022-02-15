#criando uma lista de números

numerosLista = []
minimo = 0
maximo  = 10.0
passo = 2
valor = minimo
#maximo_ = maximo + passo

while valor <= maximo:
    numerosLista.append(valor)
    valor = valor + passo
    
print(numerosLista)
    
