class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_count = Counter(chars)
        length = 0

        for word in words:
            count = Counter(word)
            
            flag = True
            for c in count:
                if count[c] > char_count[c]:
                    flag = False
                    break

            if flag:
                length += len(word)
        
        return length