from collections import deque



class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_deque = deque()
        max_deque = deque()

        leftPointer = 0
        rightPointer = 0

        answer = 0
        while rightPointer < len(nums):
            while min_deque and nums[rightPointer] <= nums[min_deque[-1]]:
                min_deque.pop()
            while max_deque and nums[rightPointer] >= nums[max_deque[-1]]:
                max_deque.pop()
            min_deque.append(rightPointer)
            max_deque.append(rightPointer)
            
            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                leftPointer += 1
                if leftPointer > min_deque[0]:
                    min_deque.popleft()
                if leftPointer > max_deque[0]:
                    max_deque.popleft()
            
            answer = max(answer, rightPointer - leftPointer + 1)
            rightPointer += 1
                
        return answer