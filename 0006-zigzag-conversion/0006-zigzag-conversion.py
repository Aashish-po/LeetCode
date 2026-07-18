class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s  # no zigzag possible, single row or row count exceeds length

        rows = [[] for _ in range(numRows)]
        cur_row, direction = 0, -1  # direction flips at top/bottom boundary

        for ch in s:
            rows[cur_row].append(ch)
            if cur_row == 0 or cur_row == numRows - 1:
                direction *= -1
            cur_row += direction

        return ''.join(''.join(row) for row in rows)