# your code goes here!

List = [
    "enlists",
    "google",
    "inlets",
    "banana"
]

class Anagram:
    def __init__( self, word ):
        self.word = word
    
    def get_word( self ):
        return self.get_word
    
    def set_word( self, word ):
            self.word = word
            
    def match(self, word_list):
        return [word for word in word_list if sorted(word) == sorted(self.word)]
        
