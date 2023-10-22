# CS331 F23 Homework 2 
# TODO: Write your full name here
# Implement A* Search
# Tested with Python 3.9.12

from time import time


class Node:
    """Node class
    name (string): Node name like "S" or "1"
    heuristic (int): h value
    neighbors (dictionary): dictionary of neighboring nodes with values as neighbors
    cost (int): cost from S to the node 
    """
    def __init__(self, name, heuristic):
        self.name = name
        self.heuristic = heuristic
        self.neighbors = {}
        self.cost = float('inf') 

    def add_neighbor(self, neighbor, cost):
        self.neighbors[neighbor] = cost


def a_star_search(start, goal):
    """Implement A* Search
    start: start node S
    goal: goal node G
    shortest_path (list of strings)
    solution_cost (int)
    nodeds_expanded (list of strings)"""
    # TODO: Write your code here

    # Skeleton code to be changed, just here so things can run
    shortest_path, solution_cost, nodes_expanded = [], 0, []

    return shortest_path, solution_cost, nodes_expanded 


def main():
    # Graph
    S = Node("S", 7)
    node1 = Node("1", 6)
    node2 = Node("2", 5)
    node3 = Node("3", 4)
    node4 = Node("4", 2)
    node5 = Node("5", 3)
    G = Node("G", 0)

    # Adding edges
    S.add_neighbor(node1, 6)
    S.add_neighbor(node2, 5)
    node1.add_neighbor(node3, 3)
    node1.add_neighbor(node4, 4)
    node2.add_neighbor(node4, 6)
    node2.add_neighbor(node5, 5)
    node3.add_neighbor(node4, 5)
    node4.add_neighbor(G, 4)
    node5.add_neighbor(node4, 8)

    # Running A*
    start_time = time()
    shortest_path, solution_cost, nodes_expanded = a_star_search(S, G)
    end_time = time()

    # Outputting the results
    print("Shortest path", shortest_path)
    print("Solution cost:", solution_cost)
    print("Number of nodes expanded:", nodes_expanded)
    print("Time taken to solve: {:.5f} seconds".format(end_time - start_time))


if __name__ == "__main__":
    main()
