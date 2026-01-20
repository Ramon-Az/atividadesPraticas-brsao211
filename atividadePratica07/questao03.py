# Crie um programa que leia um arquivo  informado pelo usuário, percorrendo cada linha do arquivo e a exibe na tela, caso o arquivo não seja encontrado, mostre uma mensagem de erro.
import csv

def ler_arq(nome_arq):
    try:
        with open(f"./data/{nome_arq}", 'r',  encoding="utf-8") as arquivo:
            for linha in arquivo:
                print(linha.strip())
              
    except FileNotFoundError:
        print(f"Arquivo não encontrado")

nome_arquivo = input("Digite o nome do arquivo: ")
ler_arq(nome_arquivo) 
