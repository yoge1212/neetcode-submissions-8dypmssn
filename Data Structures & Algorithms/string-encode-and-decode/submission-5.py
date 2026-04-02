class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs is []:
            return ""
        encodedStr = strs[0]
        for i in range(1, len(strs)):
            encodedStr = encodedStr + "," + strs[i]
        return encodedStr

    def decode(self, s: str) -> List[str]:
        if s is "":
            return []
        decodedStrList = s.split(",")
        return decodedStrList

