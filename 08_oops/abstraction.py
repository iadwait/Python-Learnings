from abc import ABC, abstractmethod

#Step 1 - Create an abstract class
class Payment(ABC):
    def pay(self, amount):
        # Common steps visible to the user
        print("Checking Account Balance")
        print("Verifying payment details")

        # Hiding implementation in subclass
        self.process_payment(amount) # The parent class abstract method is never called; self.process_payment(amount) calls the subclass’s method.

        print("Payment Completed !!")

    @abstractmethod
    def process_payment(self, amount):
        # Declared in abstract class, implemented in subclass
        pass

#Subclass 1
class CreditCard(Payment):
    def process_payment(self, amount):
        # Subclass provides the actual implementation
        print(f"Paid {amount} using Credit Card")

#Subclass 2
class UPI(Payment):
    def process_payment(self, amount):
        # Subclass provides its own implementation
        print(f"Paid {amount} using UPI")

# Usage
payment1 = CreditCard()
payment1.pay(500)

payment2 = UPI()
payment2.pay(300)