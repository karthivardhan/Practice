students = {"John":['Python', 'Selenium'], "Mike":['Java', 'Angular'], "David": ['Cypress', 'JavaScript']}
keys = students.keys()
for eachkey in keys:
    print("Courses taken by", eachkey,':')
    for eachCourse in students[eachkey]:
        print(eachCourse)