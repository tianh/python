#author: sight_cold
#date:   2017/9/25
name=input("Name:")
age=int(input("Age:"))
job=input("Job:")
salary=input("Salary：")

if salary.isdigit():
    salary=int(salary)
msg="""
------------info of %s----------
Name:%s
Age:%d
Job:%s
Salary:%d
You will be retired in %s years
------------end------------
""" %(name,name,age,job,salary,65-age)license
print(msg)
