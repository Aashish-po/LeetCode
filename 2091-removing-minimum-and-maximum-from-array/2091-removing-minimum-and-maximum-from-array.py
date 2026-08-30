class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        mn = min(nums)
        mx = max(nums)

        mnIdx = nums.index(mn)
        mxIdx = nums.index(mx)

        left = min(mnIdx, mxIdx)
        right = max(mnIdx, mxIdx)

        return min(
            right + 1,                  # remove from front
            n - left,                   # remove from back
            (left + 1) + (n - right)    # both sides
        )