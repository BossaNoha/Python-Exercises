class Main:
    def most_frequent(self,given_list):
        countingdic = {}
        for num in given_list:
            if num in countingdic:
                countingdic[num] += 1
            else:
                countingdic[num] = 1
        most_frequented = max(countingdic.items(), key=lambda item: item[1])
        return most_frequented



main = Main()
mf = main.most_frequent([1, 2, 2, 3, 3, 3])
print (mf)