class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        thelist = []
        for n in nums:
            if n in map:
                
                map[n] = map[n] + 1
                if map[n] == k:
                    thelist.append(n)

            else:
                map[n] = 1
                if map[n] == k:
                    thelist.append(n)
        return thelist