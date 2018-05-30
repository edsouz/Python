dicionário = {'chave1' : 123, 'chave2' : 'string', 'chave3' : [1, 2, 3]}
print(type(dicionário))

print(dicionário['chave3'])
print(dicionário['chave3'][2])
print(dicionário['chave2'].upper())
print(dicionário)

dicionário['chave1'] = dicionário['chave1'] + 4
print(dicionário)
