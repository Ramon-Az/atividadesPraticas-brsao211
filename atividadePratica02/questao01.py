# converte valores de R$ para $ e €

valor_em_real = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

valor_convertido_dolar = valor_em_real / taxa_dolar
valor_convertido_euro = valor_em_real / taxa_euro

print(f"O valor em real é R${valor_em_real:.2f} \nO valor convertido em dolar é ${valor_convertido_dolar:.2f} \nO valor convertido em euro é €{valor_convertido_euro:.2f}")