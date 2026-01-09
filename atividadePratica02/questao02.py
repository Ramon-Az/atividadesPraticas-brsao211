# Calculadora de descontos
nome_produto = "Camiseta"
preco_produto = 50.00
percentagem_desconto = 0.20

desconto = preco_produto * percentagem_desconto
preco_final = preco_produto - (desconto)

print(f"Informações da compra: \nProduto: {nome_produto} \nPreço: R${preco_produto:.2f} \nDesconto: {percentagem_desconto * 100:.0f}% é igual a R${desconto:.2f}\nPreço final: R${preco_final:.2f}")