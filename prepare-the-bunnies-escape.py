# python 2.7.13


def find_path_bfs(graph, start, end):
    """
    find path using bfs
    """
    visited = [start]
    queue = [start]
    counter = 1
    path_length = 1
    while queue:
        node = queue.pop(0)
        counter -= 1
        if node == end:
            return path_length
        for n in graph[node]:
            if n not in visited:
                queue.append(n)
                visited.append(n)
        
        if counter == 0:
            counter = len(queue)
            path_length += 1
    return path_length

def make_adjacent_list(graph):
    res = {}
    for r, row in enumerate(graph):
        for idx in range(1, len(row)):
            if row[idx-1] == 0 and row[idx] == 0:
                if not res.get((r, idx), None):
                    res[(r, idx)] = []
                if not res.get((r, idx-1), None):
                    res[(r, idx-1)] = []
                res[(r, idx)].append((r, idx-1))
                res[(r, idx-1)].append((r, idx))
    for c, col in enumerate(zip(*graph)):
        for idx in range(1, len(col)):
            if col[idx-1] == 0 and col[idx] == 0:
                if not res.get((idx, c), None):
                    res[(idx, c)] = []
                if not res.get((idx-1, c), None):
                    res[(idx-1, c)] = []
                res[(idx, c)].append((idx-1, c))
                res[(idx-1, c)].append((idx, c))
    return res

def solution(map_):
    """
    start point (0, 0)
    end point (w-1, h-1)
    """

    print("=========================")
    for row in map_:
        print(row)

    steps = []
    adjacent_list = make_adjacent_list(map_)
    steps.append(find_path_bfs(adjacent_list, (0, 0), (len(map_)-1, len(map_)-1)))

    for row in range(len(map_)):
        for col in range(len(map_[0])):
            if map_[row][col] == 0:
                continue
            map_[row][col] = 0

            adjacent_list = make_adjacent_list(map_)
            steps.append(find_path_bfs(adjacent_list, (0, 0), (len(map_)-1, len(map_)-1)))
            map_[row][col] = 1

    return min(steps)
    

print solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])
# 7

print solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])
# 11
