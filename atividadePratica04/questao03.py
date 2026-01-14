# Verificador de senhas
while True:
    try:
        senha = input("Digite a senha ou 'fim' para sair: ")
        
        if senha.lower() == "fim":
            print("Fim do programa")
            break
        
        # deve ter pelo menos 8 caracteres
        valida_caracteres = True 
        
        # deve conter pelo menos um numero
        valida_numeros = True

        if len(senha) < 8:
            valida_caracteres = False

        for i in senha:
            if i.isdigit():
                valida_numeros = True
                break
            else:
                valida_numeros = False
        
        if valida_numeros == False:
            raise Exception("Deve conter pelo menos um número")

        if valida_caracteres and valida_numeros:
            print("Senha válida")
            break
        else:
            print("Senha inválida")
        
    except Exception as e:
        print(f"Erro: {e}. Tente novamente")