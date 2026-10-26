# Sua lista inicial
cardapio = ['pizza', 'pastel', 'coxinha']

# A forma mais simples de acrescentar um item
cardapio.append('refrigerante')

# Resultado: ['pizza', 'pastel', 'coxinha', 'refrigerante']
print(cardapio)

# Sua lista inicial atualizada
cardapio = ['pizza', 'pastel', 'coxinha', 'refrigerante']

# Removendo um item específico da lista (exemplo: 'pastel')
cardapio.remove('pastel')

# Resultado esperado: ['pizza', 'coxinha', 'refrigerante']
print(cardapio)

# Sua lista inicial
cardapio = ['pizza', 'pastel', 'coxinha']

# Inserindo 'refrigerante' na primeira posição (índice 0)
cardapio.insert(0, 'refrigerante')

# Inserindo 'suco' na terceira posição (índice 2)
cardapio.insert(2, 'suco')

# Resultado esperados
print(cardapio)