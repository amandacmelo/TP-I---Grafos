def ordem(grafo):
  return len(grafo) - 1

def tamanho(grafo):
  tamanho = 0
  for linha in grafo:
    for i in range(1, ordem(grafo)+1):
      if linha[i] != 0:
        tamanho += 1
  return tamanho // 2

def densidade(grafo):
  return tamanho(grafo)/ordem(grafo)

def vizinhos(grafo, vertice):
  vizinhos = []
  for i in range(1, ordem(grafo)+1):
    if grafo[vertice][i] != 0:
      vizinhos.append(i)
  return vizinhos

def grauVertice(grafo, vertice):
  return len(vizinhos(grafo, vertice))

def verificaArticulacao(grafo, vertice):
  def dfs(grafo, vertice, visitados): #Busca em profundidade
    visitados[vertice] = True
    for vizinho in vizinhos(grafo, vertice):
      if not visitados[vizinho]:
        dfs(grafo, vizinho, visitados)

  buscaOriginal =  [False] * (ordem(grafo) + 1)
  dfs(grafo, 1, buscaOriginal)

  visitados = [False] * (ordem(grafo) + 1)
  visitados[vertice] = True  
 
  if vertice == 1:
    dfs(grafo, 2, visitados)
  else:
    dfs(grafo, 1, visitados)
  print(visitados)
  print(buscaOriginal)

  for i in range(1, ordem(grafo) + 1):
    if visitados[i] != buscaOriginal[i] and i != vertice:
      return True
  return False


def bfs(grafo, vertice, operacao):  #Busca em largura 
  visitados = [False] * (ordem(grafo) + 1)
  ordemVisita = []
  fila = [vertice]
  visitados[vertice] = True
  ordemVisita.append(vertice)
  arestasRetorno = []
  arestasNormal = []

  while fila:
    atual = fila.pop(0)
    for vizinho in vizinhos(grafo, atual):
      print(atual, vizinho)
      if not visitados[vizinho]:
        visitados[vizinho] = True
        fila.append(vizinho)
        ordemVisita.append(vizinho)
        arestasNormal.append((atual, vizinho))
      else:
        if(atual != vertice and vizinho != vertice and (vizinho, atual) not in arestasRetorno and (vizinho, atual) not in arestasNormal):
          arestasRetorno.append((atual, vizinho))
  if operacao == 1:
    return ordemVisita
  elif operacao == 2:
    return arestasRetorno  
  else:
    print("Ordem de visita:", ordemVisita)
    print("Arestas de retorno:", arestasRetorno)


def componentesConexas(grafo):
  visitados = [False] * (ordem(grafo) + 1)
  componentes = []

  def dfs(grafo, vertice, componente):
    visitados[vertice] = True
    componente.append(vertice)
    for vizinho in vizinhos(grafo, vertice):
      if not visitados[vizinho]:
        dfs(grafo, vizinho, componente)

  for vertice in range(1, ordem(grafo) + 1):
    if not visitados[vertice]:
      componente = []
      dfs(grafo, vertice, componente)
      componentes.append(componente)

  return componentes

def qtdComponentesConexas(grafo):
  return len(componentesConexas(grafo))


def possuiCiclo(grafo):
  def dfs(grafo, vertice, visitados, pai):  # Busca em profundidade
    visitados[vertice] = True
    for vizinho in vizinhos(grafo, vertice):
      if not visitados[vizinho]:  # Explora apenas vértices não visitados
        if dfs(grafo, vizinho, visitados, vertice):  # Passa o vértice atual como pai
          return True
      elif vizinho != pai:  # Vizinho já visitado que não é o pai indica ciclo
          return True
    return False

  visitados = [False] * (ordem(grafo) + 1)  # Assumindo vértices indexados de 1 a n

  for vertice in range(1, ordem(grafo) + 1):  # Lida com componentes desconexas
    if not visitados[vertice]:
      if dfs(grafo, vertice, visitados, -1):  # Usa -1 como pai inicial
        return True
  return False


def leituraArquivo(nome):
  grafo = []
  try:
    with open(nome, 'r') as arquivo:
      tamanho = int(arquivo.readline().strip()) 
      grafo = [[0 for _ in range(tamanho + 1)] for _ in range(tamanho + 1)]
      
      linhas =  arquivo.readlines()
      for linha in linhas:
        inicio, fim, peso = map(str, linha.split())
        inicio = int(inicio) 
        fim = int(fim) 
        peso = float(peso)
        grafo[inicio][fim] = peso
        grafo[fim][inicio] = peso

  except FileNotFoundError:
    print("Erro: O arquivo não foi encontrado.")
  except Exception as nome:
    print(f"Erro ao ler o arquivo: {nome}")

  return grafo


def main():
  #nome = input("Digite o caminho do arquivo: ")
  nome = "teste.txt"
  grafo = leituraArquivo(nome)

  for linha in grafo:
    print(linha)
  print("resultado")
        
if __name__ == "__main__":
  main()
