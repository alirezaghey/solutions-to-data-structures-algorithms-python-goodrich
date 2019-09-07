# Solutions to Chapter one reinforcement exercises

**R-2.1** Give three examples of life-critical software applications.

- Air Traffic Management Software
- Electrical Grid Control Software
- Dam Monitoring and Control Software


**R-2.2** Give an example of a software application in which adaptability can mean
the difference between a prolonged lifetime of sales and bankruptcy.

Word processing software


**R-2.3** Describe a component from a text-editor GUI and the methods that it en-
capsulates.

**R-2.4** Write a Python class, Flower, that has three instance variables of type str,
int, and float, that respectively represent the name of the flower, its num-
ber of petals, and its price. Your class must include a constructor method
that initializes each variable to an appropriate value, and your class should
include methods for setting the value of each type, and retrieving the value
of each type.
[Solution](R-2.4.py)

**R-2.5** Use the techniques of Section 1.7 to revise the charge and make payment
methods of the CreditCard class to ensure that the caller sends a number
as a parameter.
[Solution](R-2.5.py)

**R-2.6** If the parameter to the make_payment method of the CreditCard class
were a negative number, that would have the effect of raising the balance
on the account. Revise the implementation so that it raises a ValueError if
a negative value is sent.
[Solution](R-2.6.py)

**R-2.7** The CreditCard class of Section 2.3 initializes the balance of a new ac-
count to zero. Modify that class so that a new account can be given a
nonzero balance using an optional fifth parameter to the constructor. The
four-parameter constructor syntax should continue to produce an account
with zero balance.
[Solution](R-2.7.py)

**R-2.8** Modify the declaration of the first for loop in the CreditCard tests, from
Code Fragment 2.3, so that it will eventually cause exactly one of the three
credit cards to go over its credit limit. Which credit card is it?

**Answer:** By changing the upper bound of the for loop to 59, the third wallet
will go over its limit when the loop variable reaches 58.
[Solution](R-2.8.py)


**R-2.9** Implement the sub method for the Vector class of Section 2.3.3, so
that the expression u−v returns a new vector instance representing the
difference between two vectors.
[Solution](R-2.9.py)