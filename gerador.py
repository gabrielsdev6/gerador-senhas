import random
import string

while True:
    print("===== G E R A D O R  D E  S E N H A S =====")
    print("1. Apenas letras")
    print("2. Letras e números")
    print("3. Letras, números e caracteres especiais")
    print("0. Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 0:
        print("Saindo...")
        break

    ## APENAS LETRAS
    if opcao == 1:
        tamanho = int(input("Digite o tamanho da senha: "))
        caracteres = string.ascii_letters
        senha = ""

        for i in range(tamanho):
            senha += random.choice(caracteres)

    ## NUMEROS E LETRAS
    elif opcao == 2:
        tamanho = int(input("Digite o tamanho da senha: "))
        caracteres = string.ascii_letters + string.digits
        senha = ""

        for i in range(tamanho):
            senha += random.choice(caracteres)

    ## LETRAS, NÚMEROS E CARACTERES ESPECIAIS
    elif opcao == 3:
        tamanho = int(input("Digite o tamanho da senha: "))
        caracteres = string.ascii_letters + string.digits + string.punctuation
        senha = ""

        for i in range(tamanho):
            senha += random.choice(caracteres)
    else:
        print("Opção inválida!")
        continue


    print("================================")
    print("Senha gerada: " + senha)
    print("================================")