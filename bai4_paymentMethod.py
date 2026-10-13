import random
from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):  #lớp trừu tượng
        pass

class Cash(PaymentMethod):
    def pay(self, amount):
        if amount < 0:
            raise ValueError('Invalid amount')
        else:
            return f'Paid {amount:,} VNĐ in cash'  

class CreditCard(PaymentMethod):
    FEE = 0.02
    def __init__(self, card_number):
        self.card_number = card_number

    def pay(self, amount):
        if amount < 0:
            raise ValueError('Invalid amount')
        
        phi = amount * self.FEE #tính phí
        #che số thẻ
        return f"Paid {amount + phi :,} by card **** {''.join(self.card_number[-4:])}"  #lấy ra 4 phần tử cuối chuỗi

class Ewallet(PaymentMethod):
    def __init__(self,balance):
        self.balance = balance

    def pay(self, amount):
        if amount < 0:
            raise ValueError('Invalid amount')  #số tiền ko hợp lệ
        elif amount > self.balance:
            raise ValueError('Insufficient funds')  #ko đủ số dưS
        else:
            self.balance -= amount #thanh toán 
            return f'paid {amount:,} by e-wallet, remaining {self.balance}'


#chạy
def checkout(method, amount):
    print(method.pay(amount))

"""
Note: method là phương thức, amount là số tiền/ trong trường hợp này method sẽ gọi tên class, amount sẽ đại
diện số tiền, giúp gọi tắt
"""
#thanh toán tiền mặt
checkout(Cash(), 200000)

#thanh toán qua thẻ
number_card = ''
for x in range(1,17):
    number_card += str(random.choice(range(1,10)))

checkout(CreditCard(number_card), 200000)

#thanh toán qua ví
checkout(Ewallet(500000), 200000)
