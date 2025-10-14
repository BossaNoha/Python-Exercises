class Main:
    def sort_scores(self, results):
        sortedic=dict (sorted(results.items(), key=lambda item: item[1], reverse = True))
        return sortedic


main = Main()
sort_scores = main.sort_scores({"Alice": 85, "Bob": 42, "Charlie": 73, "Diana": 90})
print (sort_scores)