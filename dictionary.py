
student_data = {'id1':
{'name': ['Ira'], 'class': ['VII'], 'subject_integration': ['english, math, science']},

'id2':
{'name': ['Smayan'], 'class': ['VII'], 'subject_integration': ['english, math, science']},

'id3':
{'name': ['Rushathi'], 'class': ['VII'], 'subject_integration': ['english, math, science']},

'id4':
{'name': ['Anaya'], 'class': ['VII'], 'subject_integration': ['english, math, science']},

'id5':
{'name': ['Anika'], 'class': ['VII'], 'subject_integration': ['english, math, science']},}

result= {}


for key, value in student_data.items():
    if value not in result.values():
        result[key]= value
print(result)