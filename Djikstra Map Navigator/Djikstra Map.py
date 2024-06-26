import math
import heapq


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)
        self.edges[value] = []

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance


def dijkstra(graph, initial):
    # Initialize distances from the source node to all other nodes as infinity
    distances = {node: math.inf for node in graph.nodes}
    distances[initial] = 0

    # Priority queue to store nodes with their current known shortest distance from the start
    priority_queue = [(0, initial)]  # (distance, node)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Visit each edge exiting from the current node
        for neighbor in graph.edges[current_node]:
            distance = current_distance + graph.distances[(current_node, neighbor)]

            # If a shorter path to the neighbor is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Example usage:
if __name__ == "__main__":
    # Create a graph
    graph = Graph()

    # Add nodes
    graph.add_node("A")
    graph.add_node("B")
    graph.add_node("C")
    graph.add_node("D")
    graph.add_node("E")

    # Add edges with weights
    graph.add_edge("A", "B", 6)
    graph.add_edge("A", "D", 1)
    graph.add_edge("B", "D", 2)
    graph.add_edge("B", "E", 2)
    graph.add_edge("B", "C", 5)
    graph.add_edge("D", "E", 1)
    graph.add_edge("E", "C", 5)

    # Compute shortest paths from "A" to all other nodes
    distances_from_A = dijkstra(graph, "A")
    print("Shortest distances from node 'A':", distances_from_A)
