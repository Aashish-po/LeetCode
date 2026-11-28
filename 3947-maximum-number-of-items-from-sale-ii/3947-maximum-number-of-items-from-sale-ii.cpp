class Solution {
public:
    long long maximumSaleItems(vector<vector<int>>& items, long long budget) {
        int n = static_cast<int>(items.size());
        const long long INF = numeric_limits<long long>::max();

        vector<long long> freq(n + 1, 0);
        long long global_min_p = INF;

        for (const auto& item : items) {
            int f = item[0];
            long long p = item[1];
            ++freq[f];
            if (p < global_min_p) {
                global_min_p = p;
            }
        }

        // mult_count[f] = total items whose factor is a multiple of f.
        vector<long long> mult_count(n + 1, 0);
        for (int f = 1; f <= n; ++f) {
            if (freq[f] > 0) {
                long long total = 0;
                for (int m = f; m <= n; m += f) {
                    total += freq[m];
                }
                mult_count[f] = total;
            }
        }

        // {price_for_2_items, max_2_item_copies} per individual item.
        vector<pair<long long, long long>> bundles;
        bundles.reserve(n);

        for (const auto& item : items) {
            int f = item[0];
            long long p = item[1];
            long long c_i = mult_count[f] - 1;
            if (c_i > 0) {
                bundles.emplace_back(p, c_i);
            }
        }

        sort(bundles.begin(), bundles.end());

        long long total_items = 0;
        long long rem = budget;

        for (const auto& [p, count] : bundles) {
            if (p > 2LL * global_min_p) {
                break;
            }
            long long can_buy = min(count, rem / p);
            total_items += can_buy * 2LL;
            rem -= can_buy * p;
            if (can_buy < count) {
                break;
            }
        }

        total_items += rem / global_min_p;
        return total_items;
    }
};