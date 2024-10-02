# your code goes here!
class Anagram:

    def __init__(self, word):
        self.word = word


    def match(self, candidates):
        matches = []
        for candidate in candidates:
            if sorted(candidate) == sorted(self.word):
                matches.append(candidate)
        return matches