class BankAccount:
    def __init__(self, owner, balance, deposit, withdraw):
        self.owner=owner
        self.balance=balance
        self.deposit=deposit
        self.withdraw=withdraw
    def dep(self):
        self.balance+=self.deposit
        self.deposit = 0
        print ("Текущий баланс: " + str(self.balance))
    def withdr(self):
        if self.balance<self.withdraw:
            print ("У вас недостаточно средств.")
        else:
            self.balance-=self.withdraw
            print("Текущий баланс: " + str(self.balance))
        self.withdraw = 0
name = str(input("Напишите свое имя: "))
balance = int(input("Ваш баланс: "))
option = int(input("Выберите опцию: 1.Пополнить 2.Вывести 3.Закрыть "))
while (option != 3):
    if option == 1:
        dep = int(input("Введите количество денег для пополнения: "))
        deping = BankAccount(name, balance, dep, 0)
        deping.dep()
        balance = deping.balance + deping.deposit
        dep = 0
    elif option == 2:
        draw = int(input("Введите количество денег для вывода: "))
        withdrawing = BankAccount(name, balance, 0, draw)
        withdrawing.withdr()
        balance = withdrawing.balance - withdrawing.withdraw
    option = int(input("Выберите опцию: 1.Пополнить 2.Вывести 3.Закрыть "))