metros = float(input("Metros: ").replace(",", "."))

centimetros = metros * 100
milimetros = metros * 1000

print(f"Centímetros: {centimetros:g}")
print(f"Milímetros: {milimetros:g}")
