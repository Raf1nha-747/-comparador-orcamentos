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
