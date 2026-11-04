class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs: string[]): string[][] {
        const res: Record<string,Array<string>> = {};
        for (let s of strs){
            const count: Array<number> = new Array(26).fill(0);

            for (const char of s){
                count[char.charCodeAt(0) - 'a'.charCodeAt(0)] += 1
            }
            
            const key: string = count.join(',')
            if (!res[key]){
                res[key] = [] 
            }
            res[key].push(s)
        }
        return Object.values(res)
    }
}
