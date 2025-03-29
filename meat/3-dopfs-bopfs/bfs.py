from queue import Queue

# HAVEN'T TESTED YET
# Breadth first search
def bfs(adjacent : list, start : int = 0, color : list = None, que : Queue = None) -> list:
    if color is None:
        color = [0 for i in range(len(adjacent))]
    if que is None:
        que = Queue()

    path = []
    if color[start] == 0:
        color[start] = 1
    path.append(start)

    for v in adjacent[start]:
        if color[v] == 0:
            color[v] = 1
            que.put(v)
            path.append(v)
    
    while not que.empty():
        next_v = que.get()
        if color[next_v] == 1:
            for v in bfs(adjacent, next_v, color, que):
                path.append(v)

    return path


# INPUT
# N - amount of vertexes
N = int(input())
# Adjecent vertexes for each vertex in next N lines
# K - amount of adjecent
# numbers for adjacent vertexes
adj = [None]*N
for i in range(N):
    K = int(input())
    adj[i] = []
    if (K == 0):
        continue
    for x in input().split():
        adj[i].append(int(x)-1)

path = bfs(adj)

print(path)