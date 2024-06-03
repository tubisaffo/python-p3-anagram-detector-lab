# your code goes here!

def is_match (word, anagram):
    if len(word) != len(anagram):
        return False
    
    char_count = {}
    for char in word:
        char_count[char] = char_count.get(char, 0) + 1
        
    anagram_count = {}
    for char in anagram:
       anagram_count[char] = anagram_count.get(char, 0) + 1
       
    return char_count == anagram_count
class Anagram:
    
    def __init__(self, word):
        self.word = word
    
    def match(self, words):
        return [word for word in words if is_match( self.word, word )]    