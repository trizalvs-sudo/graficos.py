import matplotlib.pyplot as plt
import pandas as pd


produtos = ['Teclado', 'Mouse', 'Monitor', 'Webcam']
quantidades = [50, 75, 30, 60]


df_comparacao = pd.DataFrame({
    'Produto': produtos,
    'Quantidade': quantidades
}).sort_values(by='Quantidade', ascending=False)


plt.figure(figsize=(10, 6))
cores = ['#2c7fb8', '#41b6c4', '#a1dab4', '#c7e9b4'] 
plt.bar(df_comparacao['Produto'], df_comparacao['Quantidade'], color=cores)

plt.title("Comparativo de Estoque Atual por Produto", fontsize=15)
plt.xlabel("Produto", fontsize=12)
plt.ylabel("Quantidade em Estoque", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
