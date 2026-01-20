# Crie um programa que cria um arquivo  com nome, idade e cidade de algumas pessoas, que este programa escreva os dados em formato tabular e salva no arquivo escolhido pelo usuário, caso ocorra um erro ao salvar, mostre uma mensagem de falha.
import csv

def escrever_dados(nome_arq, dados):
    try:
        with open(f"./data/{nome_arq}", "w", newline="", encoding="utf-8") as arq:
            escritor = csv.writer(arq)
            escritor.writerow(["Nome", "Idade", "Cidade"])
            for linha in dados:
                escritor.writerow(linha)
        return "Dados escritos com sucesso!"
    
    except Exception as e:
        return f"Falha ao escrever os dados: {e}"
    
dados = [
    ["João", "26", "São Paulo"],
    ["Maria", "30", "Rio de Janeiro"],
    ["Pedro", "22", "Belo Horizonte"]
]

nome_arquivo = input("Digite o nome do arquivo: ")
print(escrever_dados(nome_arquivo, dados))