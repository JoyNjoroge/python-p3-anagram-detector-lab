# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, word_list):
        matches = []
        original_sorted = sorted(self.word)

        for w in word_list:
            if sorted(w.lower()) == original_sorted:
                matches.append(w)

        return matches
    
listen = Anagram("listen")
result = listen.match(['enlists', 'google', 'inlets', 'banana'])
print(result)  # ['inlets']

