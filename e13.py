class Main:
    def filtnum(self, numbers):
        newList = []
        for num in numbers:
            if num > 0:
                num *=2
                newList.append(num)
        return newList
        
main = Main()
newList = main.filtnum([-3, 5, 0, 7, -1])
print (newList)