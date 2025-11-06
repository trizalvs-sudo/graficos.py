import matplotlib.pyplot as plt

dias = [1, 2, 3, 4, 5, 6, 7]
estoque = [100, 95, 110, 105, 120, 115, 130]

plt.figure(figsize=(10, 6))
plt.plot(dias, estoque, marker='o', linestyle='-', color='skyblue')

plt.title("Tendencia de Estoque Diaria ", fontsize=15)
plt.xlabel("Dia da Semana", fontsize=12)
plt.ylabel("Quantidade", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(dias) 
plt.tight_layout()
plt.show()
