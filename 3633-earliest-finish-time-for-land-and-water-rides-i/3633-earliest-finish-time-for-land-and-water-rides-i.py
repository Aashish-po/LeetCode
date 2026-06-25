class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int]
    ) -> int:
        
        ans = float('inf')
        
        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                
                # Option 1: Land -> Water
                finish_land = landStartTime[i] + landDuration[i]
                start_water = max(finish_land, waterStartTime[j])
                ans = min(ans, start_water + waterDuration[j])
                
                # Option 2: Water -> Land
                finish_water = waterStartTime[j] + waterDuration[j]
                start_land = max(finish_water, landStartTime[i])
                ans = min(ans, start_land + landDuration[i])
        
        return ans