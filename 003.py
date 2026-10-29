# Seu dicionário de itens e preços
cardapio = {
    'pizza': 10,
    'suco': 5,
    'bolo': 7,
    'refrigerante': 8
}

# Transformamos as chaves (nomes dos itens) em uma lista para usar o índice
itens = list(cardapio.keys())

# Usamos o range para passar pelas 4 posições (0, 1, 2, 3)
for i in range(len(itens)):
    nome_item = itens[i]
    preco_item = cardapio[nome_item]
    
    # Imprime o índice (i), o nome do item e o preço aliado
    print(f"Índice {i} -> item: {nome_item} - preço R${preco_item}") 

