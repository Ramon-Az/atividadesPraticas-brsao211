# Crie um programa que calcule a quantos dias um individuo está vivo de acordo com a data do dia
import datetime

def calcular_idade(data_nascimento):
    ano_atual = datetime.datetime.now().year
    idade = ano_atual - data_nascimento
    return idade * 365

data_nascimento = int(input("Informe o ano de nascimento: "))

dias_vivo = calcular_idade(data_nascimento)

print(f"Você está vivo há {dias_vivo} dias")