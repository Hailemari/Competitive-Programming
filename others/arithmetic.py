def checkArithmeticSubarrays(self, nums, l, r):
        
    answer = []
    
    for i in range(len(l)):

        arr = sorted(nums[l[i]:r[i]+1])
        count = 1
        diff = arr[1] - arr[0]

        for j in range(1, len(arr)):
            if arr[j] - arr[j-1] != diff:
                answer.append(False)
                count = 0
                break

        if count:
            answer.append(True)
            
    return answer