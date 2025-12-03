class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, words):
        return [word for word in words if sorted(word.lower()) == sorted(self.word.lower())]