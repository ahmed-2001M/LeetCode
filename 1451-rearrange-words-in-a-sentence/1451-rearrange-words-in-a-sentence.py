class Solution:
    def arrangeWords(self, text: str) -> str:
        text = text.split(' ')
        text = sorted(text,key = lambda x:len(x))
        res = ' '.join(text)
        res = res.lower()
        return res.capitalize()