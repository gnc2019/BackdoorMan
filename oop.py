class Produto:
    def __init__(self, nome, preco, quantidade_estoque):
        self.nome = nome
        self.preco = preco
        self.quantidade_estoque = quantidade_estoque
    
    def vender(self, qtd):
        if self.quantidade_estoque >= qtd:
            self.quantidade_estoque -= qtd
            print(f"O produto {self.nome} foi vendido {qtd} unidades!")
        else:
            print("Sem estoque")

    def repor(self, qtd):
        self.quantidade_estoque += qtd
        print(f"O produto {self.nome} foi reposto {qtd} unidades!")

    def exibir_dados(self):
        print("------ESTOQUE-----------")
        print(self.nome)
        print(self.preco)
        print(self.quantidade_estoque)


nome_produto = str(input("Digite o nome do produto"))
estoque_produto = int(input("Digite o estoque do produto"))
preco_produto = float(input("Digite o preço do produto"))

p = Produto(nome_produto, preco_produto, estoque_produto)

qtd_a_vender = int(input("Digite a quantidade a vender produto"))

p.exibir_dados()
p.vender(qtd_a_vender)
p.exibir_dados()
