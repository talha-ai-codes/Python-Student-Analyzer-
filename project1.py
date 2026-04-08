print("==========SMART STUDENTS ANALYZER=============")
#step 1: creat empty dictionary to store student data
student = {}

#input name and marks of students and store them in dictionary
n = int(input("enter number student you want to store data: "))
for i in range(1,n+1):
    Name = input(f"enter name of student {i}:  ")
    Marks = int(input(f"enter marks for {Name}:  "))
    student[i] = {"name" : Name,"marks" : Marks}

print("---------------------------------------------------------")
print("---------------------------------------------------------")

#step 4: find highest and lowest marks taken by student
highest_marks = max(s["marks"] for s in student.values())
lowest_marks = min(s["marks"] for s in student.values())
print("higest marks : ",highest_marks)
print("lowest marks : ",lowest_marks)
#step5 take two variables to track multiple highest and lowest marks count
highest_count = 0
lowest_count = 0
#creat two lists to stor highest and lowest marks student names and marks
top_students = []
low_students = []
for key, s in student.items():
    if s["marks"] == highest_marks:
        highest_count += 1
        top_students.append(s["name"])
        
    if s["marks"] == lowest_marks:
        lowest_count += 1
        low_students.append(s["name"])

print("count of highest marks : ",highest_count)
print("count of lowest marks: ",lowest_count)
print("top students : ",top_students)
print("low students : ",low_students)

#creat a function grade to find grade of students
print("===========Students Grades based on their marks===============")
def grade(marks):
    if(s["marks"] >= 90):
        return "A"
    elif(s["marks"] >= 80):
        return "B"
    elif(s["marks"] >= 70):
        return "C"
    elif(s["marks"] >= 60):
        return "D"
    else:
        return "Fail"


print("\n------ STUDENT ANALYSIS ------\n")

for key,s in student.items():
    g = grade(s["marks"])
    status = "Pass" if s["marks"] >= 50 else "Fail"
    print(f"{s["name"]:<6} : Marks = {s["marks"]} | Grade = {g} | Status = {status}")

print("=========Averege marks taken by students=============")
# find averege marks take by students
total = sum(s["marks"] for s in student.values())
if n > 0:
    average = total/n
else:
    average = 0
print("averege: ",average)

print("=========Total Result===========")
#count number of pass and fail students
pass_students = 0
fail_students = 0
for s in student.values():
    if s["marks"] >= 50:
        pass_students += 1
    else:
        fail_students += 1
print("pass student : ",pass_students)
print("fail students : ",fail_students)

print("================the whole data of students is as follow============")
print(student)

