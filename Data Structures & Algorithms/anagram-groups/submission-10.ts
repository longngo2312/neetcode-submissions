class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs: string[]): string[][] {
        let hashMap: Object = {};
        let result: Array<Array<string>> = [];

        for (const word of strs){
            let sortedWord = word.split("").sort().join("")
            if (!(sortedWord in hashMap)){
                hashMap[sortedWord] = []
            }

            hashMap[sortedWord].push(word)
        } 

        for (const key in hashMap){
            result.push(hashMap[key])
        }

        return result
    }
}
