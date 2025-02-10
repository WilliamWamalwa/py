#use multi div add sub
#ent 1 num ,ent op, ent 2 num

num1=int(input("Enter 1st number: "))

op=input("input operator: ")

num2=int(input("Enter 2nd number: "))

if op in ("+"):
    print(num1+num2)
elif op in ('-') :
    print(num1 - num2)
elif op in ('*'):
    print(num1 * num2)
elif op in ('/'):
    print(num1 / num2)
else:
    print("invalid")