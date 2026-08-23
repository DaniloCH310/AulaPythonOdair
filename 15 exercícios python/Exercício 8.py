def formatar_moeda(valor):
    return f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


preco = float(input("Preço: R$ ").replace(",", "."))

desconto = preco * 0.10
preco_final = preco - desconto

print(f"Desconto: R$ {formatar_moeda(desconto)}")
print(f"Preço final: R$ {formatar_moeda(preco_final)}")
