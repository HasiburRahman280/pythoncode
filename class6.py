# class hasibur:
#     def info(self,id,name,dept):
#         return id,name,dept
#
# class Student(hasibur):
#     def student_info(self,roll):
#         return roll
# stu_obj=Student()
# stu_v=stu_obj.info(30,'hasibur','cse')
# stu_v1=stu_obj.student_info(280)
# print(stu_v,stu_v1)
#
# class Teacher(hasibur):
#     def salary(self,salary):
#         return salary
# teacher=Teacher()
# print(teacher.info(40,'teachername','eee'))
# print(teacher.salary(40000))

# class hasibur:
#     def info(self,id,name,dept):
#         return id,name,dept
#
# class Student(hasibur):
#     def student_info(self,roll):
#         return roll
#
# class Teacher(hasibur,Student):
#     def student_info(self,salary,desig):
#         return
# teacher=Teacher()
# print(teacher.info(40,'teachername','eee'))
# print(teacher.salary(40000))

# ---------decerptor--------
# def d_fun(fun):
#     def wrapper():
#         print("########")
#         fun()
#         fun()
#         fun()
#         fun()
#         print('@@@@@@')
#     return wrapper()
# @d_fun
# def a_dec():
#     print('hello')
# a_dec


def uppercase_decorator(f):
    def change():
        func=f()
        make_uppercase=func.upper()
        return make_uppercase
    return change
@uppercase_decorator
def say_hi():
    name='hasibur'
    return name
print(say_hi())

@uppercase_decorator
def say_hii():
    return ('hello is there anyone')
print(say_hii())
