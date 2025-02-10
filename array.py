

courses= ["MIT","Cybersecurity","datascience"]

print(courses[1])
#looping thru array

for x in courses:
    print("course is",x)

    #aadding new element into an array
courses.append("Laravel")
print (courses)

#removing element
courses.remove("Cybersecurity")
print(courses)

