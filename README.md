# Shopping Test
Coding test

## ShoppingCart()
Items are added as a unique entry and if subsequent items are added the count is increased. 
Items can be removed one by one or all of one type or the cart completely cleared. 
The cart can provide information on the total count of a specified item, total number of items, 
total cost and median price. The class has no support for different currencies, 
any conversion is assumed to be done by ordering software.
Items added to cart are checked for validity and not added if invalid and error logged.
Prices are returned as floats rounded to 2 decimal places as floats.

## ShoppingItem()
This is a base class stubbed out to represent a generic item for the purposes of testing the shopping cart.
It is assumed any items passed to the shopping cart class would have a fully implemented sub-class and 
include the price and name properties.
Prints out name and price as float to 2 decimal places.

## Utilities
This module contains some helper functions
### get_median()
Normally use would be made of numpy's median function or for python 3, statistics.median() but if these are
unavailable a helper function is included.
### sort_numbers()
Normally use would be made of pythons inbuilt list.sort() if a list was required to be sorted in place or
sorted() where a non list was used or a new list was required from the result.
These use the Timsort algorithm but for this helper function a simpler quicksort algorithm has been used.
This function provides the function to return a new list or in place sorting of the passed list.
The get_median() function also makes use of this method but uses the copy option to return a new list
in order to preserve the original list when the median price is returned
