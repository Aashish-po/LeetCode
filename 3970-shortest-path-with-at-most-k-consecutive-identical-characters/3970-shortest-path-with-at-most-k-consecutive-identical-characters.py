class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))

        dist = [[float("inf")] * (k + 1) for _ in range(n)]

        pq = [(0, 0, 1)]
        dist[0][1] = 0

        while pq:
            d, u, c = heapq.heappop(pq)

            if u == n - 1:
                return d

            if d > dist[u][c]:
                continue

            for v, w in adj[u]:
                if labels[v] == labels[u]:
                    nc = c + 1
                else:
                    nc = 1
                if nc <= k and d + w < dist[v][nc]:
                    dist[v][nc] = d + w
                    heapq.heappush(pq, (d + w, v, nc))

        return -1
