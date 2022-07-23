def targetIndices(self, nums, target):
       
        sorted_num = sorted(nums)
        lst_len = len(sorted_num)
        ans = []
        
        for i in range(lst_len):
            if sorted_num[i] == target:
                ans.append(i)
            
        return ans