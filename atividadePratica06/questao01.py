'''Crie um programa que gere senhas aleatórias com letras, números e símbolos e que o usuário  também escolha o tamanho da senha  para criar senhas seguras automaticamente.'''
import random
import string

def gerar_senha(tamanho):
    char = string.ascii_letters + string.digits + "@!#$%&"
    senha = ''.join(random.choice(char) for _ in range(tamanho))
    return senha

tamanho = int(input("Digite o tamanho da senha: "))
senha = gerar_senha(tamanho)

print(f"Senha: {senha}")