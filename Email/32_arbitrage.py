"""  
Suppose you are given a table of currency exchange rates, 
represented as a 2D array. Determine whether there is a possible arbitrage: 
that is, whether there is some sequence of trades you can make, 
starting with some amount A of any currency, so that you can end up with 
some amount greater than A of that currency.

There are no transaction costs and you can trade fractional quantities. 
"""
""" 
the 2D array is essentially and adjacency matrix where matrix[i][j] = the exchange rate 
when trading currency i for currency j

create a node list
starting from the base currency move through the graph using the edgeweight given by the adjacency matrix
to calculate the current value of the currency. 
When the traversal comes back to the base currency check if the new value is greater than the initial value
This will be done recursively

Edge cases:
need to keep track of the recursion stack somehow so that we dont enter into infinite cycles

"""