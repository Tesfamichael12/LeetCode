class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse=True)
        print(tasks)
        mintime = k = 0
        for i in range(len(processorTime)):
            time = processorTime[i] + tasks[k]
            mintime = max(mintime, time)
            k += 4

        return mintime