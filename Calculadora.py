while True:
    try:
        print('========== CALCULADORA ==========')

        valor1 = float(input('Digite um valor: '))

        valor2 = float(input('Digite um outro valor: '))
    
    except ValueError:
        print("Por favor digite um número")
        continue
    
    print('Os sinai que pode ser usado é: +, -, *, /')
    sinal = input("Digite um sinal: ")

    if sinal == '+':
        print(f"A resposta é: {valor1 + valor2}")
    elif sinal == '-':
        print(f"A resposta é: {valor1 - valor2}")
    elif sinal == '*':
        print(f"A resposta é: {valor1 * valor2}")
    elif sinal == '/':
        try:
            print(f"A resposta é: {valor1/valor2}")
        except ZeroDivisionError:
            print("Não é possível divisão por zero")
    elif sinal != "+" or "-" or "*" or "/":
        print("Por favor digite um sinal")

    while True:
        cont = input("Você quer tentar novamente? (s/n): ").lower()
        if cont in ["s", "n"]:
            break
        print("Por favor, digite 's' para sim ou 'n' para não.")

    if cont == "n":
        print("Fim do programa!")
        break
    print()