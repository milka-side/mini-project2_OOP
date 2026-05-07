#python3
import collections
import sys


class Edge:
    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = 0

class FlowGraph:
    def __init__(self, n):
        self.graph = [[] for _ in range(n)]
        self.edges = []

    def add_edge(self, from_, to, capacity):
        self.graph[from_].append(len(self.edges))
        self.edges.append(Edge(from_, to, capacity))
        self.graph[to].append(len(self.edges))
        self.edges.append(Edge(to, from_, 0))

    def add_flow(self, id, flow):
        self.edges[id].flow += flow
        self.edges[id ^ 1].flow -= flow

def max_flow(graph, from_, to):
    total_flow = 0
    n = len(graph.graph)
    while True:
        parent = [-1] * n
        edge_from = [-1] * n
        queue = collections.deque([from_])
        parent[from_] = from_
        while queue:
            curr = queue.popleft()
            if curr == to: break
            for id in graph.graph[curr]:
                edge = graph.edges[id]
                if parent[edge.v] == -1 and edge.capacity > edge.flow:
                    parent[edge.v] = curr
                    edge_from[edge.v] = id
                    queue.append(edge.v)
        if parent[to] == -1:
            break
        path_flow = float('inf')
        curr = to
        while curr != from_:
            id = edge_from[curr]
            path_flow = min(path_flow, graph.edges[id].capacity - graph.edges[id].flow)
            curr = parent[curr]
        total_flow += path_flow
        curr = to
        while curr != from_:
            id = edge_from[curr]
            graph.add_flow(id, path_flow)
            curr = parent[curr]
    return total_flow

if __name__ == '__main__':
    input_data = sys.stdin.read().split()
    if input_data:
        n, m = map(int, input_data[:2])
        graph = FlowGraph(n)
        idx = 2
        for _ in range(m):
            u, v, c = map(int, input_data[idx : idx + 3])
            graph.add_edge(u - 1, v - 1, c)
            idx += 3
        print(max_flow(graph, 0, n - 1))
