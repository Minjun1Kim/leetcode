from collections import deque

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
        
    def getImportance(self, employees: List['Employee'], id: int) -> int:

        id_map = {}

        for emp in employees:
            id_map[emp.id] = [emp.id, emp.importance, emp.subordinates]

        queue = deque()
        queue.append(id_map[id])
        seen = {id}
        score = 0

        while queue:
            curr = queue.popleft()
            score += curr[1]
            seen.add(curr[0])

            for employee in curr[2]:
                if employee not in seen:
                    queue.append(id_map[employee])

        return score
        
