# R-2.7 The CreditCard class of Section 2.3 initializes the balance of a new ac-
# count to zero. Modify that class so that a new account can be given a
# nonzero balance using an optional fifth parameter to the constructor. The
# four-parameter constructor syntax should continue to produce an account
# with zero balance.


class CreditCard:
    """A consumer credit card."""

    def __init__(self, customer: str, bank: str, acnt: str, limit: float, balance=0):
        """
        Create a new credit card instance.

        The initial balance is zero.

        customer    the name of the customer (e.g., John Bowman )
        bank        the name of the bank (e.g., California Savings )
        acnt        the acount identifier (e.g., 5391 0375 9387 5309 )
        limit       credit limit (measured in dollars)
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = balance

    def get_customer(self) -> str:
        """Return name of the customer."""
        return self._customer

    def get_bank(self) -> str:
        """Return the bank s name."""
        return self._bank

    def get_account(self) -> str:
        """Return the card identifying number (typically stored as a string)."""
        return self._account

    def get_limit(self) -> float:
        """Return current credit limit."""
        return self._limit

    def get_balance(self) -> float:
        """Return current balance."""
        return self._balance

    def charge(self, price: float) -> bool:
        """
        Charge given price to the card, assuming sufficient credit limit.
        Return True if charge was processed; False if charge was denied.
        """
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be numeric!")

        if price + self._balance > self._limit:       # if charge would exceed limit,
            return False                            # cannot accept charge

        else:
            self._balance += price
            return True

    def make_payment(self, amount: float):
        """Process customer payment that reduces balance."""
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be numeric!")
        if amount < 0:
            raise ValueError("Amount can't be less than zero!")

        self._balance -= amount

    # Overriding builtin methods
    def __str__(self):
        return f"""
        {self.get_customer()} has account {self.get_account()} with {self.get_bank()}.
        The account has a balance of {self.get_balance()} and a limit of {self.get_limit()}.
        *********************************************************************************
                """


if __name__ == "__main__":
    cardWithDefaultInitialBallance = CreditCard(
        "azgh", "some Bank", "666 999 333", 1000)
    print(cardWithDefaultInitialBallance)
    cardWithDefaultInitialBallance.charge(100)
    print(cardWithDefaultInitialBallance)
    cardWithDefaultInitialBallance.make_payment(50)
    print(cardWithDefaultInitialBallance)

    cardWithCustomizedInitialBallance = CreditCard(
        "ozgh", "American Express", "666 888 999", 1000, 500)
    print(cardWithCustomizedInitialBallance)
