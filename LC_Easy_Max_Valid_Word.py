def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        dic = defaultdict(int)
        banned.append("")
        max_word = ("", 0)
        for c in string.punctuation:
            paragraph = paragraph.replace(c, " ")
        for i in paragraph.lower().split(" "):
            if i.strip() not in banned:
                dic[i] += 1
                curr_val = dic[i]
                if curr_val >= max_word[1]:
                    max_word = (i, curr_val)
        return max_word[0]
                