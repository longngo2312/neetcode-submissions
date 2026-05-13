class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        set<int>neighbors(nums.begin(), nums.end());
        int res = 0;
        for (int num : nums){
            if (!(neighbors.find(num - 1) != neighbors.end())){
                int curr = 0;
                while (neighbors.find(num + curr) != neighbors.end()){
                    curr++;
                }
                res = max(res,curr);
            }
       }
       return res;
    }
};
