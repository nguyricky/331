# CS331 F23 Homework 1
# TODO: Write your full name and student id here
# Implement Breadth First Search and Depth First Search
# Tested with Python 3.9.12

import pandas as pd


def main():
	# Don't modify main
	graph = {'S' : ['1','2', '3'],
	  '1' : ['4', '5'],
	  '2' : ['6', '7', '8'],
	  '3' : ['9'],
	  '4' : ['10', '11'],
	  '5' : ['G', '12'],
	  '6' : ['13', '14'],
	  '7' : ['15', '16'],
	  '8' : ['17', '18'],
	  '9' : ['19'],
	  '10' : [],
	  '11' : [],
	  '12' : [],
	  'G' : [],
	  '13' : [],
	  '14' : [],
	  '15' : [],
	  '16' : [],
	  '17' : [],
	  '18' : [],
	  '19' : []
	  }
	visited = set()
	# Visited_order will contain a list of nodes in the order visited
	visited_order = []
	dfs(visited, graph, 'S', visited_order)
	print("Depth First Search:", visited_order)
	df_dfs = pd.DataFrame()	
	df_dfs["solution"] = visited_order
	visited_order = []
	bfs(visited, graph, 'S', visited_order)
	print("Breadth First Search:", visited_order)
	# Recall visited_order is a mutable list aka a pointer under the hood, so you can modify it anywhere
	# and get the same value outside the function you modified it in.
	# Thus you don't need to return anything for these functions.

	# Write the results to a file
	df_bfs = pd.DataFrame()
	df_bfs["bfs"] = visited_order
	df_dfs.to_csv("dfs.csv")
	df_bfs.to_csv("bfs.csv")


def dfs(visited, graph, node, solution):
	"""Depth First Search Function to implement
	visited (set): set of visited nodes
	graph (dictionary): input graph to search on
	node (string): node to expand
	solution (list): the solution
	"""
	# TODO: Write your code here

	visited.add(node)
	solution.append(node)

	for i in graph[node]:
		if i not in visited:
			dfs(visited, graph, i, solution)

	return None


def bfs(visited, graph, node, solution):
	"""Breadth First Search Function to implement
	visited (set): set of visited nodes
	graph (dictionary): input graph to search on
	node (string): node to expand
	solution (list): the solution
	"""
	# TODO: Write your code here

	visited = set()
	queue = []

	queue.append(node)
	visited.add(node)
	solution.append(node)

	while queue:
		s = queue.pop(0)

		for i in graph[s]:
			if i not in visited:
				queue.append(i)
				visited.add(i)
				solution.append(i)

	return None


if __name__ == "__main__":
    main()
