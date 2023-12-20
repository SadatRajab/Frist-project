# def twice(y,x):
#     return y(y(x))
# def mul(x):
#     return x**2
# out=twice(mul,2)
# print(out)
# #--------------------------------------
# #--------------------------------------
# a=[1,2,3]
# b=a
# c=list(a)
# print(id(a),id(b),id(c))
# #---------------------------------------------------------
# #---------------------------------------------------------
# d={
#     1:'one',
#     2:'two',
#     3:'three',
# }
# for key , value in d.items():
#     print(key,value)
# #------------------------------------------------------------    
# #------------------------------------------------------------
# a={x for x in 'adjhbsdhwd'if x not in 'abc'}    
# print(a)
# #----------------------------------------------------
# #----------------------------------------------------
# class Customer:
#     def set_name(self,new_name):
#         self.name=new_name
#     def display(self):
#         print(self.name)
# x=Customer()
# print(x)
# x.set_name("Anwar")
# x.display()
# --------------------------------------------------------
# --------------------------------------------------------
# --------------------------------------------------------
# class Customer:
#     def	__init__(self, name, balance=0):  
#         self.name = name
#         self.balance = balance
#         print("The	init	method was called")
        
#     def __str__(self):
#         return 'Customer : ' +str(self.name)+ ' , balance: ' + str(self.balance) 
    
#     def __add__(self, other): # On "self + other"
#         return Customer("Test_Customer",self.balance + other)

# cust = Customer("Lara de Silva") # <-- don't specify balance explicitly  print(cust.name)
# print(cust.balance) # <-- attribute is created anyway
# print("#"*20)
# print(cust)
# print("#"*20)

# c2 = cust + 230
# print(c2.balance)
# print("#"*20)
# print(c2.balance)
# print("#"*20)
# del cust #make delet all the class
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
# class persson(object):#object=> مهناها انو تدخل المعطيات الي هدخاها
#     def __init__(self,name,idnumber):
#         self.name=name
#         self.idnumber=idnumber
#     def Desplay(self):
#         print("name:",self.name)    
#         print(self.idnumber)

# class Employee(persson):
#     def __init__(self,name,idnumber,salary,post):
#         self.salary=salary
#         self.post=post
#         persson. __init__(self,name,idnumber)# persson كده عملنا وراثة لل 
#     def Desplay(self):
#         print("name:",self.name)    
#         print(self.idnumber)
#         print(self.post)
#         print(self.salary)


# a=Employee("anwar",20220112,15000,"osama")
# a.Desplay()
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------

# class f1:
#     def __init__(self):
#         self.str1="hi"
#         print('str1')

# class f2:
#     def __init__(self):
#         self.str2="welcom"
#         print("str2")

# class plus(f1,f2):
#     def __init__(self):
#         f1.__init__(self)
#         f2.__init__(self)
#         print('plus')
#     def desplay(self):
#         print(self.ste1,self.str2)

# pl=plus()
# pl.desplay
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
# class father:
#     def __init__(self,name,age,idnumber):
#         self._name=name
#         self._age=age
#         self._idnumber=idnumber
    
#     def _display(self):
#         print("name:",self._name)
#         print("age:",self._age)

# class cld(father):
#     def __init__(self,nm,ag,id):
#         father.__init__(self,nm,ag,id)

#     def dis(self):
#         print("idnumber:",self._idnumber)
#         self._display()
# ob=cld('ahmed',19,11001) 
# ob.dis()    
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#///////ster , getr\\\\\\\\\\\\\\\\\\\\

# class father:
#     def __init__(self,name,age,idnumber):
#         self.__name=name
#         self.__age=age
#         self.__idnumber=idnumber
#     def __display(self):
#         print('name:',self.__name)
#         print('age:',self.__age)
#         print('idnumber:',self.__idnumber)

#     def accessprivatdisplay(self):
#         self.__display()

#     def get_name(self):
#         return self.__name
    
#     def set_name(self,name):
#         self.__name=name
    
#     def get_age(self):
#         return self.__age
    
#     def set_age(self,age):
#         self.__age=age

#     def get_idnumber(self):
#         return self.__idnumber
    
#     def set_idnumber(self,idnumber):
#         self.__idnumber=idnumber

# ob=father("anwar",19,20220112)
# ob.set_age(35)
# print("age",ob.get_age())
# ob.accessprivatdisplay()
#---------------------------------------------------------------------
#---------------------------------------------------------------------
# def product(a,b):
#     p=a*b
#     print(p)

# def product(a,b,c):
#     p= a *b * c
#     print(p)

# product(4,5)

#-----------------------------------------------------------------------------
# def add (datatype,*args):
#     if datatype=="int":
#         answer=0
    
#     if datatype=="str":
#         answer=""
#     for x in args:
#         answer=answer+x
#     print(answer)

# add("int",20,30,15)
# add("str","an","wa","r")
#------------------------------------------------------------
# def add(a=None , b=None):
#     if a!=None and b==None:
#         print(a)
#     else:
#         print(a+b)
# add(1)
# add(15,2)
#------------------------------------------------------------
#------------------------------------------------------------
# from asyncore import dispatcher_with_send


# @dispatch(int,int,int)
# def product(frist,second,third):
#     result=frist*second*third
#     print(result)

# @dispatcher_with_send(float,float,float)

# def product(frist,second,third):
#     result=frist*second*third
#     print(result)

# product(10,1,2)
#------------------------------------------------------------
#------------------------------------------------------------
# from abc import ABC , abstractmethod

# class polygom(ABC):
    
#     @abstractmethod
#     def noofsidas(self):
#         pass

# class Triangke(polygom):

#     def area(self):
#         print("I have ")
    
# class Mexagon(polygom):

#     def noofsidas(self):
#         print("I have 6 siad")
        
# class Circle (polygom):

#     def noofsidas(self):
#         print("I have 4 siad") 
#------------------------------------------------------------
#------------------------------------------------------------            

# def f1():
#     print("this f1")
#     def f2():
#         print("this f2")
#       f2()
    
# f1()
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
# x=5
# y="hi"
# try:
#     z=x+y
# except TypeError:
#     print('its error')
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
# def fun(a):
#     if a<4:
#         b=a/(a-3)
#     print("value of b =",b)  
# try:
#     fun(3)
#     fun(5)
# except ZeroDivisionError:
#     print("you are Division 0")  
# except NameError:
#     print("print name error")
#------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------
# import calc as ca


# print(ca.add(5,7))
# print(ca.subtract(10,5))

