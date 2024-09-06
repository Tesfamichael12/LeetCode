class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort(reverse=True)
        tasks.sort()
        print(processorTime)
        mintime = k = 0
        for i in range(len(processorTime)):
            time = processorTime[i] + tasks[k+3]
            mintime = max(mintime, time)
            k += 4

        return mintime