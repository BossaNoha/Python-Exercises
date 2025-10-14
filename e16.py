class Main:
    def primes(self, numbers):
        primes_list = []
        for num in numbers:
            x = 2
            while x < num:
                if num %x == 0:
                    break
                x +=1
            else: 
                primes_list.append(num)
        return primes_list
    
main = Main()
primes_list = main.primes([3, 2, 6, 1, 10])
print(primes_list)
bonus = len(primes_list)
print(bonus)