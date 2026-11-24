import pandas as pd

df = pd.read_csv("orcamentos.csv")

# Fornecedor mais barato de cada produto
melhores = df.loc[df.groupby("produto")["preco"].idxmin()]
print("Melhores preços:")
print(melhores)

# Preço médio por produto
print("\nPreço médio:")
print(df.groupby("produto")["preco"].mean())

# Salva o resultado em um novo arquivo
melhores.to_csv("melhores_precos.csv", index=False)


total_melhor = melhores["preco"].sum()
total_medio = df.groupby("produto")["preco"].mean().sum()
print(f"\nEconomia estimada: R$ {total_medio - total_melhor:.2f}")

import matplotlib.pyplot as plt

grafico = df.pivot(index="produto", columns="fornecedor", values="preco")
grafico.plot(kind="bar")
plt.title("Preço por fornecedor")
plt.ylabel("Preço (R$)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("grafico.png")
plt.show()
