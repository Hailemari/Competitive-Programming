import collections
import itertools
import math


def shortestSubarray(self, nums: List[int], k: int) -> int:

    q = collections.deque()  
    ans = math.inf
    pref = [*itertools.accumulate([0] + nums)]

    for i, n in enumerate(pref):
        while q and pref[q[-1]] >= n:
            q.pop()
        while q and n - pref[q[0]] >= k:
            ans = min(ans, i - q.popleft())
        q += i,
    if ans != math.inf:
        return ans 
    else:
        return -1