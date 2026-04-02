class Solution:

    #encode: create a string where each string begins with a number#
    #when decoding loop through the string when we hit a 
    #number and a # take the substring and add to array

    #Input: ["neet","code","love","you"]
    #newStr = [4#need4#code4#love]
    #i = 0, newStr[i] = 4, newStr[i+1] = #
    #
    #newList = []
    #

    def encode(self, strs: List[str]) -> str:
        newStr = ""
        for s in strs:
            newStr = newStr + str(len(s)) + "#" + s

        return newStr

    def decode(self, s: str) -> List[str]:
        newList = []

        i = 0
        while i < len(s):
            if s[i].isdigit() and s[i+1] == "#":
                theSubString = s[i+2: i+2 + int(s[i])]
                newList.append(theSubString)
                i = i+2 + int(s[i])



        return newList