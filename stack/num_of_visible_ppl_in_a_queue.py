class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        
        n = len(heights)

        res = [0]*n
        stack = []
        for i in range(n-1, -1, -1):

            # count each shorter person popped
            while stack and heights[i] > stack[-1]:
                stack.pop()
                res[i] += 1
            
            # count the first taller/equal person (the blocker)
            if stack:
                res[i] += 1

            stack.append(heights[i])

        return res
