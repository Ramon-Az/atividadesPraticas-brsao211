# Idade e classificar as idades

try:
    idade = int(input("Digite a idade: "))
    
    if idade < 0:
        print("Idade não pode ser negativa")
    elif idade <= 12:
        print("Criança")
    elif idade > 12 and idade <= 17:
        print("Adolescente") 
    elif idade > 17 and idade <= 59:
        print("Adulto")
    elif idade <=150:
        print("Idoso")
    else:
        print("Pode ser que você esteja mentido a sua idade!")
    
except ValueError:
    print("Idade inválida")
