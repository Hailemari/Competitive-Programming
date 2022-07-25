def maxCoins(self, piles):
    piles = sorted(piles, reverse=True)
    
    max = 0
    for i in range(1, len(piles) // 3 * 2, 2):
        max += piles[i]
    
    return max