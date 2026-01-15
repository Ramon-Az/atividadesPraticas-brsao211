'''Crie um programa que serve para calcular o preço final de um produto após aplicar um desconto percentual.
a - Cálculo de desconto: Calcula o valor do desconto baseado em uma porcentagem.
b - Preço final: Determina o novo preço após o desconto.
c - Formatação: Arredonda o resultado para 2 casas decimais (centavos).
d - Interação com usuário: Pede os valores necessários e mostra o resultado formatado'''

def desconto(preco, porcentagem):
    return preco * (porcentagem / 100)

def preco_final(preco, desconto):
    return preco - desconto

preco_produto = float(input("Informe o preço do produto: "))
porcentagem_desconto = float(input("Informe a porcentagem de desconto: "))

valor_desconto = desconto(preco_produto, porcentagem_desconto)
preco_com_desconto = preco_final(preco_produto, valor_desconto)
preco_formatado = round(preco_com_desconto, 2)

print(f"O preço final do produto é de R$ {preco_formatado:.2f}")
