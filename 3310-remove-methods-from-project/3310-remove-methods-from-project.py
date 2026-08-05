class Solution:
    def remainingMethods(
        self, n: int, k: int, invocations: List[List[int]]
    ) -> List[int]:
        adj_lst = [[] for _ in range(n)]
        for u, v in invocations:
            adj_lst[u].append(v)

        def dfs(node):
            visited[node] = 1
            for nie in adj_lst[node]:
                if visited[nie] == 0:
                    dfs(nie)

        visited = [0] * n
        dfs(k)

        for u, v in invocations:
            if visited[u] == 0 and visited[v] == 1:
                return [i for i in range(n)]

        return [i for i in range(n) if visited[i] == 0]
