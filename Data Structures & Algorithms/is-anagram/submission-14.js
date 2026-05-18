class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        let freq = {}
        if (s.length != t.length) return false;
        for (const char of s){
            freq[char] = (freq[char] || 0) + 1;
        }

        for (const char of t){
            if (!freq[char]) return false 
            else{
                freq[char]--
            }
        }
        return true 
    }
}
