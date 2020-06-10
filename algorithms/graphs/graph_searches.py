def graph_search(start_node, graph, use_dfs=True):
  """
  search graph using DFS or BFS depending on value of DFS
  :param start: node to start from
  :param graph: dictionary {node:set((adjacent node, weight)...)}
  :param DFS: if true use DFS else BFS
  :return:
  """
  pop_index = -1 if use_dfs else 0
  search_nodes, searched = [start_node], {start_node}
  while search_nodes:
    current_node = search_nodes.pop(pop_index)
    searched.add(current_node)
    search_nodes.extend((i for i in graph[current_node] if i not in searched))


def djikstra(start_node, graph):
  """
  return table of showing shortest path from
  start_node to all other node
  """
  #table = [[start_node, None, None]]+[[node, None, None] for node in graph.keys() if not node == start_node]
  table = {node:[None, None] for node in graph.keys()}
  table[start_node]=[0,None]
  search_node, visited, dist = start_node, {start_node}, 0
  while search_node:
    visited.append(search_node)
    next_node, min_dist = None, None
    for n, weight in graph[search_node]:
      if table[n][1] is None or table[n][1]<dist+weight:
        table[n][1] = weight+dist
        if next_node==None or weight+dist<min_dist:
          min_dist = weight+dist
          next_node = n
  return table


if __name__ == '__main__':
  graph_search(0, {0:(1,1), 1:(0,1)})
  djikstra(0, {0:(1,1), 1:(0,1)})