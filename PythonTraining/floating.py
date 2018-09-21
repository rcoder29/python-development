# to show floating is approximation
# if actual precision needed then use Decimal

type(0.1 + 0.1 + 0.1 - 0.3)
print(0.1 + 0.1 + 0.1 - 0.3)

type(0.1 + 0.1 + 0.1)
print(0.1 + 0.1 + 0.1)


from decimal import *
print(Decimal(".1")+Decimal(".1")+Decimal(".1"))
print(Decimal("0.3"))
