class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        let prefix = 1;
        let pre_arr = new Array(nums.length).fill(1);
        for (let i = 0; i < nums.length; i++){
            pre_arr[i] = prefix;
            prefix *= nums[i];
        }
        let postfix = 1;
        for (let j = nums.length - 1; j > -1; j--){
            pre_arr[j] *= postfix;
            postfix *= nums[j]
        }
        return pre_arr;

    }
}
