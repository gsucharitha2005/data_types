#iterable/sequence datatypes
#list
class_room=["students",(1,2,3,4,5),{"std_name":"bhavi"},[1,6,72,9],3+4j] #heterogenious
print(class_room)
print(type(class_room))

student_marks=[1,46,57,34] #homogenious
print(student_marks)
print(type(student_marks))

#list is mutable

employe=["salary","emp_id","department","experiance"]
employe[0]="emp_data"
print(employe)

employee_details=[{"emp_id":123,"emp_name":"suchi","emp_contacts":(12334567890,7898761234)}]
employee_details[-1]["emp_contacts"][0]=123456675



