nomes = []

#diferença extend e append.
# append coloca um elemento na lista. 

#nomes.append('Luciano')
#nomes.append('Augusto')
#nomes.extend('Dalton Soares')
#nomes.em
#print(nomes)


nomes = [
    'Italo',
    'Vinicius',
    'Edson',
    'Dalton',
    'Paulo',
    'Nincao'
]

nomes_copia = nomes.copy()
nomes_copia.clear() 



print('nomes', nomes)
print('nomes_copia: ', nomes_copia) #lista está vazia.
print('Index of Edson: ', nomes.index('Edson'))
nomes.insert(3, 'Fabio')
print('Inser pós Fabio: ', nomes)
print('lista popada: ', nomes.pop()) # pop remove o último índice da lista se não passar o índice a ser removido.
print('pós pop', nomes)
print('lista popada (index 2): ', nomes.pop(2))
print('pós lista popada (index 2): ', nomes)
nomes.remove('Italo')
print('pós remove Italo', nomes)
nomes.reverse()
print('pós reverse', nomes)

