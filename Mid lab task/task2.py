from collections import deque
import heapq


graph = {
    "S": [("A", 3), ("B", 5)],
    "A": [("D", 9)],
    "B": [("C", 8), ("E", 13)],
    "C": [("F", 5)],
    "D": [("H", 12)],
    "E": [("H", 20)],
    "F": [("G2", 3)],
    "H": [("G1", 4)],
}

heuristics = {"S":9,"A":12,"B":8,"C":13,"D":7,"E":5,"F":3,"H":12,"G1":0,"G2":0}


def bfs(start, goals):
    queue = deque([(start, [start])])
    while queue:
        node, path = queue.popleft()
        if node in goals:
            return path
        for neighbor, _ in graph.get(node, []):
            queue.append((neighbor, path + [neighbor]))


def astar(start, goals):
    pq = [(heuristics[start], 0, start, [start])]
    while pq:
        est, cost, node, path = heapq.heappop(pq)
        if node in goals:
            return path, cost
        for neighbor, edge_cost in graph.get(node, []):
            new_cost = cost + edge_cost
            heapq.heappush(pq, (new_cost + heuristics[neighbor], new_cost, neighbor, path+[neighbor]))

print("BFS Path:", bfs("S", {"G1","G2"}))
print("A* Path:", astar("S", {"G1","G2"}))
