import os

from bibliotecaGrafos import *
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

  print("Bem-vindo(a) à biblioteca de grafos não direcionados ponderados!\n")
  '''
  print("Matriz de pesos:")
  for linha in grafo:
    print(linha)
  '''
  
  opcao = int(1)
  while (opcao != 0):
      print("\nEscolha uma opção:")
      print("1 - Retornar a ordem do grafo")
      print("2 - Retornar o tamanho do grafo")
      print("3 - Retornar a densidade ε(G) do grafo")
      print("4 - Retornar os vizinhos de um vértice fornecido")
      print("5 - Retornar o grau de um vértice fornecido")
      print("6 - Verificar se um vértice é articulação")
      print("7 - Retornar a sequência de vértices visitados na busca em largura e informar a(s) aresta(s) que não faz(em) parte da árvore de busca em largura")
      print("8 - Retornar o número de componentes conexas do grafo e os vértices de cada componente")
      print("9 - Verificar se um grafo possui ciclo")
      print("10 - Retornar a distância e o caminho mínimo")
      print("0 - Sair\n")

      opcao = int(input("Digite a opção desejada: "))

      match opcao:
        case 0:
          break
        case 1:
          print("Ordem do grafo:", ordem(grafo))
        case 2:
          print("Tamanho do grafo:", tamanho(grafo))
        case 3:
          print(f"Densidade do grafo: {densidade(grafo):.2f}")
        case 4:
          vertice = int(input("Digite o vértice: "))
          print(f"Vizinhos do vértice {vertice}: {vizinhos(grafo, vertice)}")
        case 5:
          vertice = int(input("Digite o vértice: "))
          print(f"Grau do vértice {vertice}: {grauVertice(grafo, vertice)}")
        case 6:
          vertice = int(input("Digite o vértice: "))
          if(verificaArticulacao(grafo, vertice) == True):
            print(f"O vértice {vertice} é uma articulação")
          else:
            print(f"O vértice {vertice} não é uma articulação")
        case 7:
          vertice = int(input("Digite o vértice pelo qual deseja iniciar a busca: "))
          print(f"Busca em largura a partir do vértice {vertice}: ")
          bfs(grafo, vertice, 3)
        case 8:
          componentes = componentesConexas(grafo)
          print("Número de componentes conexas:", len(componentes))
          for i, componente in enumerate(componentes):
            print(f"Componente {i+1}: {componente}")
        case 9:
          if(possuiCiclo(grafo)):
            print("O grafo possui ciclo")
          else:
            print("O grafo não possui ciclo")
        case 10:
          vertice = int(input("Digite o vértice de origem: "))
          resultados = obter_caminhos_e_distancias(grafo, vertice)
          if resultados is None:
            print("O grafo possui ciclo negativo.")
          else:
            print(f"\nDistâncias e caminhos a partir do vértice {vertice}:")
            for destino, info in resultados.items():
                  print(f"Para o vértice {destino + 1}:")
                  print(f"  Distância: {info['distancia']:.2f}")
                  print(f"  Caminho: {info['caminho']}")
        case _:
          print("Opção inválida. Tente novamente.")
      input("Pressione Enter para continuar...")
      os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
  main()