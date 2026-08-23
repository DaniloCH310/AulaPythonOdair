def formatar_moeda(valor):
    return f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


preco_unitario = float(input("Preço unitário: R$ ").replace(",", "."))
quantidade = int(input("Quantidade: "))
frete = float(input("Frete: R$ ").replace(",", "."))

subtotal = preco_unitario * quantidade
total = subtotal + frete

print(f"Subtotal: R$ {formatar_moeda(subtotal)}")
print(f"Total: R$ {formatar_moeda(total)}")
