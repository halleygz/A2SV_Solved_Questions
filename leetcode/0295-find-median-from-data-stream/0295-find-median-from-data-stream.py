from heapq import heappush, heappop, heapify

class MedianFinder:

    def __init__(self):
        self.upper_heap = []
        self.lower_heap = []
        heapify(self.upper_heap)
        heapify(self.lower_heap)

    def addNum(self, num: int) -> None:
        if not self.upper_heap:
            heappush(self.upper_heap, num)
        else:
            upper_curr = self.upper_heap[0]
            if num >= upper_curr:
                heappush(self.upper_heap, num)
            else:
                heappush(self.lower_heap, -num)
        
        if len(self.upper_heap) > len(self.lower_heap) + 1:
            upper_curr = heappop(self.upper_heap)
            heappush(self.lower_heap, - upper_curr)
        elif len(self.lower_heap) > len(self.upper_heap) + 1:
            lower_curr = heappop(self.lower_heap)
            heappush(self.upper_heap, - lower_curr)

    def findMedian(self) -> float:
        if len(self.upper_heap) > len(self.lower_heap):
            return self.upper_heap[0]
        elif len(self.lower_heap) > len(self.upper_heap):
            return - self.lower_heap[0]
        else:
            return (self.upper_heap[0] - self.lower_heap[0]) /2 

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()