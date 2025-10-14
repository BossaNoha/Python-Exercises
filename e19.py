class Main:
    def fibonacci(self, number):
        sequence = [0, 1]
        i = 1
        while i < number-1:
            num = sequence[i]+sequence[i-1]
            sequence.append(num)
            i+=1
        return sequence

main = Main()
fibseq = main.fibonacci(10)
print (fibseq)