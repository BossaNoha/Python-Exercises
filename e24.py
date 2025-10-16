class Main:
    def BankAccount(self, account_name, deposit, withdraw):
        balance = self.BankActions(balance, deposit, withdraw)
        if balance < 0:
            output = "Insufficient funds"
        else: output = {"Account holder" : account_name, "Balance" : balance}
        return output

    def BankActions(self, balance, deposit, withdraw):
        balance = balance + deposit - withdraw
        return balance

main = Main()
bank = main.BankAccount("Alice", 100, 30)
print (bank)
