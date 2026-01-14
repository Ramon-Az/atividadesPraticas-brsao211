# Criar um código que serve para analisar números digitados pelo usuário, classificando-os como pares ou ímpares e contabilizando quantos de cada tipo foram inseridos.

par = 0
impar = 0

while True:
    try:
        
        entrada = input("Digite um número inteiro ou 'fim' para SAIR: ")
        
        if entrada.lower() == 'fim':
            print("Encerrando o programa.")
            break
        
        num = int(entrada)
        
        if num % 2 == 0:
            print(f'{num} é par.')
            par += 1
        else:
            print(f'{num} é ímpar.')
            impar += 1
    
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")

print(f'Você digitou {par} número pare e {impar} número ímpar.')