class Solution:

    #encode a list of strings to a single string
    # we need to take the array of strings and convert it to one string
    # use a symbol to seperate the strings
    # 

    def encode(self, strs: List[str]) -> str:
        newString = ""
        for i in range(len(strs)):
            if i == len(strs) - 1:
                newString = newString + strs[i]
            else:
                newString = newString + strs[i] + ","
        return newString
            

    def decode(self, s: str) -> List[str]:
        newList = s.split(",")
        return newList
        

