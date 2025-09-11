class Payment():
    def __init__(self,amount):
        self.amount=amount

class CashPayment(Payment):
    def pay(self):
        print("Paid Rs.",self.amount,"in cash")

class CardPayment(Payment):
    def pay(self):
        print("Paid Rs.",self.amount,"using credit/debit")
    
class UPIPayment(Payment):
    def pay(self):
        print("Paid Rs.",self.amount,"using UPI")

cash=CashPayment(1000)
card=CardPayment(1000)
upi=UPIPayment(1000)

cash.pay()
card.pay()
upi.pay()