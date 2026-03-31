class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for str in strs:
            key = tuple(sorted(str))
    
            map[key].append(str)
            
        
    

        return list(map.values())
