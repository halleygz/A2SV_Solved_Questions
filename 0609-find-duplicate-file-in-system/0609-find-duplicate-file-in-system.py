class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dict = {}
        for path in paths:
            parts = path.split(" ")
            dir = parts[0]
            for file in parts[1:]:
                name, content = file.split("(")
                content =  content[:-1]
                full_path = dir + "/" + name
                dict.setdefault(content, []).append(full_path)
        return [group for group in dict.values() if len(group) > 1]