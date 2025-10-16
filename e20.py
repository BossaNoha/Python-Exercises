class Main:
    def merge_and_sort(self,listA,listB):
        combined = listA + listB
        sortedlist = list(set(combined))
        sortedlist.sort()
        return sortedlist



main = Main()
mes = main.merge_and_sort([3, 1, 2], [5, 3, 4])
print (mes)