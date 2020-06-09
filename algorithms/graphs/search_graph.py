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


if __name__ == '__main__':
  graph_search(0, {0:(1,1), 1:(0,1)})