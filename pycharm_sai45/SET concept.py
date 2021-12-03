# concept 'SET' & it is a unordered collection of the data.
a={1,2,3,'sai','tyson','kenta',278.567,0.9,734.56}
print("given set: ",a,type(a), '\n address of set: ',id(a))
print("length of the static set: ",len(a))
a.add('prabhuram',) # add() ===> takes only one argument.
print("items added to static set: ",a)
a.update(['apple',1,4,8,10,9])
print("updated static set: ",a)
b={'dr.B','ziggaraout','pluto',297.56,17654,920230}
print("second set: ",b, type(b),"\n length of second set: ",len(b))
b.remove(297.56) # remove()===> takes only one argument.
print("item deleted from second set: ",b)
b.discard('pluto') # discard()===> takes only one argument.
print("item deleted from second set: ",b)
d={'power','voltage'}
# join two sets using union().
c = a.union(b,d) # union() takes only multiple arguments.
print("union of set 'a' and 'b': ",c,"\nlength of the union set: ",len(c),"\ntype of the union set: ",type(c))
d.clear()
print("cleared set: ",d)
d.update(['resistance','power','voltage',100])
print("updated third set: ",d,type(d))
del d
print("deleted set 'd' successfully")
# operations on the sets.
setA = {4,5,6,9}
setB = {1,2,5,6,8}
print("setA and setB: ",setA,setB)
print("intersection operation sets: ",setA & setB)
print("union operation on sets: ",setA | setB)
print("difference of the sets: ",setA - setB)
print("difference of the sets: ",setB - setA)
