class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        width = len(matrix[0]) - 1
        height = len(matrix)
        lo = 0
        hi = height - 1
        row = -1

        while lo <= hi:
            mid = (lo + hi) // 2
            if matrix[mid][0] <= target <= matrix[mid][width]:
                row = mid
                if matrix[mid][0] == target or matrix[mid][width] == target:
                    return True
                break
            elif matrix[mid][width] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        
        hi = width
        lo = 0
        if row == -1:
            return False

        while lo <= hi:
            mid = (lo + hi) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return False
