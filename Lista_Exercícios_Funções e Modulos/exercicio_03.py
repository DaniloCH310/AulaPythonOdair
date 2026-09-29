def encontrar_maior(a, b, c):
    maior = a

    if b > maior:
        maior = b

    if c > maior:
        maior = c

    return maior


numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

resultado = encontrar_maior(numero1, numero2, numero3)
print(f"O maior valor é: {resultado}")
