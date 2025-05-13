num_produtos = int(input("Quantos produtos foram vendidos hoje?"))

# Armazena vários produtos
nomes_produtos = []
quantidades = []
precos = []

# Percorre e captura os dados dos produtos
for i in range(num_produtos):
    nome = str(input("Nome do produto:"))
    quantidade = int(input("Quantidade do produto:"))
    preco = float(input("Preço do produto:"))

    #Insere nas listas os dados dos produtos
    nomes_produtos.append(nome)
    quantidades.append(quantidade)
    precos.append(preco)

total_vendas = 0
mais_vendido_qtd=0
mais_vendido_nome=""
total_itens = 0

for i in range(num_produtos):
    subt_total = quantidades[i] * precos[i]
    total_vendas = total_vendas + subt_total
    total_itens = total_itens + quantidades[i]

    # verificar item mais vendido
    if quantidades[i] > mais_vendido_qtd:
        mais_vendido_nome = nomes_produtos[i]
        mais_vendido_qtd = quantidades[i]

print(f"Total de vendas: {total_vendas} ")
print(f"Produto mais vendido: {mais_vendido_nome} com {mais_vendido_qtd} unidades")
print(f"Quantidade total de itens vendidos no dia: { total_itens}")