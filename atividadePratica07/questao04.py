import json

def ler_arquivo_json(nome_arq):
    try:
        with open(f"./data/{nome_arq}", "r", encoding="utf-8") as arq_json:
            dados_json = json.load(arq_json)
            return dados_json
        
    except FileNotFoundError:
        print("Arquivo, {nome_arq}, não encontrado!")
        
def escrever_arq_json(nome_arq, dados):
    try:
        with open(nome_arq, 'w', encoding="utf-8") as arq_json:
            json.dump(dados, arq_json, ensure_ascii=False, indent=4)
            return f"Arquivo {nome_arq} criado com sucesso!"
        
    except Exception as e:
        return f"Erro aos escrever no arquivo: {e}"
    
dados = {
    "nome": "João",
    "idade": 25,
    "cidade": "São Paulo"
}

nome = input("Digite o nome do arquivo: " )
print(escrever_arq_json(f"./data/{nome}.json", dados))

print(ler_arquivo_json(f"{nome}.json"))

