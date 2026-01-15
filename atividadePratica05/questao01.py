# Crie uma função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de gorjeta desejada. Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.
# Parâmetros:
# a - valor_conta (float): O valor total da conta
# b - porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 10 para 10%)
# c - retorna: float: O valor da gorjeta calculada

def gorgeta(conta, porcentagem):
    return conta * (porcentagem / 100)

valor_conta = float(input("Informe o valor total da conta: "))
porcentagem_gorjeta = float(input("Informe a porcentagem da gorjeta (10 para 10%): "))

valor_gorjeta = gorgeta(valor_conta, porcentagem_gorjeta)

print(f"O valor da gorgeta é de R$ {valor_gorjeta:.2f}")