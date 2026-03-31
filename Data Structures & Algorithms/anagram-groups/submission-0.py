class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for str in strs:
            key = tuple(sorted(str))
            if key in map:
                map[key].append(str)
            else:
                map[key] = [str]
        
    

        return list(map.values())
