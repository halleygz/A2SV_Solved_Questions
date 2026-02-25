class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        separated = s.strip().split()
       
        if len(pattern) != len(separated):
            return False

        container = {}
        used = set()


        for ch, word in zip(pattern, separated):
            if ch in container:
                if container[ch] != word:
                    return False
            else:
                if word in used:
                    return False
                container[ch] = word
                used.add(word)

        return True