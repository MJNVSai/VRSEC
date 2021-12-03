# concept 'dictionary'.
# ex:- dict={key1:value1,key2:value2}
blader = {1:'tyson',2:'kai',4:'max',3:'ray',5:'diachi',6:'hilari'}
print("dictionary: ",blader,type(blader),   id(blader))
print("best blader: ",blader[1],"\nstrongest blader: ",blader.get(2))
# get() ===> takes only key.
print("unknown: ",blader.get(10,'not found'),"\tknown: ",blader.get(6,'not found'))
blader[6]='madoka'
print("updated dictionary: ",blader,"\tlength of the dictionary: ",len(blader))
blader['world']='beyblade'
print("items added to dict: ",blader)
student = {'mounav':'it','keerthi':'civil','sasi':'it1','kumar':'ece','dhruthi':'eie'}
print("student dict: ",student,"\tstudent type: ",type(student))
print("length of the student: ",len(student))
# delete item from dict
student.pop('dhruthi') # takes only one argument.
print("decresed student: ",student,"\tlength of the student: ",len(student))
del student['keerthi']
print(student,"\t",len(student))
college = {1:'vrsec',2:'pvp',3:'lrbr',4:'vit'}
bit = {'tyson':'dragoon','kai':'dranzer','max':'dracial','ray':'drigger'}
print(college,bit)
college.clear()
print("cleared college: ",college)
del bit
print("deleted")
# nested dictionary.
student1 = {'mounav':{'roll':22,'branch':'it'},'mohith':{'roll':46,'branch':'ece'}}
print("nested student: ",student1,type(student1))
print("accesing the items: ",student1['mounav'],"\tmounav rollno: ",student1['mounav']['roll'])
print("accesing nested dict: ",student1['mohith']['branch'])
student2 = student1.copy()
print("student2 dict: ",student2,type(student2))
# using fromkeys()===> takes two arguments.
keyset=('key1','key2','key3')
dictionary1 = dict.fromkeys(keyset)
print("without value: ",dictionary1)
dictionary2 = dict.fromkeys(keyset,50)
print("with value: ",dictionary2)
# using items()===> returns key-value pair.
print("key-value pairs: ",blader.items())
# using key()===> it returns all the keys from the dictionary
print("keys of the blader are: ",blader.keys())
# using values()===> it returns values of the dictionary.
print("values of the blader are: ",blader.values())
# using setdefault()
print("student dictionary: ",student)
x = student.setdefault('mounav')
print("branch is: ",x)
student.setdefault('dhruthi')
print("dictionary student: ",student)
student.setdefault("vamsi","eie")
print("added student dictionary: ",student)
print("updated student info: ",student)
student.update({'dhruthi':'eie'})
print("updated student info: ",student)