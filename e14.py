class Main:
    def string_analyze(self, sentence):
        sentencelenght = len(sentence)
        words = len(sentence.split())
        vowels, consonants = self.char_analyze(sentence)
        stats = {
            "characters" : sentencelenght,
            "words" : words,
            "vowels" : vowels,
            "consonants" : consonants
        }
        return stats
    
    def char_analyze(self, sentence):
        vowels = []
        consonants = []
        for letter in sentence:
            if letter in "aeiouy":
                vowels.append(letter)
            elif letter not in " ":
                consonants.append(letter)
        return vowels, consonants


main = Main()
stats = main.string_analyze("Hello world")
print (stats)