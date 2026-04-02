class Solution:

    #we need to design an algorith to encode a list of strings to a string
    #the encoded string will have to be doceded to the original list of strings

    #we need to deconstruct the array of strings to be one whole string
    #then we need to reconstruct the string to be a array of strings
    #we can seperate the strings by a symbol such as #

    #for example : ["the", "blue", "cat"]
    #""
    #the#blue#cat#
    #so when we reach the last word we dont add the hashtag
    #and decoding:
    #""
    #keep looping until we reach a symbol
    #then we add those characters to our array
    #and we keep doing that until we reach the end of the string

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for i in range(len(strs)):
            if i == len(strs) - 1:
                encoded_string += strs[i]
            else:
                encoded_string += (strs[i] + "#")
        
        return encoded_string
                
            
            

    def decode(self, s: str) -> List[str]:

        return s.split('#')
