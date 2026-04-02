class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        thelist = []
        for n in nums:
            map[n] = map.get(n, 0) + 1
        sortedlist = sorted(map.values())[-k:]
        for key in map:
            for n in sortedlist:
                 if map[key] == n:
                     thelist.append(key)
               

        return thelist