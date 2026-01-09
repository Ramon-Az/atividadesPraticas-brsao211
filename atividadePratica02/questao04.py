# Calculadora de consumo de combustível
distancia_percorrida = 300
combustivel_gasto = 25

consumo_medio = distancia_percorrida / combustivel_gasto
arrendondamento = round(consumo_medio, 2)

print(f"Informações: \nDistância percorrida: {distancia_percorrida} km \nCombustível gasto: {combustivel_gasto} litros \nConsumo médio: {arrendondamento:.2f} km/l")
