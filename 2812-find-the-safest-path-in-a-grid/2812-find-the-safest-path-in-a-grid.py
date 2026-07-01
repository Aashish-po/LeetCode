class Solution:
    def maximumSafenessFactor(self, grid):
        n = len(grid)
        
        # Step 1: Compute distance from nearest thief
        dist = [[-1]*n for _ in range(n)]
        q = deque()
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    q.append((i, j))
        
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while q:
            x, y = q.popleft()
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
        
        # Step 2: Binary search + BFS
        def can_go(min_safe):
            if dist[0][0] < min_safe:
                return False
            
            q = deque([(0, 0)])
            seen = {(0, 0)}
            
            while q:
                x, y = q.popleft()
                if (x, y) == (n - 1, n - 1):
                    return True
                
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if (0 <= nx < n and 0 <= ny < n and
                        (nx, ny) not in seen and
                        dist[nx][ny] >= min_safe):
                        seen.add((nx, ny))
                        q.append((nx, ny))
            
            return False
        
        left, right = 0, max(max(row) for row in dist)
        ans = 0
        
        while left <= right:
            mid = (left + right) // 2
            if can_go(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return ans