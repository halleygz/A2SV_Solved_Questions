class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        countChar = Counter(chars)

        len_sum = 0
        
        for w in words:
            countWord = Counter(w)
            if all(countWord[c] <= countChar[c] for c in countWord):
                len_sum+=len(w)
        return len_sum