def minPairSum(self, nums):
    
    lst=[]
    nums=sorted(nums)
    
    for i in range(len(nums)/2):
        lst.append(nums[i] + nums[-i-1])
    return max(lst)