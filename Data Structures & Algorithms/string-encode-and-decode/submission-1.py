class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = strs[0]
        for i in range(1, len(strs)):
            encodedStr = encodedStr + "," + strs[i]
        return encodedStr

    def decode(self, s: str) -> List[str]:
        decodedStrList = s.split(",")
        return decodedStrList

