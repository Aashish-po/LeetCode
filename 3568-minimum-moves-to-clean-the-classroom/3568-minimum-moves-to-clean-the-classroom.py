class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])

        litters = []
        start = None

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == "S":
                    start = (i, j)
                elif classroom[i][j] == "L":
                    litters.append((i, j))

        k = len(litters)
        all_mask = (1 << k) - 1

        litter_id = {pos: idx for idx, pos in enumerate(litters)}

        sr, sc = start

        start_mask = 0
        if (sr, sc) in litter_id:
            start_mask |= 1 << litter_id[(sr, sc)]

        best = {}

        q = deque([(sr, sc, start_mask, energy, 0)])
        best[(sr, sc, start_mask)] = energy

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            r, c, mask, e, dist = q.popleft()

            if mask == all_mask:
                return dist

            if e == 0:
                continue

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < m and 0 <= nc < n):
                    continue
                if classroom[nr][nc] == "X":
                    continue

                ne = e - 1

                if classroom[nr][nc] == "R":
                    ne = energy

                nmask = mask
                if (nr, nc) in litter_id:
                    nmask |= 1 << litter_id[(nr, nc)]

                key = (nr, nc, nmask)

                if best.get(key, -1) >= ne:
                    continue

                best[key] = ne
                q.append((nr, nc, nmask, ne, dist + 1))

        return -1
