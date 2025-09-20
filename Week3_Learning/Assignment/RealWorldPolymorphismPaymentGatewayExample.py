# You are building a payment system that supports multiple payment methods.

# a) Create three classes: CreditCardPayment, PayPalPayment, and BankTransferPayment. b) In each class, define a method process_payment(amount) that prints how the payment is processed. Examples:
#  CreditCardPayment → "Processing credit card payment of $<amount>"
#  PayPalPayment → "Processing PayPal payment of $<amount>"
#  BankTransferPayment → "Processing bank transfer of $<amount>"
# c) Write a function make_payment(payment_method, amount) that accepts an object and calls its process_payment(amount) method.
# d) In the main section:
#  Create one object of each payment class.
#  Call make_payment() with different payment objects to demonstrate polymorphism.

class CreditCardPayment:
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")

class PayPalPayment:
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")

class BankTransferPayment:
    def process_payment(self, amount):
        print(f"Processing bank transfer of ${amount}")

def make_payment(payment_method, amount):
    payment_method.process_payment(amount)

if __name__ == "__main__":
    credit_card = CreditCardPayment()
    paypal = PayPalPayment()
    bank_transfer = BankTransferPayment()
    
    make_payment(credit_card, 100)
    make_payment(paypal, 150)
    make_payment(bank_transfer, 200)