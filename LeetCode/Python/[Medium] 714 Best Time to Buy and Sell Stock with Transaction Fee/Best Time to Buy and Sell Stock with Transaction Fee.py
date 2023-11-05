class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # 마지막으로 물건을 샀을 때의 최대 수익금
        buy = -sys.maxsize
        # 마지막으로 물건을 팔았을 때의 최대 수익금
        sell = 0

        # 물건 가격
        for price in prices:
            buy = max(buy, sell - price)
            sell = max(sell, buy + price - fee)

        return sell