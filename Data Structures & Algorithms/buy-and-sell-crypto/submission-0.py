class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprofit=float('inf')
        maxprofit=0
        for i in prices:
            minprofit=min(i,minprofit)
            maxprofit=max(maxprofit,i-minprofit)
        
        return maxprofit
        