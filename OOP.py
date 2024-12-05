                   #object oriented programming 

#create class and object  [ class is just a design 
"""
class myclass():
    x=12
    y=32
    z=92
    adi=(x+y+z)
    sub=(x-y)
    mul=(x*y)
    div=(x/y)


obj1=myclass()
print(obj1.x)
print(obj1.y)
print(obj1.z)
print(obj1.adi)
print(obj1.sub)
print(obj1.mul)
print(obj1.div)



#(oop) class variable and class methods
class myclass():
    x=12
    y=32
    z=92
    
    def addnew(self,a,b):
        sum=self.x+self.y+self.z+a+b
        print(sum)
    def addnow(self):
        self.addnew(3,4)

obj=myclass()
obj.addnew(3,4)
obj.addnow()

#object oriented constructors
class myclass():
    x=10
    y=20
    def __init__(self,a,b):
        sum=self.x+self.y+a+b
        print(sum)

obj=myclass(5,15)


#instance variable [constructor er maddme variable add kora]
class myclass():
    x=10
    y=20

    def __init__(self,zvalue):
        self.z = zvalue
        
   

obj=myclass(15)
print(obj.z)



#change class variable using constructor param
class myclass():
    x=10
    y=20

    def __init__(self,xvalue):
        self.x=xvalue

obj=myclass(20)
print(obj.x)


#instance methods
class myclass():
    x=10
    y=30

    def __init__(self,zvalue,xvalue):
        self.z=zvalue
        self.x=xvalue
    def addtow(self):
        print(self.x+self.y+self.z)

obj=myclass(20,50)
obj.addtow()



#static property
#static method
class myclass():
    x=10
    y=20

    @staticmethod #[This is point of static method]
    def addtow():
        sum=myclass.x+myclass.y
        print(sum)

myclass.addtow()
     

#static variable
class myclass():
    x=10
    y=20

    @staticmethod 
    def addtow():
        sum=myclass.x+myclass.y
        print(sum)

print(myclass.x)
print(myclass.y)
object=myclass()
print(object.x)
print(object.y)


#single inheritance

class father:
    x = 10
    y = 20
    
    def add(self):
        print(self.x + self.y)

    def mul(self):
        print(self.x * self.y)

class son(father):   #[Inheritance]
    pass

obj=son()
obj.add()
obj.mul()
print(obj.x)
print(obj.y)


#multiple inheritance

class father:
    x = 10
    y = 20

    def add(self):
        print(self.x+self.y)

    def mul(self):
        print(self.x*self.y)

class mother:
    a = 30
    b = 40

    def sub(self):
        print(self.a-self.b)

    def div(self):
        print(self.a/self.b)


class son(father,mother):
    pass

obj=son()

#father
print(obj.x)
print(obj.y)
obj.add()
obj.mul()

#mother
print(obj.a)
print(obj.b)
obj.sub()
obj.div()


#multilevel inheritance
class Grandfather:
    x = 10
    y = 20

    def add(self):
        print(self.x+self.y)

    def mul(self):
        print(self.x*self.y)

class father(Grandfather):
    pass

class son(father):
    pass

#Grandfather
obj=Grandfather()
print(obj.x)
print(obj.y)
obj.add()
obj.mul()

#father
obj=father()
print(obj.x)
print(obj.y)
obj.add()
obj.mul()

#son
obj=son()
print(obj.x)
print(obj.y)
obj.add()
obj.mul()



#when parent class has, but the child class has not
class father:
    x=10
    y=20

    def __init__(self):
        print("father constructor")

    def addtow(self):
        print(self.x+self.y)

class son(father):
    pass

obj=father()
obj=son()
obj.addtow()

#when child class has, but the parent class has not
class father:
    x=10
    y=20


    def addtow(self):
        print(self.x+self.y)

class son(father):
    def __init__(self):
        print("son constructor")


obj=son()
obj=father()
obj.addtow()


#when parent child both has constructor

class father:
    x=10
    y=20

class father:
    def __init__(self):
        print("father constructor")

    def addtow(self):
        print(self.x+self.y)

class son(father):
    def __init__(self):
        print("son constructor")


obj=son()
obj=father()



#Accessing the parent constructor
class father:
    x = 10
    y = 20

    def __init__(self):
        print("father constructor")

    def addtow(self):
        print(self.x+self.y)

class son(father):
    def __init__(self):
        super().__init__()  #inheriance for father
        print("son constructor")
    
obj=son()

#(oop) static properties in inheritance 
#if parent has static properties child can access as it is like parent
class father:
    x = 10
    y = 20

    @staticmethod
    def addtow():
        print(father.x+father.y)

class son(father):
    pass

father.addtow()
son.addtow()



#if child has static properties parent cannot access as it is like child

class father:
    pass

class son(father):
    x = 10
    y = 20


    @staticmethod
    def addtow():
        print(son.x+son.y)


son.addtow()


#How child can access parent static and non static properties
class father:
    x = 10
    y = 20
    
    def addtowfather(self):
        return(self.x+self.y)
      

class son(father):

    def addtowson(self):
        sum=self.addtowfather()+20
        print(sum)
        

obj=son()
obj.addtowson()

#method overriding 
class father:
    x = 10
    y = 20

    def add(self):
        print(self.x+self.y)

class son(father):
    #overriding
    def add(self):
        print(self.x+self.y+20)

obj=son()
obj.add()


#oop abstract class and methods 
#what is abstract
#how to create a abstract class
#abstract class whitout enforcing abstract methods 
#abstract calss with enforcing one or abstract method

from abc import ABC,abstractmethod
class bangladesh(ABC):

    @abstractmethod
    def print10to20(self):
        pass

    @abstractmethod
    def print20to30(self):
        pass

    def print0to10(self):
        for i in range(11):
            print(i)

class dhaka(bangladesh):

    def print10to20(self):
        for i in range(21):
            print(i)
    
    def print20to30(self):
        for i in range(31):
            print(i)


obj=dhaka()
obj.print10to20()
obj.print0to10()
obj.print20to30()



#method overloading
#method overloading using default argument
class father:
    x = 10
    y = 20

    def addtow(self,a=0,b=0):  #[default argument(a=0,b=0)]
        print(self.x+self.y+a+b)

obj=father()
obj.addtow()
obj.addtow(10)
obj.addtow(10,10)

#method overloading using variable length arguments
class father:
    x = 10
    y = 20

    def addtow(self,a=0,b=0):
        print(self.x+self.y+a+b)

    def mymethod(self,*a): #[variable lenght argument (*--)]
        print(a)

obj=father()
obj.addtow()
obj.addtow(10)
obj.addtow(10,10)

obj.mymethod(1)
obj.mymethod(1,2)
obj.mymethod(1,2,3)
obj.mymethod(1,2,3,4)
obj.mymethod(1,2,3,4,5)



#public access modifiers 
#there are no restrictions on public attributes
#(inside class) + (child class) + (out side of class)

class car:
    brand="BMW"

    def display(self):
        print(f"our brand name is {self.brand}")
    
class child(car):
    def childclass(self):
        print(f"our brand name is {self.brand}")

obj=child()
obj.childclass()
print(obj.brand)



#protected modifier 
#prefixed with a single underscore _ are protected
#(inside class) + (child class) + (out side of class(xx))
class car:
    _brand="BMW"

    def parentclass(self):
        print(f"our brand name is {self._brand}")

class child(car):

    def childclass(self):
        print(f"our brand name is {self._brand}")

obj=child()
print(obj._brand)
obj.childclass()


#privete, modifiers 
#prefixed with a double underscore __ are protected
#(inside class) + (child class(xxx)) + (out side of class(xxx))
class car:
    __brand="BMW"

    def parentclass(self):
        print(f"our brand name is {self.__brand}")

class child(car):

    def childclass(self):
        print(f"our brand name is {self.__brand}")

obj=car()
obj.parentclass()


#getter
class car:
    __brand = "BMW"

    @property
    def brand(self):
        return self.__brand


obj=car()
print(obj.brand)

#setter
class car:
    __brand = "BMW"

    @property
    def brand(self):
        return self.__brand
    
    @brand.setter
    def brand(self,value):
        self.__brand=value

obj=car()

#set
obj.brand="toyta"

#get
print(obj.brand)
"""


#encapsulation 

class BankAccount:
    __balance=0

    
    #deposit
    def Deposit(self,amount):
        if amount>0:
            self.__balance +=amount
            print("deposit successfully")
        else:
            print("invlaid amount")

    #withdraw 
    def withdraw(self,amount):
        if amount>0 and amount<self.__balance:
            self.__balance -=amount
            print("withdraw")
        else:
            print("insufficient amount")


    #check balance
    
    def check_balance(self):
        return self.__balance

obj=BankAccount()
obj.Deposit(100)
print(obj.check_balance())
obj.withdraw(20)
print(obj.check_balance())