# Crie um programa que realize consultas a  em relação ao Real (BRL) usando a API mostre valor atual, máxima, mínima e data/hora da última atualização, caso a moeda não existir ou houver erro na requisição, retorne uma mensagem de erro.
import requests as req

def consultar_moeda(moeda_destino):
    try:
        resposta = req.get(f'https://economia.awesomeapi.com.br/last/{moeda_destino}-BRL')
        resposta.raise_for_status()
        dados = resposta.json()[f"{moeda_destino.upper()}BRL"]
        
        cotacao = float(dados['bid'])
        alta =  float(dados['high'])
        baixa = float(dados['low'])
        data = dados["create_date"]       
        
        return f"Cotação: R${cotacao:.2f}\nMáxima: R${alta:.2f}\nMínima: R${baixa:.2f}\nData/Hora: {data}"
        
    except req.RequestException as e:
        return f"Erro ao obter o usuário aleatório: {e}"
    
moeda_destino = input("Digite o código da moeda de destino (ex: USD, EUR, GBP): ")

print(consultar_moeda(moeda_destino))
