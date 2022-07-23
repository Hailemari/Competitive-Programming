def sortColors(self, nums):
        
        start = 0 
        end = len(nums)-1
        i = 0
        while  end >= i:
            if nums[i] == 0:
                nums[start], nums[i] = nums[i], nums[start]
                start += 1 
                i += 1
            elif nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                nums[i], nums[end] = nums[end], nums[i]
                end -= 1
        return