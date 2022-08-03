
def dailyTemperatures(self, nums: 'List[int]') -> 'List[int]':
    
    result = [0] * len(nums)
    stack = []
    for i in range(len(nums)):
        while stack and nums[i] > nums[stack[-1]]: #find the higher
            cur = stack.pop()
            result[cur] = i - cur
        stack.append(i)  

    return result