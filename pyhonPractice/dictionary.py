#Dictionaries are used to store data values in key:value pairs.
#Dictionaries are written with curly brackets, and have keys and values:
#Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
#Duplicates Not Allowed

dict = {'Country': 'India', 'City': 'Hyderabad'}

print(dict)

dict.pop('City')

#adding:
dict['Town']='Kakinada'
dict.update({'District': 'East Godavari'})

#multiple

print(dict)
