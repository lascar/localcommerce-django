# TODO

## [BAD_SMELL](BAD_SMELL.md)

## [SCRATCHPAD](SCRATCHPAD.md)

## NOW
offer simple

## ALL FEATURES
* user role as admin and user

* user can mark a product of interest
Products of interest will be a relation many to many.
The UserProduct model has a boolean 'mailling' for warning the user when
 an offer is made nearby on that product

* product has name, brands, varieties, aspects, size, calibers and packgagings

* concrete_product has a product_id, the name of the product, can have one of
 the brands, one of the varieties... of the product

* offer has one concrete_product, user, unit_quantity, unit_price, date_start, a possible
 date_end, code_postal (is put by the user or comes from the shop or from the
  user), localization (that is comes from the code postal), and a valid
  attribute (serves to invalidate an offer when start_end is passed)

* order has one user, offers that come all from the same user making offer,
  concret_products and each has unit_quantity (can not be bigger that the offer one)
  code_postal (is put by the user or from the one of the user)

* user can make offers (on his products of interest)

* * within each is included

* * the user who makes the offer

* * a product (with variety, observation...)

* * quantity available

* * unit price on site (with and without vat)

* * date of start (defaut today)

* * date of end (is not precised and valid True defaulted at today + one day)

* * possibility of delivery and an average of the additional cost for delivery

* user can see offers (based on his products of interest)

* user can see his orders

* user can see orders on his offers

* user can see his offers and the orders on his offers

* user can make orders based on existing offers

* * within each order there is

* * the user who places the order

* * the identifier of the offer referenced

* * the required quantity

* * date of order

* * delivery and location

* * wished date of delivery

## [README](README.md)

