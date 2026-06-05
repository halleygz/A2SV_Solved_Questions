class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = {}

        for word in words:
            freq[word] = freq.get(word, 0) + 1

        unique_words = sorted(freq.keys(), key=lambda w: (-freq[w], w))
        
        return unique_words[:k]