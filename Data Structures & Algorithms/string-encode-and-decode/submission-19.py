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
            j = i
            while s[j] != '#':
                j += 1

            length = int(s[i:j])

            newList.append(s[j+1: j+1 + length])
            i = j+1 + length



        return newList