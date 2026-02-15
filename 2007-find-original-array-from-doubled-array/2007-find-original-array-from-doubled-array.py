class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        # if an element if the original element is duplicated then the changed one will also have duplicated
        # use count of changed to get the number of times a number is present
        # 1:1, 3:1 4:1 2:1 6:1 8:1 len(changed) / 2 = len(original)
        # if dict[num[num]] in dict append to org, else skip. if len(changed) == 2len(original) return original else return []
        # if count(changed)[num] == 2 append num to org two times

        count = Counter(changed)
        originalList = []

        for num in sorted(changed):
            if count[num] == 0:
                continue
            if count[2*num] == 0:
                return []
            if num == 0 and count[num] <= 1:
                return []
            originalList.append(num)
            count[num] -= 1
            count[2*num] -= 1 
        return originalList
