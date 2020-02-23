def procura_chaves(dicionario, nome):
  chaves = []
  for chave in dicionario:
    if chave.startswith(nome):
      chaves.append(chave)
  return chaves