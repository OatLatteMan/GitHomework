class Bank_Account:
    def __init__(self, num, holder, status):
        self.num = num
        self.holder = holder
        self.status = status

    def withdrawal(self, status):
        if self.status >= status:
            self.status -= status
        else:
            raise Exception('You have insufficient funds')

    def deposit(self, status):
        self.status += status

    def acc_status(self):
        print(f'Account holder: {self.holder}')
        print(f'Account number: {self.num}')
        print(f'Available amount: {self.status}')

dima = Bank_Account(3066379360300, 'Dima', 23000)
sasha = Bank_Account(4177480801311, 'Sasha', 12000)

dima.acc_status()
sasha.acc_status()

dima.withdrawal(7000)
dima.deposit(14600)

sasha.withdrawal(13500)
sasha.deposit(7300)

dima.acc_status()
sasha.acc_status()