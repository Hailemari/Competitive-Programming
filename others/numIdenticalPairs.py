def numIdenticalPairs(self, nums):
    numSet = set(nums)
    numPairs = 0
    for i in numSet:
        j = nums.count(i)
        if j == 1:
            pass
        else:
            numPairs += j*(j-1)//2
    return numPairs 