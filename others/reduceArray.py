from collections import Counter


def minSetSize(self, arr):
    counter = Counter(arr) 
    vals = sorted(counter.values(), reverse=True)
    
    goal = len(arr) // 2
    res = 1
    total = vals[0]
    
    if total >= goal:
        return res
        
    for val in vals[1:]:
        
        if total >= goal:
            return res

        total += val
        res += 1
        
    
    