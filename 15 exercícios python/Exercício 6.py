largura = float(input("Largura: ").replace(",", "."))
altura = float(input("Altura: ").replace(",", "."))

area = largura * altura
perimetro = 2 * (largura + altura)

print(f"Área: {area:g}")
print(f"Perímetro: {perimetro:g}")
