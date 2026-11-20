class Solution {
public:
    int maxSelectedElements(vector<int>& nums) {
        sort(nums.begin(), nums.end());

        int ans = 0;
        unordered_map<int, int> mp;

        for (int x : nums) {
            mp[x + 1] = max(mp[x + 1], mp[x] + 1);
            mp[x] = max(mp[x - 1] + 1, mp[x]);

            ans = max({ans, mp[x], mp[x + 1]});
        }

        return ans;
    }
};