# Uses python3

import sys

def explore(adj, vertex, visited):
    visited[vertex] = True

    for neighbor in adj[vertex]:
        if not visited[neighbor]:
            explore(adj, neighbor, visited)

def search(adj, init, target):
    _len = len(adj)
    visited = [False for _ in range(_len)]

    explore(adj, init, visited)

    return int(visited[target])

def reach(adj, x, y):
    if y in adj[x]:
        return 1

    else:
        return search(adj, x, y)

if __name__ == '__main__':
    _input = sys.stdin.read()    
    data = list(map(int, _input.split()))

    # n - vertices; m - edges
    n, m = data[0:2]
    data = data[2:]

    # data[0:(2 * m):2] - gets every other element starting from 0 until number of edges points
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))

    x, y = data[2 * m:]

    # create n lists 
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)

    print(reach(adj, x, y))
