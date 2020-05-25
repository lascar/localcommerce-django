# TODO

## [BAD_SMELL](BAD_SMELL.md)

## [SCRATCHPAD](SCRATCHPAD.md)

* user role as admin and user

* user can mark a product of interest
Products of interest will be a relation many to many.

Real products are products with one variety (or none), one aspect (or none)...
 defined.
Theys are used in offers and orders.
Offers and Orders have a relation many to one with them.

After defined offer and order, we will defined products of interest (so offer
 and order have no filter restriction at this point (a user see all without
 filtering his interests).


* user can make offers (on his products of interest)

* * within each offer there is

* * * concrete products (with variety, aspect...)

* * * * quantity available

* * * * unit price on site (with and without vat)

* * * * date of start, date of end

* * * possibility of delivery and an average of the additional cost for delivery

* user can see his offers and the orders on his offers

* user can make orders (on his products of interest) based on existing offers

* * within each order there is

* * * the identifier of the offer referenced

* * * the concerned concrete products (with variety, aspect...) of the offer

* * * * the required quantity

* * * date of order

* * * delivery and location

* * * wished date of delivery

## [README](README.md)

