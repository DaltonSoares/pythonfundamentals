quitanda = [
'Banana',
'Melancia',
'Morango'
]

cesta = {}

while True:
    print('-' * 10)
    print('Bem-vindo à quitanda Pythera')
    print('1: Ver Cesta')
    print('2: Adicionar frutas')
    print('3: Sair')

    if entrada == 1:
        print(cesta)
    
    elif entrada == 2:
        while True:
            for (i, fruta) in  enumerate(quitanda):
                print(f"{i}: {fruta}")
            print('-1: Sair')
        
            entrada = int(input('Digite a fruta/opção desejada:'))

            if entrada == -1:
                break

            