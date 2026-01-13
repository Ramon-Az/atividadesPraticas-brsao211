# Conversor de temperatura
# Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
# O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.

try:
    
    temp_entrada = float(input("Digite a temperatura: "))
    unidade_entrada = input("Digite a unidade de origem (C, F ou K): ").upper()
    unidade_convertida = input("Digite a unidade para qual deseja converter (C, F ou K): ").upper()
    
    if unidade_entrada == unidade_convertida:
        print("As unidades de origem e destino são iguais. Nenhuma conversão é necessária.")
        exit()
    
    elif unidade_entrada == "C" and unidade_convertida == "F":
        temp_convertida = (temp_entrada * 9/5) + 32
        print(f"{temp_entrada}°C é igual a {temp_convertida}°F")
        
    elif unidade_entrada == "C" and unidade_convertida == "K":
        temp_convertida = temp_entrada + 273.15
        print(f"{temp_entrada}°C é igual a {temp_convertida}K")
        
    elif unidade_entrada == "F" and unidade_convertida == "C":
        temp_convertida = (temp_entrada - 32) * 5/9
        print(f"{temp_entrada}°F é igual a {temp_convertida}°C")
        
    elif unidade_entrada == "F" and unidade_convertida == "K":
        temp_convertida = (temp_entrada - 32) * 5/9 + 273.15
        print(f"{temp_entrada}°F é igual a {temp_convertida}K")
        
    elif unidade_entrada == "K" and unidade_convertida == "C":
        temp_convertida = temp_entrada - 273.15
        print(f"{temp_entrada}K é igual a {temp_convertida}°C")
        
    elif unidade_entrada == "K" and unidade_convertida == "F":
        temp_convertida = (temp_entrada - 273.15) * 9/5 + 32
        print(f"{temp_entrada}K é igual a {temp_convertida}°F")

    print('Obrigado por usar nosso programa de conversão ;). Volte sempre!')
    
except ValueError:
    print("Valor inválido")