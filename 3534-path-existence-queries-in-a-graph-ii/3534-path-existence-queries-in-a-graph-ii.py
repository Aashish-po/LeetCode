class Solution:
    def pathExistenceQueries(
        self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]
    ) -> List[int]:

        # 1. Sort nodes by value, keep track of original index
        sorted_nums = sorted((val, i) for i, val in enumerate(nums))

        # 2. Map original node id -> its position in sorted order
        pos = [0] * n
        for idx, (val, node) in enumerate(sorted_nums):
            pos[node] = idx

        # 3. reach(i): farthest sorted index directly reachable from i in 1 edge
        max_jump = [0] * n
        for idx, (val, _node) in enumerate(sorted_nums):
            target = val + maxDiff
            # last index whose value <= target
            next_idx = bisect.bisect_right(sorted_nums, (target, float('inf'))) - 1
            max_jump[idx] = next_idx

        # 4. Binary lifting table: up[k][i] = position after 2^k greedy jumps
        LOG = max(1, n.bit_length())
        up = [max_jump]
        for k in range(1, LOG):
            prev = up[-1]
            up.append([prev[prev[i]] for i in range(n)])

        # 5. Answer queries
        res = []
        for u, v in queries:
            A, B = pos[u], pos[v]

            if A == B:
                res.append(0)
                continue

            if A > B:
                A, B = B, A

            curr, jumps = A, 0
            for k in range(LOG - 1, -1, -1):
                if up[k][curr] < B:
                    curr = up[k][curr]
                    jumps += (1 << k)

            if max_jump[curr] >= B:
                res.append(jumps + 1)
            else:
                res.append(-1)

        return res