# built in functions/standard library functions
y=max(45,89,75,999,56,43)

print("the maximum value is",y)

#user defined functions

def school():
    print("eMobilis")


def add():
    num1=4
    num2=5
    print(num1+num2)


add()

#parameter/variable and argument/value stored
def multiply(a,b):

    print(a*b)

multiply(24,56)
multiply(78,49)


def employee (name,age,gender,salary,postion):

    print(name,age,gender,salary,postion)

employee("Maurine",30,"female",560000,"CEO")
employee("Mark",50,"male",80000,"managing director")
employee("John",50,"male",80000,"managing director")
employee("John",50,"male",80000,"managing director")
employee("John",50,"male",80000,"managing director")


#program to display details of 5 patients
#Using a user defined function implment parameter and argument
#fullname,gender,age,disease

def patient (fullname,gender,age,disease):

    print(fullname,gender,age,disease)

patient("Mark Mende","male",34,"malaria")
patient("John Mwendwa","male",44,"cancer")
patient("Mary Ochieng","female",32,"bilharzia")
patient("Peter Wanyonyi","male",20,"malaria")
patient("Jane Kenyatta","female",14,"polio")




