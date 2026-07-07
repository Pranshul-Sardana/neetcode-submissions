class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        strsCounts = defaultdict(list)
    
        for item in strs:
            count = [0]*26

            for alphabet in item:
                count[ord(alphabet)-ord("a")] += 1

            strsCounts[tuple(count)].append(item)

        #print(strsCounts)
        
        return list(strsCounts.values())