class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        M = r - l + 1
        dim = 2 * M
        def multiply(A, B):
            C = [[0] * dim for _ in range(dim)]
            for i in range(dim):
                for k in range(dim):
                    if A[i][k] == 0:
                        continue
                    for j in range(dim):
                        C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD
            return C
        def power(matrix, p):
            res = [[0] * dim for _ in range(dim)]
            for i in range(dim):
                res[i][i] = 1
            base = matrix
            while p > 0:
                if p % 2 == 1:
                    res = multiply(res, base)
                base = multiply(base, base)
                p //= 2
            return res
        T = [[0] * dim for _ in range(dim)]
        
        for v in range(M):
            for j in range(v):
                T[v][M + j] = 1
            for j in range(v + 1, M):
                T[M + v][j] = 1
                
        base_vector = [0] * dim
        for v in range(M):
            base_vector[v] = v         
            base_vector[M + v] = M - 1 - v 
            
        T_pow = power(T, n - 2)
        
        total_valid = 0
        for i in range(dim):
            row_sum = 0
            for j in range(dim):
                row_sum = (row_sum + T_pow[i][j] * base_vector[j]) % MOD
            total_valid = (total_valid + row_sum) % MOD
            
        return total_valid