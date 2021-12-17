# crie um produto e preço para três itens
produto1_nome, produto1_valor = "Livro", 50.95
produto2_nome, produto2_valor = "Computador", 598.99
produto3_nome, produto3_valor = "Monitor", 156.89

# Agora vamos guardar o nome e endereço de uma empresa que é muito importante mostrar no topo de um recibo
nome_empresa = 'O programador inteligente, inc.'
endereço_empresa = 'Av.Presidente Vargas 144'
cidade_empresa = 'Rio de Janeiro'

# Agora vou armazenar uma mensagem de saudação em uma variável para mostrar no final da nota fiscal
mensagem = 'Obrigado por comprar conosco hoje!'

# criar uma borda superior
print('*' * 50)

# Agora vou imprimir o nome da empresa em um formato tabular
print('\t\t{}'.format(nome_empresa.title()))
print('\t\t{}'.format(endereço_empresa.title()))
print('\t\t{}'.format(cidade_empresa.title()))

# imprimir uma linha entre as seções
print('=' * 50)

# Agora vamos imprimir os nomes e preços dos produtos no formato tabular
print('\tProduto Nome\tProduto Valor')

# criar uma declaração impressa para cada item
print('\t{}\t\tR$ {}'.format(produto1_nome.title(), produto1_valor))
print('\t{}\tR$ {}'.format(produto2_nome.title(), produto2_valor))
print('\t{}\t\tR$ {}'.format(produto3_nome.title(), produto3_valor))

# imprimir uma linha entre as seções
print('=' * 50)

# imprimir o cabeçalho para a seção do total
print('\t\t\tTotal')

# calcular o preço total e imprimir
total = produto1_valor + produto2_valor + produto3_valor
print('\t\t\t R$ {}'.format(total))

# imprimir uma linha entre as seções
print('=' * 50)

# saída da mensagem de agradecimento
print('\n\t{}\n'.format(mensagem))

# imprimir uma linha entre as seções
print('=' * 50)




