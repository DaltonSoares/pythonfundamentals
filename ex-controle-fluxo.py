ano_nascimento = int(input('Digite seu ano de nascimento: '))

if ano_nascimento <= 1964:
    print('Baby Boomer')
elif ano_nascimento >= 1965 and ano_nascimento <= 1979:
    print('Geração X')
elif ano_nascimento >= 1980 and ano_nascimento <= 1994:
    print('Geração Y')
else:
    print('Geração atual')