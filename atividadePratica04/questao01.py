# Calculadora com operações básicas
while True:

    try:
        
        numero_1 = float(input('Digite o primeiro número: '))
        numero_2 = float(input('Digite o segundo número: '))
        operacao = input(
        '+ ---> Adição\n' \
        '- ---> Subtração \n' \
        '* ---> Multiplicação\n' \
        '/ ---> Divisão\n'
        'Digite a operação desejada: ').upper
                
        if operacao == '+':
            print(f'{numero_1} + {numero_2} = {numero_1 + numero_2}')
            break
        elif operacao == '-':
            print(f'{numero_1} - {numero_2} = {numero_1 - numero_2}')
            break
        elif operacao == '*':
            print(f'{numero_1} * {numero_2} = {numero_1 * numero_2}')
            break
        elif operacao == '/':
            print(f'{numero_1} / {numero_2} = {numero_1 / numero_2}')
            break
        else:
            raise Exception()

    except ValueError:
        print('Digite os dados corretamente')
    
    except ZeroDivisionError:
        print('Não é possível dividir por zero')
        
    except KeyboardInterrupt:
        print('Saindo...')
        break
    
    except Exception:
        print('Operação inválida')