# def person(name,id,dept):
#     return name,id,dept
#
# p1=person('hasibur','280','cse')
# print('1st person',p1)
# p2=person('hasib','280','cse')
# print('2nd person',p2)
# p3=person('korim','280','cse')
# print('3nd person',p3)
# p4=person('jakir','280','cse')
# print('4th person',p4)
# p5=person(5th person',kuddus','320','eee')
# print(p5)

# def shop_total(*args):
#     print(type(args))
#     sum=0
#     for amount in args:
#         sum=sum+amount
#     return sum
# total_amount=shop_total(10,20,30,40)
# print('total amount',total_amount)

#--------argument--------
def shop_total_sale(*args):
    print(type(args))
    sum = 0
    for amount in args:
        sum = sum + amount
    return sum

total_amount = shop_total_sale(10,60,23,44,33,92,12,44,40,30)
print('Total Sale Amount : ', total_amount)

#----------x^2 argument----
# def add(**kwargs):
#     print(type(kwargs))
#     sum = 0
#     for key in kwargs:
#         sum = sum + kwargs[key]
#     return sum
# total = add(a=4,b=6,c=3,d=2)
# print(total)