# Crie um programa que lê um arquivo CSV com a biblioteca pandas, calcule e exiba a média e o desvio padrão da coluna tempo_execucao
import pandas as pd

def processar_logs(arq_log):
    try:
        leitor = pd.read_csv(f"./data/{arq_log}")
        media = leitor['tempo_execucao'].mean()
        desvio_padrao = leitor['tempo_execucao'].std()
        return f"Média: {media:.2f}, Desvio padrão: {desvio_padrao:.2f}"
    
    except FileNotFoundError:
        return "Erro: Arquivo não encontrado"
    except KeyError:
        return "Erro: Coluna 'tempo_execucao' não encontrada no arquivo"
    except Exception as e:
        return f"Erro na leitura do arquivo: {e}"

dados = input("Digite o nome do arquivo de log: ")
print(processar_logs(dados))
