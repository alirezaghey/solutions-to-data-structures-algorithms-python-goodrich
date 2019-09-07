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

**R-2.10** Implement the neg method for the Vector class of Section 2.3.3, so
that the expression −v returns a new vector instance whose coordinates
are all the negated values of the respective coordinates of v.
[Solution](R-2.10.py)

**R-2.11** In Section 2.3.3, we note that our Vector class supports a syntax such as
v = u + [5, 3, 10, −2, 1], in which the sum of a vector and list returns
a new vector. However, the syntax v = [5, 3, 10, −2, 1] + u is illegal.
Explain how the Vector class definition can be revised so that this syntax
generates a new vector.

**Answer:** In addition to the `__add__` method, the `Vector` class needs to overwrite the `__radd__` method to be able to have a simple list as the left-hand operand in an addition operation with a `Vector`.

The reason is that `__add__` is only invoked on the left-hand operand and when the left-hand operand is a simple list, the default `__add__` method for lists is invoked which does not know how to handle a `Vector` as a right-hand operand. When we implement `__radd__` in `Vector`, execution is given to it after `__add__` in `list` does not know what to do.  
[Solution](R-2.11.py)

**R-2.12** Implement the mul method for the Vector class of Section 2.3.3, so
that the expression v 3 returns a new vector with coordinates that are 3
times the respective coordinates of v.
[Solution](R-2.12.py)

**R-2.13** Exercise R-2.12 asks for an implementation of mul , for the Vector
class of Section 2.3.3, to provide support for the syntax v 3. Implement
the rmul method, to provide additional support for syntax 3 v.
[Solution](R-2.13.py)

**R-2.14** Implement the mul method for the Vector class of Section 2.3.3, so
that the expression u v returns a scalar that represents the dot product of
the vectors, that is, <a href="https://www.codecogs.com/eqnedit.php?latex=\inline&space;\sum_{i=1}^{d}&space;u_{i}&space;\cdot&space;v_{i}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\inline&space;\sum_{i=1}^{d}&space;u_{i}&space;\cdot&space;v_{i}" title="\sum_{i=1}^{d} u_{i} \cdot v_{i}" /></a>
[Solultion](R-2.14.py)

**R-2.15** The Vector class of Section 2.3.3 provides a constructor that takes an in-
teger d, and produces a d-dimensional vector with all coordinates equal to
0. Another convenient form for creating a new vector would be to send the
constructor a parameter that is some iterable type representing a sequence
of numbers, and to create a vector with dimension equal to the length of
that sequence and coordinates equal to the sequence values. For example,
Vector([4, 7, 5]) would produce a three-dimensional vector with coordi-
nates <4, 7, 5>. Modify the constructor so that either of these forms is
acceptable; that is, if a single integer is sent, it produces a vector of that
dimension with all zeros, but if a sequence of numbers is provided, it pro-
duces a vector with coordinates based on that sequence.
[Solution](R-2.15.py)