# Scratchpad for quick notes
Idealy Offer would be a composite that holds other offers (component)
 or the fields an offer (leaf).
Offer had a user a location auto (come from user or from itself), product,
 quantity, price...

Location are given by postal code (see tools_box)
But for now, Location are in the freeze.

I'm not sure of this...
the user's products_of_interest field is a many to many. A user has a many to
 many relationship with the products. The UserProduct model has a email boolean.
 A cache must maintain a dictionary with categories as keys and product'names
 as values. Redis is a good candidate for this.

+Write on the many to many and rebuid the cache, read on the cache.
+how to display it in admin?
## [BAD_SMELL](BAD_SMELL.md)

## [TODO](TODO.md)

## [README](README.md)
