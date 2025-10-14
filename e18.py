class Main:
    def word_frequency(self, sentence):
        words = sentence.lower()
        words = words.split()
        seen = {}
        for word in words:
            if word in seen:
                seen[word] = seen[word]+1
            else: 
                seen[word] = 1
        return seen

main = Main()
frequenter = main.word_frequency("The cat and the dog and the cat")
print (frequenter)