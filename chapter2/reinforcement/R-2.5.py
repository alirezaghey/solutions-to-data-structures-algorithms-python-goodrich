# R-2.5 Use the techniques of Section 1.7 to revise the charge and make_payment
# methods of the CreditCard class to ensure that the caller sends a number
# as a parameter.


class CreditCard:
    """A consumer credit card."""

    def __init__(self, customer: str, bank: str, acnt: str, limit: float):
        """
        Create a new credit card instance.

        The initial balance is zero.

        customer    the name of the customer (e.g., John Bowman )
        bank        the name of the bank (e.g., California Savings )
        acnt        the acount identifier (e.g., 5391 0375 9387 5309 )
        limit       credit limit (measured in dollars)
        """
        self.customer = customer
        self.bank = bank
        self.account = acnt
        self.limit = limit
        self.balance = 0

    def get_customer(self) -> str:
        """Return name of the customer."""
        return self.customer

    def get_bank(self) -> str:
        """Return the bank s name."""
        return self.bank

    def get_account(self) -> str:
        """Return the card identifying number (typically stored as a string)."""
        return self.account

    def get_limit(self) -> float:
        """Return current credit limit."""
        return self.limit

    def get_balance(self) -> float:
        """Return current balance."""
        return self.balance

    def charge(self, price: float) -> bool:
        """
        Charge given price to the card, assuming sufficient credit limit.
        Return True if charge was processed; False if charge was denied.
        """
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be numeric!")

        if price + self.balance > self.limit:       # if charge would exceed limit,
            return False                            # cannot accept charge

        else:
            self.balance += price
            return True

    def make_payment(self, amount: float):
        """Process customer payment that reduces balance."""
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be numeric!")

        self.balance -= amount

    # Overriding builtin methods
    def __str__(self):
        return f"""
        {self.get_customer()} has account {self.get_account()} with {self.get_bank()}.
        The account has a balance of {self.get_balance()} and a limit of {self.get_limit()}.
        *********************************************************************************
                """


if __name__ == "__main__":
    card = CreditCard("azgh", "some Bank", "666 999 333", 1000)
    print(card)
    card.charge(100)
    print(card)
    card.make_payment(50)
    print(card)
    # card.make_payment("50")  # raise TypeError
    # card.charge("hello")  # raise TypeError
