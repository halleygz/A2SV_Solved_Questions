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
        emp_map = {emp.id: emp for emp in employees}

        queue = [id]
        total = 0

        while queue:
            emp_id = queue.pop(0)
            emp = emp_map[emp_id]

            total += emp.importance

            for sub in emp.subordinates:
                queue.append(sub)

        return total