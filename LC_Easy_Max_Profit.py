def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        profits = 0
        for i in prices:
            if i < min_price:
                min_price = i
            if i - min_price > profits:
                profits = i - min_price
        return profits