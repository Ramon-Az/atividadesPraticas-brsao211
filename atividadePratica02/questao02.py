# Calculadora de descontos
nome_produto = "Camiseta"
preco_produto = 50.00
percentagem_desconto = 0.20

preco_final = preco_produto - (preco_produto * percentagem_desconto)

print(f"Informações da compra: \nProduto: {nome_produto} \nPreço: R${preco_produto:.2f} \nDesconto: {percentagem_desconto * 100:.0f}% \nPreço final: R${preco_final:.2f}")