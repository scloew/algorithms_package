"""utility functions for generating random graphs"""

from random import randint


def build_weighted_graph(num_nodes=10, min_edges=1, max_edges=2):
  """
  builds a random graph with num_nodes nodes that can have
  inclusively between min_edges and max_edges between each vertex
  with weights randomly assigned between 1 and 10

  returns graph as dictionary:
  {node: set((adjacent node, edge weight)...)}
  """
  graph = {i: set() for i in range(num_nodes)}
  for node in graph.keys():
    num_edges = randint(min_edges, max_edges)
    used = {node}
    for _ in range(num_edges - len(graph[node])):
      connected_node = randint(0, num_nodes-1)
      while connected_node in used:
        connected_node = randint(0, num_nodes - 1)
      used.add(connected_node)
      weight = randint(0, 10)
      graph[node].add((connected_node, weight))
      graph[connected_node].add((node, weight))
      print('\n***\n***\n')
  for node, adjacent in graph.items():
    print(node, adjacent)

if __name__ == '__main__':
  build_weighted_graph()
