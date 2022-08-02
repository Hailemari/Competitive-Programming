import collections


class Solution:
    def leastInterval(self, tasks, n):

        tasksCounter = list(collections.Counter(tasks).values())
        maxCounter = max(tasksCounter)
        maxCounterTasks = tasksCounter.count(maxCounter)

        return max(len(tasks), (maxCounter-1)*(n+1)+maxCounterTasks)