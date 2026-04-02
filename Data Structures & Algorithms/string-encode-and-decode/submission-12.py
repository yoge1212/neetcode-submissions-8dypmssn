class Solution:

    #encode a list of strings to a single string
    # we need to take the array of strings and convert it to one string
    # use a symbol to seperate the strings
    # example ["neet,code", "love", "code"]
    # we use a number with a indentifier
    #newString = "9#neet,code4#love#code
    #newList = [""]

    def encode(self, strs: List[str]) -> str:
        newString = ""
        for i in range(len(strs)):
            newString = newString + str(len(strs[i])) + "#" + strs[i]
        return newString
            

    def decode(self, s: str) -> List[str]:
        newList = []
        for i in range(len(s)):
            if i != len(s) -1:
                if s[i].isdigit() and s[i+1] == '#':
                    newString = s[i+2:i+2 + int(s[i])]
                    newList.append(newString)
                    i = i+2 + int(s[i])


        return newList
        

