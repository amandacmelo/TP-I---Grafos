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

  for i in range(1, ordem(grafo) + 1):
    if visitados[i] != buscaOriginal[i] and i != vertice:
      return True
  return False

def bfs(grafo, vertice, operacao):  # Busca em largura considerando toda a floresta
 
  visitados = [False] * (ordem(grafo) + 1)
  
  florestasOrdemVisita = []
  arestasRetorno = []
  arestasNormal = []

  # Função interna para realizar a busca em largura a partir de um vértice específico
  def bfs_componente(vertice):
    fila = [vertice]  
    visitados[vertice] = True  
    ordemVisita = [vertice] 

    while fila: 
      atual = fila.pop(0) 
      for vizinho in vizinhos(grafo, atual):  
        if not visitados[vizinho]: 
          visitados[vizinho] = True  
          fila.append(vizinho) 
          ordemVisita.append(vizinho) 
          arestasNormal.append((atual, vizinho))  # Adiciona a aresta normal
        else:
          # Se o vizinho já foi visitado e não é o vértice inicial, adiciona como aresta de retorno
          if (atual != vertice and vizinho != vertice and 
              (vizinho, atual) not in arestasRetorno and 
              (vizinho, atual) not in arestasNormal):
            arestasRetorno.append((atual, vizinho))

    florestasOrdemVisita.append(ordemVisita)  # Adiciona a ordem de visita da componente à lista de florestas

  # Inicia a busca a partir do vértice escolhido
  bfs_componente(vertice)

  # Continua a busca para os vértices não visitados
  for vertice in range(1, ordem(grafo) + 1):
    if not visitados[vertice]: 
      bfs_componente(vertice)  # Realiza a busca em largura a partir desse vértice

  if operacao == 1:
    return florestasOrdemVisita  
  elif operacao == 2:
    return arestasRetorno 
  else:
    print("Ordem de visita por componente:", florestasOrdemVisita)
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

def floyd_warshall(grafo):
    n = ordem(grafo)  # Número de vértices
    # Inicialização das matrizes L (menores distâncias) e R (reconstrução de caminhos)
    L = [[float('inf')] * n for _ in range(n)]
    R = [[None] * n for _ in range(n)]

    # Preenchendo L e R com os valores iniciais a partir do grafo
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                L[i - 1][j - 1] = 0  # Distância para si mesmo é 0
            elif grafo[i][j] != 0:
                L[i - 1][j - 1] = grafo[i][j]

    # Regra de inicialização da matriz R
    for i in range(n):
        for j in range(n):
            if L[i][j] == float('inf'):  # Não há aresta entre i e j
                R[i][j] = None
            else:  # Inicialmente, o caminho mais curto é direto de i para j
                R[i][j] = i
    
    # Algoritmo de Floyd-Warshall
    for k in range(n):  # Índices intermediários (de 0 a n-1)
        for i in range(n):  # Vértices de origem (de 0 a n-1)
            for j in range(n):  # Vértices de destino (de 0 a n-1)
                if L[i][j] > L[i][k] + L[k][j] and R[i][k] != j and R[k][j] != i:
                    L[i][j] = L[i][k] + L[k][j]
                    R[i][j] = R[k][j]  # Atualiza o caminho para passar por k

    # Verificação de ciclos negativos
    for i in range(n):
        if L[i][i] < 0:
            print(f"Ciclo negativo detectado no vértice {i}")
            return None, None

    return L, R

def reconstruir_caminho(R, start, end):
    """Reconstrói o caminho mínimo de start a end usando a matriz R."""
    if R[start][end] is None:
        return None  # Não há caminho entre os vértices
    
    caminho = []
    atual = end
    while atual != start:
        caminho.append(atual+1)
        atual = R[start][atual]
    caminho.append(start+1)
    caminho.reverse()
    return caminho


def obter_caminhos_e_distancias(grafo, vertice):
    
    L, R = floyd_warshall(grafo)
    if L is None or R is None:
        return None
    vertice -= 1  # Ajusta o índice do vértice para a matriz L
    """Retorna as distâncias e os caminhos mínimos do vértice dado para todos os outros."""
    caminhos = {}
    n = ordem(grafo)  
    for destino in range(n):
        caminho = reconstruir_caminho(R, vertice, destino)
        caminhos[destino] = {
            "distancia": L[vertice][destino],
            "caminho": caminho
        }
    return caminhos

