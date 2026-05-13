class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let _map = {}
        for (let i = 0; i < nums.length; i++){
            let diff = target - nums[i]
            if (diff in _map){
                return [_map[diff], i]
            }
            _map[nums[i]] = i
        }
        return []
    }
}
