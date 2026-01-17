#  Crie um programa que  acesse a API  para buscar um usuário fictício aleatório. exibindo o nome, e-mail e país desse usuário, caso houver erro na conexão, mostre uma mensagem de falha.
import requests as req

def obter_user_random():  
     
    try:
        resposta = req.get('https://randomuser.me/api/') 
        resposta.raise_for_status()        
        dados = resposta.json()
        user = dados['results'][0]
        
        nome = f"{user['name']['first']} {user['name']['last']}"
        email = user['email']
        pais = user['location']['country']
        
    except req.RequestException as e:
        return f"Erro ao obter o usuário aleatório: {e}"
    
    return f"Nome: {nome}\nE-mail: {email}\nPaís: {pais}"

print(obter_user_random())