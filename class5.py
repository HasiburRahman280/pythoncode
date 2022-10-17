# class Firstclass:
#     a=5
#     b=80
# stu1=Firstclass()
# stu2=Firstclass()
#
# print(stu1.a,stu1.b)
# print(stu2.a,stu2.b)

class MyCal:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def multiplication(self,a,b):
        return a*b
    def division(self,a,b):
        return a/b

x=int(input("Enter value x : "))
y=int(input("Enter value y : "))
z=input("+,-,*,/or x for exit:")

Cal=MyCal()
if z=='+':
 print (Cal.add(x,y))
elif z=='-':
 print (Cal.sub(x,y))
elif z=='*':
 print (Cal.multiplication(x,y))
elif z=='/':
 print (Cal.division(x,y))
elif z=='x':
 exit()


# class Cal:
#     def add(self,num1,num2):
#         return num1+num2
#     def sub(self,num1,num2):
#         return num1-num2
#     def multi(self,num1,num2):
#         return num1*num2
#     def divi(self,num1,num2):
#         return num1/num2
# cl=Cal()
# jok=cl.add(12,20)
# biyog=cl.sub(12,2)
# gun=cl.multi(12,2)
# vag=cl.divi(12,2)
# print("Add",jok)
# print("Sub",biyog)
# print("multi",gun)
# print("divi",vag)

# class abc:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def add(self):
#         return self.a+self.b
#     def sub(self):
#         return self.a-self.b
#     def mul(self):
#         return self.a*self.b
# object=abc(20,10)
# print(object.add())
# print(object.sub())
# print(object.mul())

