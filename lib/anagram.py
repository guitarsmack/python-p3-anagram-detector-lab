# your code goes here!
class Anagram:

    def __init__(self,word):
        self.word = word
        self.list = list()
    
    def match(self,word_list):
        for w in word_list:
            match = True
            for letter in w:
                if letter in self.word:
                    match = True
                else:
                    match = False
                    break
            if match == True:
                self.list.append(w)
        return self.list
