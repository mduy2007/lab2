#class BankAccount
import time

class BankAccount:
    def __init__(self, owner, balance = 0):
        self.__owner = owner
        self.__balance = balance

        self.__history = []

    def deposit(self,amount):
        seconds = time.time()
        self.local_time = time.ctime(seconds)

        if amount < 0:
            return "Số tiền không hợp lệ"

        else:
            self.__balance += amount
            self.__history.append({'Type': 'deposit','Value': amount, 'Time': self.local_time})

        pass
    
    def withdraw(self,target,amount):
        if amount < 0:
            return "Số tiền không hợp lệ"

        else:
            target.__balance += amount
            self.__balance -= amount
            self.__history.append({'Type': 'withdraw','Value': amount,'Member 1': self.__owner, 'Member 2': target.__owner, 'Time': self.local_time})

        pass
    def get_balance(self):
        return f"Số dư hiện có: {self.__balance}"

    def get_history(self):
        return f'Lịch sử giao dịch:\n{self.__history}\n'


if __name__ == "__main__":
    acc1 = BankAccount('Duy',1000)
    acc2 = BankAccount('An', 3000)
    acc3 = BankAccount('Ngọc', 5000)

    acc1.deposit(5000)
    acc2.deposit(1000)
    acc3.deposit(3000)

    acc1.withdraw(acc2, 2000)
    acc3.withdraw(acc1, 1000)

    print(acc1.get_balance())
    print(acc2.get_balance())
    print(acc3.get_balance())

    print(acc1.get_history())
    print(acc2.get_history())
    print(acc3.get_history())

    try:
        acc1.withdraw(5000)

    except ValueError as e:
        print("Lỗi:", e)

    print(hasattr(acc1, "__balance"))