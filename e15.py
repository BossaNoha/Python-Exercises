class Main:
    def is_palindrome(self, is_it_or_not):
        is_it_or_not = is_it_or_not.lower()
        not_or_it_is = []
        for letter in is_it_or_not:
            not_or_it_is.insert(0, letter)
        
        if is_it_or_not == not_or_it_is:
            return True
        else:
            return False

main = Main()
palindrome = main.is_palindrome("Aloha")
print (palindrome)