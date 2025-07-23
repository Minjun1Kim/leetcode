import heapq

class MedianFinder:

    def __init__(self):
        self.left = [] # 1, ..., k elements
        self.right = [] # k+1, ..., n elements

    def addNum(self, num: int) -> None:
        
        if not self.left or num <= -self.left[0]:
            heapq.heappush(self.left, -num)
        else:
            heapq.heappush(self.right, num)
        
        if len(self.left) > len(self.right) + 1:
            heapq.heappush(self.right, -heapq.heappop(self.left))
        elif len(self.right) > len(self.left):     # right bigger
            heapq.heappush(self.left, -heapq.heappop(self.right))

        
    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        else:
            return (self.right[0] + (-1 * self.left[0])) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
