class Solution {
public:
    int maxArea(vector<int>& heights) {
        int l, r;
        l = 0;
        r = heights.size() - 1;
        int res = 0;

        while (l < r){
            int area = min(heights[l], heights[r]) * (r - l);
            res = max(res, area);

            if (heights[r] < heights[l]){
                r--;
            }
            else{
                l++;
            }
        }

        return res;
    }
};
