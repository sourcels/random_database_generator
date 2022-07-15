import json
import string
from typing import Dict, List
from random import randint, shuffle, choice

class Generator():
    def __init__(self):
        self.names = ["Henry", "Alice", "John", "Marzipan", "Dima", "Dan", "Anna", "Kate", "David", "Felix", "George", "Rachel", "Max", "Daniel", "Sasha", "Andrea"]
        self.s_names = ["Blackwooth", "Northest", "Richter", "Shiper", "Herrington", "Teltow", "Askrop", "Biss", "Koval", "Kustk", "Xian", "Stein", "Minch", "Brown", "Ohl", "Raumen"]
        self.genders = ["Man", "Woman", "Other"]
        self.jobs = ["Farmer", "Program Engineer", "Program Distributor", "CEO", "Data Scientist", "UIX Designer", "Designer", "Backend Developer", "Frontend Developer", "Fullstack Developer", "Devops", "Tester", "Publisher", "Builder"]
        self.alphabets = list(string.ascii_letters)
        self.digits = list(string.digits)
        self.special_characters = list("!@#$%^&*()")
        self.characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

    def difference(self, obj1, obj2) -> Dict:
        if not obj1 or type(obj1) != dict:
            raise ValueError(f"obj1 must be dict, not {type(obj1).__name__}!")
        if not obj2 or type(obj2) != dict:
            raise ValueError(f"obj2 must be dict, not {type(obj2).__name__}!")
        return {key: obj2[key] for key in obj1 if obj1[key] != obj2[key]}

    def generate_random_password(self, length) -> str:
        if type(length) != int:
            raise ValueError(f"min_random_entry must be int, not {type(length).__name__}!")
        
        alphabets_count = int(length / 3)
        digits_count = int(length / 3)
        special_characters_count = int(length / 3)

        characters_count = alphabets_count + digits_count + special_characters_count
        if characters_count > length:
            raise ValueError("Characters total count is greater than the password length!")

        password = list()
        for i in range(alphabets_count):
            password.append(choice(self.alphabets))

        for i in range(digits_count):
            password.append(choice(self.digits))

        for i in range(special_characters_count):
            password.append(choice(self.special_characters))

        if characters_count < length:
            shuffle(self.characters)
            for i in range(length - characters_count):
                password.append(choice(self.characters))

        shuffle(password)
        return "".join(password)

    def generate_user(self) -> Dict:
        item = dict()
        name = randint(0, len(self.names)-1)
        s_name = randint(0, len(self.s_names)-1)
        gender = randint(0, len(self.genders)-1)
        job = randint(0, len(self.jobs)-1)

        item['user'] = f"{self.names[name]} {self.s_names[s_name]}"
        item['age'] = randint(18, 90)
        item['sex'] = self.genders[gender]
        item['job'] = self.jobs[job]
        item['login'] = f"{self.names[name][:4]}{self.s_names[s_name][2:]}_{randint(10000, 99999)}"
        item['password'] = f"{self.generate_random_password(length=randint(10, 20))}"
        return item

    def return_schema(self) -> Dict:
        data = dict()
        data['user'] = "string"
        data['age'] = "int"
        data['sex'] = "string"
        data['job'] = "string"
        data['login'] = "string"
        data['password'] = "string"
        return data

    def create_users_list(self, user_amount) -> List:
        results = list()

        for i in range(user_amount):
            results.append(self.generate_user())

        return sorted(results, key=lambda d: d['user'])

    def generate_json(self, indent = None, user_amount = 1, path = "file.json") -> None:
        data = json.dumps(self.create_users_list(user_amount), indent=indent)
        try:
            file = open(path, "w")
            file.write(data)
            file.close()
            print(f"Successfully created file in {path}")
        except FileNotFoundError:
            print(f"Invalid path to file")
        return None

gen = Generator()
generate_json = gen.generate_json
create_users_list = gen.create_users_list
generate_password = gen.generate_random_password
generate_user = gen.generate_user
return_schema = gen.return_schema
