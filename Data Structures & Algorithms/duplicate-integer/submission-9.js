class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let _set = new Set()
        for (const num of nums){
            if (_set.has(num)){
                return true 
            }
            _set.add(num);
        }
        return false 
    }
}
