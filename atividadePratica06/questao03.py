# Crie um programa que consulte informações de um  na API , retorne logradouro, bairro, cidade e estado do CEP digitado, caso o CEP não existir ou houver erro na requisição, mostre uma mensagem de falha.
import requests as req

def endereco(cep):
    
    try:
        resposta = req.get(f'https://viacep.com.br/ws/{cep}/json/')
        resposta.raise_for_status()
        dados = resposta.json()
        
        if 'erro' in dados:
            return "CEP inválido."
        
        return f"Logradouro: {dados['logradouro']}\nBairro: {dados['bairro']}\nCidade: {dados['localidade']}\nEstado: {dados['uf']}"
        
    except req.RequestException as e:
        return f"Erro ao obter o usuário aleatório: {e}"

cep = input("Digite o CEP: ")

print(endereco(cep))
