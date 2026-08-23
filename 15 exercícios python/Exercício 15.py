primeiro_valor = float(input("Primeiro valor: ").replace(",", "."))
segundo_valor = float(input("Segundo valor: ").replace(",", "."))

if primeiro_valor > segundo_valor:
    print(f"Maior valor: {primeiro_valor:g}")
elif segundo_valor > primeiro_valor:
    print(f"Maior valor: {segundo_valor:g}")
else:
    print("VALORES IGUAIS")
