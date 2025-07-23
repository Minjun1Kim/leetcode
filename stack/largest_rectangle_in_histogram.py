class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        len_heights = len(heights)

        for i in range(len_heights):
            
            start = i
            
            while stack and stack[-1][1] > heights[i]:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
                
            stack.append((start, heights[i]))

        for item in list(stack):
            area = (len_heights - item[0]) * item[1]
            if area > maxArea:
                maxArea = area

        return maxArea
