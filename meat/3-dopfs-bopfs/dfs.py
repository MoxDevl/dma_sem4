# HAVEN'T TESTED BEFORE
# Depth first search
def bfs(adjacent : list, start : int = 0) -> list:
    if color is None:
        color = [0 for i in range(len(adjacent))]

    current = start
    path = [current]
    parent = {current : -1}             # list would work to, I think
    color[start] = 1

    while color[start] != 2:

        all_colored = True              # checks if all vertexes under current already colored
        for v in adjacent[current]:     # iterates through adjacent
            if color[v] == 0:           # if v hasn't been visited before
                all_colored = False     # marks the flag
                color[v] = 1            # colors v into grey
                parent[v] = current     # matches parent to v
                current = v             # current becomes v
                path.append(current)    # adds v (which is already current) to path
                break

        if all_colored:
            color[current] = 2
            current = parent[current]          

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