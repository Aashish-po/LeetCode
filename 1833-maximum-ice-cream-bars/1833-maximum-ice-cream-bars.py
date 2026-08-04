class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        heapq.heapify(costs)
        count = 0

        while costs and coins >= costs[0]:
            coins -= heapq.heappop(costs)
            count += 1

        return count
