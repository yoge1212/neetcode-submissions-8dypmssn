class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #we can iterate over the whole array of prices
        #keep track of the lowest price before our current index and substract it from each value
        #keep track of the most profit and change it when needed
        
        profit = 0
        lowestPrice = prices[0]
        for i in range(len(prices)):
            
            if i != 0:
                if prices[i] - lowestPrice > profit:
                    profit = prices[i] - lowestPrice
                if prices[i] < lowestPrice:
                    lowestPrice = prices[i]
        
        return profit
                
            
        