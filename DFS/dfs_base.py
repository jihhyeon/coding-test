def dfs(graph, v, visited):
    #현재 노드를 방문처리
    visited[v] = True
    print(v, end = ' ')
    #현재 노드와 연결된 다른 노드를 배귀적으로 방문
    for i in graph[v]:
        if not visited[i]:#방문하지 않았다면
            dfs(graph, i, visited)#방문하지 않은 노드에 대해 dfs처리
#각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [], 
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]]
#각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False]*9

dfs(graph, 1, visited)
