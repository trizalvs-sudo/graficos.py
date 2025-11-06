import matplotlib.pyplot as plt
import numpy as np


categorias = ['Eletrônicos', 'Vestuário', 'Alimentos']
valores = np.array([15000, 8000, 5000])


total = valores.sum()
porcentagens = (valores / total) * 100
labels = [f'{c}\n({p:.1f}%)' for c, p in zip(categorias, porcentagens)]

explode = (0.1, 0, 0)

plt.figure(figsize=(9, 9))
plt.pie(
    valores, 
    explode=explode, 
    labels=labels, 
    autopct='', 
    shadow=True, 
    startangle=90,
    colors=['#a50026', '#f46d43', '#fee090']
)

plt.title("Distribuição Percentual do Valor Total de Estoque por Categoria", fontsize=15, pad=20)
plt.axis('equal') 
plt.tight_layout()
plt.show()
