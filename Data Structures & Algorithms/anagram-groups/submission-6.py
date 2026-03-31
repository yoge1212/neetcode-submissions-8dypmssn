class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        str_to_dict = defaultdict(list)


        for str in strs:
            temp = [0] * 26
            for c in str:
                temp[ ord('a') - ord(c)] += 1

            str_to_dict[tuple(temp)].append(str)


        return list(str_to_dict.values())

        