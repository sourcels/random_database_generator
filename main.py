import json
from random import randint

# data source
results = list()
names = ["Henry", "Alice", "John", "Marzipan", "Dima", "Dan", "Anna", "Kate", "David", "Felix", "George", "Rachel", "Max", "Daniel"]
s_names = ["Blackwooth", "Northest", "Richter", "Shiper", "Herrington", "Teltow", "Askrop", "Biss", "Koval", "Kustk", "Xian", "Stein", "Minch", "Brown"]
genders = ["Man", "Woman", "Other"]
jobs = ["Farmer", "Program Engineer", "Program Distributor", "CEO", "Data Scientist", "UIX Designer", "Designer", "Backend Developer", "Frontend Developer", "Fullstack Developer", "Devops", "Tester", "Publisher"]

# user amount
users_amount = randint(1, 100)

# data generation
for i in range(users_amount):
    item = dict()
    name = randint(0, len(names)-1)
    s_name = randint(0, len(s_names)-1)
    gender = randint(0, len(genders)-1)
    job = randint(0, len(jobs)-1)

    item['user'] = f"{names[name]} {s_names[s_name]}"
    item['age'] = randint(18, 90)
    item['sex'] = genders[gender]
    item['job'] = jobs[job]
    item['login'] = f"{names[name][:4]}{s_names[s_name][2:]}_{randint(10000, 99999)}"
    item['password'] = f"{randint(100000, 999999)}_{randint(222222, 888888)}"

    results.append(item)

# prettify data
results = sorted(results, key=lambda d: d['user'])
jsonString = json.dumps(results, indent=4)

# writing file
jsonFile = open("data.json", "w")
jsonFile.write(jsonString)
jsonFile.close()