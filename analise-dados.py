c = 0
homens = 0
mulher = 0
while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    sexo = ' '
    cont = ' '
    idade = int(input('Idade: '))
    if idade > 18:
        c = c + 1
    while sexo not in 'MmFf':
        sexo = str(input('Sexo: [M/F] ')) .strip() .upper()[0]
        if sexo == 'M':
            homens += 1
        else:
            if idade < 20:
                mulher += 1
        print('-' * 20)
    while cont not in 'SsNn':
        cont = str(input('Quer continuar? [S/N] ')) .strip() .upper()[0]
    if cont == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {c}')
print(f'Ao total temos {homens} homens cadastrados.')
print(f'E temos {mulher} mulheres com menos de 20 anos.')
