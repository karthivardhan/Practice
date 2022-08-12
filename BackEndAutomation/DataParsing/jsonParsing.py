import json

courses = '{"name": ["Karthikeya", "Devaansh"], "languages": ["Python", "JavaScript"]}'

#Loads method parse json string and it returns disctionary
dict_courses = json.loads(courses)
print(type(dict_courses))
print(dict_courses)
print(dict_courses['name'])

list_languages = dict_courses['languages']
print(type(list_languages))
print(list_languages[0])


