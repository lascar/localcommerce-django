# TODO

## [BAD_SMELL](BAD_SMELL.md)

## [SCRATCHPAD](SCRATCHPAD.md)

* user role as admin and user

* user can mark a product of interest
Products of interest will be a relation many to many.
The UserProduct model has a boolean 'mailling' for warning the user when
 an offer is made nearby on that product

* user can make offers (on his products of interest)

* * within each offer can be included

* * *  other offers (as component)

* * and can be (as leaf)

* * * a product (with variety, observation...)

* * * * quantity available

* * * * unit price on site (with and without vat)

* * * * date of start (defaut today)

* * * * date of end (is not precised and valid True defaulted at today + one day)

* * * possibility of delivery and an average of the additional cost for delivery

* user can see offers (based on his products of interest)

* user can see his orders

* user can see orders on his offers

* user can see his offers and the orders on his offers

* user can make orders based on existing offers

* * within each order there is

* * * the identifier of the offer referenced

* * * the concerned offer_line (with variety, aspect...) of the offer with

* * * * the required quantity

* * * date of order

* * * delivery and location

* * * wished date of delivery

## [README](README.md)

