class Solution:
    def minMoves(self, nums, limit):
        n = len(nums)
        delta = [0] * (2 * limit + 2)

        for i in range(n // 2):
            a = nums[i]
            b = nums[n - 1 - i]
            
            low = min(a, b)
            high = max(a, b)
            
            
            delta[2] += 2
            delta[2 * limit + 1] -= 2
            
            
            delta[low + 1] -= 1
            delta[high + limit + 1] += 1
            
           
            s = a + b
            delta[s] -= 1
            delta[s + 1] += 1


        res = float('inf')
        curr = 0
        
        for s in range(2, 2 * limit + 1):
            curr += delta[s]
            res = min(res, curr)
        
        return res