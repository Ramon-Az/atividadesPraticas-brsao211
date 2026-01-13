# Calculadora de IMC
try:
    peso = float(input("Digite seu peso: "))
    altura = float(input("Digite sua altura: "))

    # dados condicionais
    # < 18.5: classificacao = "Abaixo do peso"
    # < 25: classificacao = "Peso normal"
    # < 30: classificacao = "Sobrepeso"
    # Para os demais cenários: classificacao = "Obeso"

    imc = peso / (altura **2)
    
    if imc < 18.5:
        classificacao = "Abaixo do peso"
        print(f"Seu IMC é {imc:.2f} e você está {classificacao}")
    elif imc < 25:
        classificacao = "Peso normal"
        print(f"Seu IMC é {imc:.2f} e você está {classificacao}")
    elif imc < 30:
        classificacao = "Sobrepeso"
        print(f"Seu IMC é {imc:.2f} e você está {classificacao}")
    else:
        classificacao = "Obeso"
        print(f"Seu IMC é {imc:.2f} e você está {classificacao}")

except ValueError:
    print("Valor inválido")