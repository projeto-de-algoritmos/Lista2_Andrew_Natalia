from collections import deque

class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
    def __repr__(self):
      return '%s' % (self.id)
    def __str__(self):
        return '%s' % (self.id)

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[str(neighbor)] = weight

    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[str(neighbor)]

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)
        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        # self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()



    def find_shortest_path(self,frm, to):
      inf = float('inf')
      distances = {vertex: inf for vertex in self.get_vertices()}
      visited = {vertex: None for vertex in self.get_vertices()}
      distances[frm] = 0

      vertices = list(self.get_vertices())

      while vertices:
        current_vertex = min(vertices, key=lambda v: distances[v])
        current_vertex_instance = self.get_vertex(current_vertex)

        if distances[current_vertex] == inf:
          break
        for neighbour in current_vertex_instance.get_connections():
          alternative_route = distances[current_vertex] + current_vertex_instance.get_weight(neighbour)

          if alternative_route < distances[neighbour]:
            distances[neighbour] = alternative_route
            visited[neighbour] = current_vertex

        vertices.remove(current_vertex)
      path, current_vertex = deque(), to
      while visited[current_vertex] is not None:
          path.appendleft(current_vertex)
          current_vertex = visited[current_vertex]
      if path:
          path.appendleft(current_vertex)

      return path


    