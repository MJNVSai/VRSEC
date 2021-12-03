# about concept of 'list'.
x=list(('tyson','kai','max','ray','diachi',500,250,25.678))
y=[20,20.3459,'sai','kill']
print("top beybladers in the world of beyblading",x)
print(type(x),  id(x))
# 'list' is represented with [        ].
numbers=[2,4,6,8,10,12,14,16,18,20]
print(numbers,  type(numbers),  id(numbers))
bladers=['gingka','kenta','kyoya','ryuga','aguma','yuki','king','masamune','dynamics','chrisis']
print(bladers,type(bladers))
a=[17,29,'rago','doji',97.56,89.999]
print(a,type(a),id(a))
# using index values.
print("individuals: ",x[0],x[4],numbers[7],numbers[9],bladers[6],bladers[9],a[1],a[3])
print("negative index values: ",x[-4],numbers[-9],bladers[-6],a[-4])
print('in between: ',numbers[4:7],bladers[7:],a[:4])
merge=[numbers,bladers,a]
print("merge list: ",merge)
numbers.append('mounav')
# append means it add the value to the list & it takes one argument only.
print(numbers)
bladers.insert(1,95)
# here '1' is a index number & '95' is a number to be added at index value '1'.
print(bladers)
print(y)
y.clear() # clear() means it clears the list.
print(y)
a.remove('rago') # it means it removes the string
print(a)
numbers.pop(5) # here '5' is a index number that means it removes the object at index 5.
print(numbers)
del x[4:7]
print(x)
x.extend([10,'hiro',25.9876,'reji'])
print("extended list 'x': ",x)
sai=[395,200,198,999,1150,95,76,29,80,100]
print("mininum number in list 'sai': ",min(sai))
print("maximum number in list 'sai': ",max(sai))
print("sum of numbers in list 'sai': ",sum(sai))
sai.sort()
print("sorted list of sai: ",sai)
x.reverse()
print("reversed list: ",x)