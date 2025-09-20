import heapq

class Solution:
    def nearlySorted(self, arr, k):
        #code
        n = len(arr)
        if k == 0:
            return arr
        if k == n:
            arr.sort()
            return arr
            
        index = 0
        heap = []    
        for i in range(n):
            if k >= 0:
                k -= 1
                heapq.heappush(heap, arr[i])
            else:
                arr[index] = heapq.heappop(heap)
                index += 1
                heapq.heappush(heap, arr[i])

        while heap:
            arr[index] = heapq.heappop(heap)
            index += 1

