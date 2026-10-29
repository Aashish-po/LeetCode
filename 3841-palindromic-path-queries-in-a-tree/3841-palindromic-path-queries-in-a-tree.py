class Solution:
    def palindromePath(
        self, n: int, edges: list[list[int]], s: str, queries: list[str]
    ) -> list[bool]:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        L = n.bit_length()
        tin, tout, depth, up = [0] * n, [0] * n, [0] * n, [[-1] * L for _ in range(n)]
        bit, chars, self.tm = [0] * (n + 2), list(s), 0

        def dfs(u, p, d):
            self.tm += 1
            tin[u], depth[u], up[u][0] = self.tm, d, p
            for i in range(1, L):
                up[u][i] = up[up[u][i - 1]][i - 1] if up[u][i - 1] != -1 else -1
            for v in g[u]:
                if v != p:
                    dfs(v, u, d + 1)
            tout[u] = self.tm

        dfs(0, -1, 0)

        def upd(i, v):
            while i <= n:
                bit[i] ^= v
                i += i & -i

        def qry(i, r=0):
            while i:
                r ^= bit[i]
                i -= i & -i
            return r

        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            for i in range(L):
                if (depth[u] - depth[v]) & (1 << i):
                    u = up[u][i]
            if u == v:
                return u
            for i in range(L - 1, -1, -1):
                if up[u][i] != up[v][i]:
                    u, v = up[u][i], up[v][i]
            return up[u][0]

        for i in range(n):
            v = 1 << (ord(chars[i]) - 97)
            upd(tin[i], v)
            upd(tout[i] + 1, v)

        ans = []
        for q in queries:
            p = q.split()
            if p[0] == "update":
                u, c = int(p[1]), p[2]
                df = (1 << (ord(chars[u]) - 97)) ^ (1 << (ord(c) - 97))
                chars[u] = c
                upd(tin[u], df)
                upd(tout[u] + 1, df)
            else:
                u, v = int(p[1]), int(p[2])
                m = qry(tin[u]) ^ qry(tin[v]) ^ (1 << (ord(chars[get_lca(u, v)]) - 97))
                ans.append(m & (m - 1) == 0)

        return ans
