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
            encoded_string += (str(len(strs[i])) + "#" + strs[i])
        print(encoded_string)
        
        return encoded_string
                
            
            #"5Hello"
            #

    def decode(self, s: str) -> List[str]:
        decoded_strings = []
        i = 0
        while i < len(s):
            length_of_str = ""
            while s[i] != "#":
                length_of_str += s[i]
                i += 1
            

            decoded_strings.append(s[i+1:i + 1 + int(length_of_str)])
            i = i + 1 + int(length_of_str)

        return decoded_strings



       
