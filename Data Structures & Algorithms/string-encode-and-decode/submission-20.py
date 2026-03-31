class Solution:

    #take the list of strs
    #concatante currentStr + len(str[i]) + "#" + str[i] 
    #when decoding:
    #we know the first character will be a number we loop through until we hit "#".
    #that will be the length of the string. we can then slice the string to extract.
    #repeat the steps above from the last index of string we extract + 1
    #'' 
    # 4 + # + neet
    #4#neet + 4 + # + code
    #

    def encode(self, strs: List[str]) -> str:
        result = ''
        for string in strs:
            result += str(len(string)) + '#' + string
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            lenOfString = ''
            while s[i] != '#':
                lenOfString += s[i]
                i += 1
                
            
            result.append(s[i+1:i+1+int(lenOfString)])
            i = i+1+int(lenOfString)
        
        return result

