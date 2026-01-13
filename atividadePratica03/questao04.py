# Ano bissexto
# Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não.
# Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400.

try:
    ano_atual = int(input('Digite o ano atual: '))

    ano_bissexto = ano_atual % 4 == 0 and ano_atual % 100 != 0 or ano_atual % 400 == 0

    if ano_bissexto == True:
        resultado = 'Sim'
        print(f'O ano {ano_atual} é bissexto? {resultado}')
    else:
        resultado = 'Não'
        print(f'O ano {ano_atual} é bissexto? {resultado}')

except ValueError:
    print('Valores de entrada, inválidos!')