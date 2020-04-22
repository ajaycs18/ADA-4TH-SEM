def canFinish(numTasks, prerequisites):
    graph = [[] for _ in range(numTasks)]
    visit = [0 for _ in range(numTasks)]
    for x, y in prerequisites:
        graph[x].append(y)
    def dfs(i):
        if visit[i] == -1:
            return False
        if visit[i] == 1:
            return True
        visit[i] = -1
        for j in graph[i]:
            if not dfs(j):
                return False
        visit[i] = 1
        return True
    for i in range(numTasks):
        if not dfs(i):
            return False
    return True

n = int(input('enter number of tasks: '))
prereq = [[1,0]]
if canFinish(n, prereq):
  print("Can finish")
else:
  print("Not possible to finish")
