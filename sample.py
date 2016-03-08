# sample = [1,["another","list"],("a","tuple")]
# mylist = ["List item 1",2,3.14]
# #print(mylist[:])
# #print(mylist[0:2])
# #print(mylist[-3:-1])
# #print(mylist[1:])
# #print(mylist[::2])

# mylist[0] = "List item 1 again"
# #we are changing the item.
# mylist[-1] = 3.21
# #Here,we refer to the last item.
# mydict = {"key 1": "Value 1", 2:3,"pi": 3.14}
# mydict["pi"] = 3.15
# #This is how you change dictionary values.
# mytuple = (1,2,3)
# myfunction = len
# #print(myfunction(mylist))



#print("This %(verb)s a %(noun)s." %{"noun": "test","verb": "is"})


# rangelist = range(10)
# #print(rangelist)
# #[0,1,2,3,4,5,6,7,8,9]
# #for number in rangelist:


#if number in (3,4,7,9):
#    break
#else:
#   continue


# if rangelist[1] == 2:
# 	print("The second item (lists are 0-based) is 2")
# elif rangelist[1] ==3:
#     print("The second item (lists are 0-based) is 3")
# else:
#     print("Dunno")
# while rangelist[1] ==1:
#         		pass        	



#作业等同于def funcvar(x): return  x+1
# funcvar = lambda x: x+1
# print(funcvar(1))

#an_int 和 a_string 是可选参数，它们有默认值
#如果调用 passing_example 时只指定1个参数，那么 an_int 缺省为2,a_string缺省为 A default string。
#如果调用 passing_example 时指定了前面2个参数，a_string仍缺省为 A default string。
#a_list 是必备参数，因为它没有指定缺省值。
# def passing_example(a_list,an_int=2,a_string="A default string"):
# 	a_list.append("A new item")
# 	an_int = 4
# 	return a_list,an_int,a_string

# my_list = [1,2,3]
# my_int =10
# print(passing_example(my_list,my_int))
# print(my_list)
# print(my_int)


# class MyClass(object):
# 	common = 10
# 	def __init__(self):
# 		self.myvariable = 3
#     # def myfunction(self,arg1,arg2):
#     # 	return self.myvariable

# # classinstance = MyClass()
# # # classinstance.myfunction(1,2)

# # classinstance2 = MyClass()
# # # classinstance.common
# # # print(classinstance.common)		

# # MyClass.common =30
# # # classinstance.common
# # # print(classinstance.common)

# # MyClass.common = 50

# # classinstance.common = 10
# # classinstance.common
# # print(classinstance.common)
# # print(classinstance2.common)




# class OtherClass(MyClass):
	
# 	def __init__(self, arg1):
# 		self.myvariable =3
# 		print(arg1)
		
# classinstance = OtherClass("hello")

# # classinstance.myfunction(1,2)


# classinstance.test = 21
# classinstance.test
# print(classinstance.test)




# def some_function():
# 	try:
# 	     10/0
# 	except ZeroDivisionError:
# 		print("Oops,invalid.")
# 	else:
# 		pass
# 	finally:
# 		print("We are done with that.")

# some_function()



# import random
# from time import clock

# randomint = random.randint(1,100)
# print(randomint)





# import pickle
# mylist = ["This","is ",4,13327]
# # myfile = open(r"c:\\binary.dat","w")
# # pickle.dump(mylist,myfile)
# # myfile.close()

# # myfile =open(r"c:\\text.txt","w")
# # myfile.write("This is a  sample string")
# # myfile.close()

# # myfile = open(r"c:\\text.txt")
# # print(myfile.read())
# # myfile.close()


# myfile = open(r"C:\\binary.dat")
# loadedlist = pickle.load(myfile)
# myfile.close()
# print(loadedlist)



lst1 = [1,2,3]
lst2 = [3,4,5]
print([x*y for x in lst1 for y in lst2])
print([x for x in lst1 if 4 > x >1])

print(any([i%3 for i  in[3,3,4,4,3]]))

print(sum(1 for i in [3,4,4,4,3] if i ==4))

del lst1[0]
print(lst1)
del lst2[2]
print(lst2)





number = 5

def myfnc():
	print(number)

def anotherfunc():
    print(number)
    number = 3

def yetanotherfunc():
    global number

    number = 3 

       	