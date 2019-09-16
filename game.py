import pydot
from graph import Vertex, Graph
from string import ascii_uppercase  
from random import randint, randrange
import subprocess
import pydot
import os


class Game():
  solution_path = []
  dot = pydot.Dot(graph_type='digraph')
  frm = None
  to = None

  def __init__(self, level):
    self.graph = Graph()
    self.random_graph(level)
    self.frm, self.to = self.selectVertices()

  def random_graph(self, level):
    labels = ascii_uppercase[0:level*5]
    for letter in labels:
      for i in range(randint(1,5)):
        adj = labels[randint(0,(level*5)-1)]
  
        while adj == letter:
          adj = labels[randint(0,(level*5)-1)]

        self.graph.add_edge(letter, adj, cost=randint(1,10))

  def selectVertices(self):

    vertices = list(self.graph.get_vertices())
    frm = to = None
    while frm == to:
      frm, to = [vertices[randrange(len(vertices))] for vertice in range(2)]
    return frm, to

  def solve(self):
    self.solution_path = self.graph.find_shortest_path(self.frm,self.to)

  def plotFeedback(self):
    if len(self.solution_path) > 0:
      f = self.solution_path.popleft()
    while len(self.solution_path) > 0 :
      t = self.solution_path.popleft()
      edge = self.dot.get_edge(f,dst=t)[0]
      edge.set_color("green")
      f = t
    self.dot.write_png('graph-game.png')
  def plotGraph(self):
    vertices = self.graph.vert_dict
    
    for v in vertices.keys():
      n = pydot.Node(v, style='filled')
      if v == self.frm:
        n.set_fillcolor('red')
      elif v == self.to:
        n.set_fillcolor('blue')
      self.dot.add_node(n)

    for v in vertices.keys():
      vert = vertices[v]
      for neighbour in vertices[v].get_connections():
        f = self.dot.get_node(v)[0]
        t = self.dot.get_node(neighbour)[0]
        self.dot.add_edge(pydot.Edge(f, t, label=vert.get_weight(vertices[neighbour])))
    self.dot.write_png('graph-game.png')
  
  def destroy(self):
    for e in self.dot.get_edge_list():
      self.dot.del_edge(e.get_source(),dst=e.get_destination(),index=0)
    for n in self.dot.get_node_list():
      self.dot.del_node(n.get_name())

while 1:
  print("Insira o nível do desafio que deseja: (1-5): ")
  level = int(input())
  while 5<level<1: level = input()
  print("Estou preparando o desafio especial para você!")
  game = Game(level)
  game.plotGraph()
  game.solve()
  print("Um grafo será exibido e voce tera que encontrar o menor caminho a partir do ponto vermelho até o azul.")
  print("Insira o caminho que você encontrou da seguinte forma exemplo do A até o P: 'A-C-D-P'")
  input("Quando estiver pronto, aperte enter para continuar... ")
  p = subprocess.Popen(['python', 'showImage.py'],stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
  print("Olhe a imagem e encontre o melhor caminho\nResposta: ")
  answer = input()
  if answer == '-'.join(game.solution_path):
    print("Parabéns você acertou!")
  else:
    print("Que pena, você errou!")
  print("A resposta correta é:")
  print('-'.join(game.solution_path))
  game.plotFeedback()
  p.stdin.write(b'a')
  p.stdin.flush()

  
  game.destroy()
  print("Deseja jogar novamente?(s/n)")
  op=input()

  p.terminate()
  p.kill()
  os.system("rm *.png")
  if op == 's': 
    continue
  else: 
    break
