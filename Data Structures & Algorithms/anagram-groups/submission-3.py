class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        str_to_dict = defaultdict(list)


        for str in strs:
            total = 0
            for c in str:
                total += ord(c)

            str_to_dict[total].append(str)


        return list(str_to_dict.values())

        