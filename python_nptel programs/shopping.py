# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 15:25:02 2021

@author: Krishna
"""
t1 = "lays"
t2 = "bingo"
t3 = "tiger"
t4 = [t1,t2,t3]
print(t4)

shopping = ["ginger","bambino","spinanch","salt","onions"]
print(shopping)


# append() is used to update the items in list
# it takes only one argument
shopping.append("tomato")
print(shopping)

# or we can also use insert()
# where it takes two arguments 1.location, 2.item name or a value
shopping.insert(1, "potato")  
print(shopping)


# to find length og the list we caN use len()
# it takes list name as a argument
print("shopping length: ",len(shopping))


ages = [12,23,34,42,15,87,12,16,25,23,82,57,7,3,2,3,1,20]
# we can find how many duplicate elements are there in a list
# by using count() function it takes only one argument 1.item name
print("no.of duplicate items of number 3: ",ages.count(3))



for i in shopping:
    print(i)
    
    
for j in ages:
    print(j,end=" ")
    
    
    
# sort() function can make list in an order
# the default order is asending order.
print()
ages.sort()
print("ordered list: ",ages)



# reverse() function can make items in list in reverse order
ages.reverse()
print("reverse order list: ",ages)