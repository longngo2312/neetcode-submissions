class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        const checker = new Set(nums);
        let res = 0
        for (let i = 0; i < nums.length; i++){
            if (!(checker.has(nums[i] - 1))){
                let curr = 0
                while (checker.has(nums[i] + curr)){
                    curr++;
                }
                res = Math.max(res, curr)
            }
        }
        return res;
    }
}
