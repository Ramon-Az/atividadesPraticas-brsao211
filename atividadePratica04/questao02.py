# Calculo de notas e média de uma turma
notas = []

while True:
    try:
        entrada = input("Digite uma nota (0 a 10) ou 'fim' para sair): ")
        
        if entrada.lower() == "fim":
            break
        
        nota = float(entrada)
        
        if nota < 0 or nota > 10:
            raise Exception()
        
        notas.append(nota)
    
    except ValueError:
        print("Digite um valor válido")
    
    except Exception:
        print("Nota inválida")
        
    except KeyboardInterrupt:
        print("\nPrograma interrompido pelo usuário.")
        break

soma = 0
for nota in notas:
    soma += nota

media = soma / len(notas)

print(f"A média final é: {media:.2f}")
