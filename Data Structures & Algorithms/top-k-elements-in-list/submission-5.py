class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #new array with index that indicate
        hashmap = {}
        occurences = [[] for i in range (len(nums) + 1)]
        ans = []
        for i in range(len(nums)):
            if nums[i] in hashmap:
                hashmap[nums[i]] = hashmap[nums[i]] + 1
            else:
                hashmap[nums[i]] = 1
        
        for n in hashmap:
            occurences[hashmap[n]].append(n)
        
        for item in reversed(occurences):
            for x in item:
                ans.append(x)
                if len(ans) == k:
                    return ans
