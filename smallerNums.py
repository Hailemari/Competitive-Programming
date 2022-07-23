def smallerNumbersThanCurrent(self, nums):
    nums_len = len(nums)
    listCount = [0] * nums_len
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] > nums[j]:
                listCount[i] += 1
        
    return listCount